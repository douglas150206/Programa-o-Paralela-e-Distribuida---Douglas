"""Atividade 11 — Registro AEAD: adulteração, contexto e repetição.

Uso exclusivamente didático. O controle de repetição é mantido apenas em
memória e não trata concorrência: não oferece segurança real.
"""
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

TAM_AAD, TAM_NONCE, TAM_TAG = 7, 12, 16

aes = AESGCM(AESGCM.generate_key(bit_length=128))
nonce = (7).to_bytes(4, "big") + (9).to_bytes(8, "big")
aad = bytes([1]) + (17).to_bytes(2, "big") + (9).to_bytes(4, "big")
mensagem = b"nota=8.5"


def alterar(dados, indice):
    """Devolve uma cópia de `dados` com um bit invertido na posição `indice`."""
    copia = bytearray(dados)
    copia[indice] ^= 1
    return bytes(copia)


# Tarefa 1 — uma única cifração e a abertura do registro correto.
pacote = aes.encrypt(nonce, mensagem, aad)  # C seguido de T
recuperada = aes.decrypt(nonce, pacote, aad)
assert len(pacote) == 24
assert recuperada == mensagem

print("== Tarefa 1: cifração única e abertura válida ==")
print(f"AAD   : {len(aad):2d} bytes  {aad.hex(' ')}")
print(f"nonce : {len(nonce):2d} bytes  {nonce.hex(' ')}")
print(f"C     : {len(pacote) - TAM_TAG:2d} bytes")
print(f"T     : {TAM_TAG:2d} bytes")
print(f"C||T  : {len(pacote):2d} bytes")
print(f"registro A||N||C||T: {len(aad) + len(nonce) + len(pacote)} bytes (a chave fica fora)")
print(f"mensagem recuperada: {recuperada.decode()}")

# Tarefa 2 — cada caso parte do original e altera um único campo.
# O último caso (chave errada) completa a matriz da atividade 10.
outra = AESGCM(AESGCM.generate_key(bit_length=128))
casos = [
    ("primeiro byte de C", aes, nonce, alterar(pacote, 0), aad),
    ("último byte de T", aes, nonce, alterar(pacote, -1), aad),
    ("último byte do AAD", aes, nonce, pacote, alterar(aad, -1)),
    ("último byte do nonce", aes, alterar(nonce, -1), pacote, aad),
    ("chave errada", outra, nonce, pacote, aad),
]
print("\n== Tarefa 2: adulteração (um campo por teste) ==")
for nome, cifra, n, p, a in casos:
    try:
        cifra.decrypt(n, p, a)
    except InvalidTag:
        print(f"{nome:22s} -> InvalidTag (nenhum texto candidato usado)")
    else:
        raise AssertionError(f"aceitação indevida: {nome}")

# Tarefa 4 — a biblioteca não tem estado: abrir de novo o original passa.
print("\n== Tarefa 4: a biblioteca não implementa política de repetição ==")
for vez in (1, 2):
    assert aes.decrypt(nonce, pacote, aad) == mensagem
    print(f"decrypt do registro intacto, {vez}a vez -> sucesso")

# Tarefa 5 — controle didático de repetição, consultado após autenticar.
aceitas = set()


def receber(n, p, a, usuario_esperado):
    """Valida formato, autentica, confere contexto e repetição, nessa ordem."""
    if len(a) != TAM_AAD or len(n) != TAM_NONCE or len(p) < TAM_TAG:
        return "rejeitado: formato"
    try:
        m = aes.decrypt(n, p, a)
    except InvalidTag:
        return "rejeitado: etiqueta inválida"  # estado não é alterado
    versao = a[0]
    usuario = int.from_bytes(a[1:3], "big")
    sequencia = int.from_bytes(a[3:7], "big")
    if versao != 1:
        return "rejeitado: versão desconhecida"
    if usuario != usuario_esperado:
        return "rejeitado: contexto (usuário diferente do esperado)"
    if (usuario, sequencia) in aceitas:
        return "rejeitado: repetição"
    aceitas.add((usuario, sequencia))
    return f"aceito: {m.decode()}"


print("\n== Tarefa 5: controle de repetição após autenticação ==")
r = receber(nonce, pacote, aad, 17)
print("original, usuário esperado 17   ->", r)
assert r.startswith("aceito")

r = receber(nonce, pacote, aad, 17)
print("mesmo registro de novo          ->", r)
assert r == "rejeitado: repetição"

r = receber(nonce, pacote, aad, 18)
print("registro do 17 usado para o 18  ->", r)
assert r.startswith("rejeitado: contexto")

# Pacote forjado que anuncia a sequência 10: a etiqueta falha e a sequência
# não pode ficar "queimada", senão um atacante bloquearia mensagens futuras.
aad_falso = bytes([1]) + (17).to_bytes(2, "big") + (10).to_bytes(4, "big")
antes = set(aceitas)
r = receber(nonce, pacote, aad_falso, 17)
print("forjado anunciando sequência 10 ->", r)
assert r == "rejeitado: etiqueta inválida"
assert aceitas == antes and (17, 10) not in aceitas
print("estado após a falha             ->", sorted(aceitas), "(inalterado)")

print("\nTodos os testes passaram.")
