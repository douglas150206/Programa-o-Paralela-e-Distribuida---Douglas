# Introdução à Criptografia — Encontro 10: Fundamentos da criptografia de chave pública

Resolução da Lista 1 e da Atividade 11 do Encontro 10.

## Entrega

📄 **[`Encontro10-ChavePublica-atividades.docx`](Encontro10-ChavePublica-atividades.docx)** — 5 páginas, sem capa.

| Parte | Conteúdo |
|---|---|
| Lista 1 (questões 1–10) | Respostas justificadas, com cada redução modular registrada |
| Atividade 11 | Código, saída dos testes, análise das tarefas 3–5, tarefa 6 e hipóteses |

## Atividade 11 — como executar

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install cryptography
python atividade11_laboratorio.py    # sem -O, que desativaria as asserções
```

- [`atividade11_laboratorio.py`](atividade11_laboratorio.py) — oito testes em `unittest`: cinco para as
  tarefas 1 a 5 e três que conferem com `pow()` as contas da Lista 1.
- [`saida_testes.txt`](saida_testes.txt) — saída da execução (Python 3.11, cryptography 50.0.2).

Nenhuma chave privada, segredo compartilhado ou chave derivada é impressa. Uso didático, local e sem rede.

## Resultados numéricos

| Questão | Resultado |
|---|---|
| 2 | 66 chaves simétricas; 11 por pessoa; 12 pares assimétricos |
| 3 | 7⁵ mod 23 = 17 |
| 4 | A = 4, B = 10, segredo comum 18 |
| 5 | Mallory compartilha 18 com Alice e 7 com Bob |
| 6 | Limite OAEP de 318 bytes: nem 320 nem 319 cabem |
