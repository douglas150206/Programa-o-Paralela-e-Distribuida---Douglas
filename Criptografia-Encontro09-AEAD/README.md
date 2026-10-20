# Introdução à Criptografia — Encontro 09: Criptografia autenticada (AEAD)

Resolução da lista de atividades do Encontro 09.

## Entrega

📄 **[`Encontro09-AEAD-atividades.docx`](Encontro09-AEAD-atividades.docx)** — 6 páginas, sem capa.

| Parte | Conteúdo |
|---|---|
| Atividades 1–10 | Respostas justificadas, com as etapas dos cálculos |
| Atividade 11 | Código, saída dos testes, respostas das tarefas 3 e 6 e parágrafo final |
| Desafio de fechamento | Campos de um registro AEAD: o que é guardado, secreto e único |

## Atividade 11 — como executar

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install cryptography
python atividade11_aead.py
```

- [`atividade11_aead.py`](atividade11_aead.py) — código executável.
- [`saida_testes.txt`](saida_testes.txt) — saída da execução (Python 3.11, cryptography 50.0.2).

A chave é gerada a cada execução e não é impressa; os tamanhos e os bytes de AAD e nonce são
determinísticos. O controle de repetição é didático: fica em memória e não trata concorrência.

## Resultados numéricos

| Atividade | Resultado |
|---|---|
| 2 | C = 23 B; C‖T = 39 B; registro = 58 B; a chave não entra |
| 3 | (a,bc) → `01 61 02 62 63`; (ab,c) → `02 61 62 01 63` |
| 4 | nonce `00 00 00 02 00 00 00 00 00 00 00 FF`; seguinte `… 00 00 01 00` |
| 5 | λ ≈ 2⁻²⁵ ≈ 2,98 × 10⁻⁸; P ≈ 2,98 × 10⁻⁸ |
| 6 | 2⁻⁶⁴ ≈ 5,42 × 10⁻²⁰ por tentativa; limite 2⁻⁴⁸ ≈ 3,55 × 10⁻¹⁵ |
