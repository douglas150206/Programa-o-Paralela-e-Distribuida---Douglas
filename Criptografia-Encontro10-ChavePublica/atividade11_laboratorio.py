"""Atividade 11 — Laboratório de conexões certas e erradas (Encontro 10).

Uso exclusivamente didático: local, sem rede e com dados fictícios. Nenhuma
chave privada, segredo compartilhado ou chave derivada é impressa; os testes
só verificam comprimentos e igualdades. Execute sem a opção -O, que
desativaria as asserções.
"""
import secrets
import unittest

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

MENSAGEM = b"nota=8.5"
CONTEXTO = b"encontro10 v1 Alice->Bob"
AAD = b"Alice->Bob"
# Nonce fixo só porque cada chave nova cifra uma única vez neste experimento.
NONCE = bytes(12)


def derivar(segredo, sal, contexto=CONTEXTO):
    """Deriva 32 bytes com uma instância nova de HKDF-SHA256."""
    return HKDF(algorithm=hashes.SHA256(), length=32, salt=sal, info=contexto).derive(segredo)


def publica_bruta(privada):
    """Exporta apenas os 32 bytes da chave pública."""
    return privada.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)


class ConexaoCorreta(unittest.TestCase):
    def setUp(self):
        self.a = X25519PrivateKey.generate()
        self.b = X25519PrivateKey.generate()
        self.sal = secrets.token_bytes(16)  # público, igual nos dois lados

    def test_1_acordo_e_exportacao(self):
        """Tarefa 1: os dois acordos têm 32 bytes e coincidem; públicas com 32 bytes."""
        sa = self.a.exchange(self.b.public_key())
        sb = self.b.exchange(self.a.public_key())
        assert len(sa) == len(sb) == 32, "Implemente os dois acordos"
        assert sa == sb
        self.assertEqual(len(publica_bruta(self.a)), 32)
        self.assertEqual(len(publica_bruta(self.b)), 32)
        self.assertNotEqual(publica_bruta(self.a), publica_bruta(self.b))

    def test_2_derivacao_e_cifracao(self):
        """Tarefa 2: mesma HKDF dos dois lados; uma cifração e uma abertura."""
        ka = derivar(self.a.exchange(self.b.public_key()), self.sal)
        kb = derivar(self.b.exchange(self.a.public_key()), self.sal)
        self.assertEqual(len(ka), 32)
        self.assertEqual(ka, kb)
        pacote = AESGCM(ka).encrypt(NONCE, MENSAGEM, AAD)
        self.assertEqual(len(pacote), len(MENSAGEM) + 16)
        self.assertEqual(AESGCM(kb).decrypt(NONCE, pacote, AAD), MENSAGEM)

    def test_5_adulteracao_e_contexto(self):
        """Tarefa 5: byte alterado e contexto diferente levam a InvalidTag."""
        segredo_a = self.a.exchange(self.b.public_key())
        segredo_b = self.b.exchange(self.a.public_key())
        ka = derivar(segredo_a, self.sal)
        pacote = AESGCM(ka).encrypt(NONCE, MENSAGEM, AAD)  # única cifração sob ka

        alterado = bytearray(pacote)
        alterado[0] ^= 1
        with self.assertRaises(InvalidTag):
            AESGCM(derivar(segredo_b, self.sal)).decrypt(NONCE, bytes(alterado), AAD)

        # Mesmo segredo, outro contexto: a chave muda e o pacote não abre.
        outro = derivar(segredo_b, self.sal, b"encontro10 v1 Bob->Alice")
        self.assertNotEqual(outro, ka)
        with self.assertRaises(InvalidTag):
            AESGCM(outro).decrypt(NONCE, pacote, AAD)

        # Mesmo segredo e contexto, outro sal: a chave também muda.
        self.assertNotEqual(derivar(segredo_b, secrets.token_bytes(16)), ka)


class ConexaoComMallory(unittest.TestCase):
    """Mallory só usa a própria privada e as públicas que intercepta."""

    def setUp(self):
        self.a = X25519PrivateKey.generate()
        self.b = X25519PrivateKey.generate()
        self.m = X25519PrivateKey.generate()
        self.sal = secrets.token_bytes(16)

    def test_3_substituicao_de_uma_publica(self):
        """Tarefa 3: Alice recebe a pública de Mallory; Mallory abre, Bob não."""
        k_alice = derivar(self.a.exchange(self.m.public_key()), self.sal)
        k_mallory = derivar(self.m.exchange(self.a.public_key()), self.sal)
        k_bob = derivar(self.b.exchange(self.a.public_key()), self.sal)
        self.assertEqual(k_alice, k_mallory)
        self.assertNotEqual(k_alice, k_bob)

        pacote = AESGCM(k_alice).encrypt(NONCE, MENSAGEM, AAD)
        self.assertEqual(AESGCM(k_mallory).decrypt(NONCE, pacote, AAD), MENSAGEM)
        with self.assertRaises(InvalidTag):
            AESGCM(k_bob).decrypt(NONCE, pacote, AAD)

    def test_4_intermediario_nos_dois_sentidos(self):
        """Tarefa 4: Mallory abre na conexão com Alice e recifra na conexão com Bob."""
        k_alice = derivar(self.a.exchange(self.m.public_key()), self.sal)
        k_bob = derivar(self.b.exchange(self.m.public_key()), self.sal)
        k_m_alice = derivar(self.m.exchange(self.a.public_key()), self.sal)
        k_m_bob = derivar(self.m.exchange(self.b.public_key()), self.sal)
        self.assertEqual(k_alice, k_m_alice)
        self.assertEqual(k_bob, k_m_bob)
        self.assertNotEqual(k_alice, k_bob)  # duas conexões distintas

        pacote_alice = AESGCM(k_alice).encrypt(NONCE, MENSAGEM, AAD)
        lida = AESGCM(k_m_alice).decrypt(NONCE, pacote_alice, AAD)
        # Outra chave, logo o mesmo nonce não é reuso: cada chave cifra uma vez.
        pacote_bob = AESGCM(k_m_bob).encrypt(NONCE, lida, AAD)
        self.assertNotEqual(pacote_alice, pacote_bob)
        # Bob recebe uma etiqueta válida e não tem como perceber o ataque.
        self.assertEqual(AESGCM(k_bob).decrypt(NONCE, pacote_bob, AAD), MENSAGEM)


class ConferenciaDasContas(unittest.TestCase):
    """Confere com pow() as contas modulares da Lista 1 e do Exemplo 4."""

    def test_questao_3(self):
        """Questão 3: 7^5 mod 23 = 17."""
        self.assertEqual(pow(7, 5, 23), 17)

    def test_questao_4(self):
        """Questão 4: A = 4, B = 10 e os dois lados obtêm 18."""
        A, B = pow(5, 4, 23), pow(5, 3, 23)
        self.assertEqual((A, B), (4, 10))
        self.assertEqual(pow(B, 4, 23), pow(A, 3, 23))
        self.assertEqual(pow(B, 4, 23), 18)

    def test_exemplo_4(self):
        """Questão 5: Mallory compartilha 18 com Alice e 7 com Bob."""
        A, B, M = pow(5, 6, 23), pow(5, 15, 23), pow(5, 13, 23)
        self.assertEqual(M, 21)
        self.assertEqual(pow(M, 6, 23), pow(A, 13, 23))
        self.assertEqual(pow(M, 6, 23), 18)
        self.assertEqual(pow(M, 15, 23), pow(B, 13, 23))
        self.assertEqual(pow(M, 15, 23), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
