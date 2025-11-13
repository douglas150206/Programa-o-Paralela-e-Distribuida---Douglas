# 🍴 Simulação do Jantar dos Filósofos — Testes com JUnit 5

Este repositório apresenta uma implementação simples utilizada para demonstrar testes unitários em **Java** utilizando **JUnit 5**.  
O projeto foi desenvolvido por **Douglas Hiroiti Kadomoto**, estudante de **Análise e Desenvolvimento de Sistemas** do **IFSP – Jacareí** (3º semestre).

A ideia é reproduzir a configuração inicial do conhecido problema de concorrência chamado **Jantar dos Filósofos**, muito discutido em disciplinas de paralelismo e sincronização.

---

## 🧠 Visão geral do problema

O Jantar dos Filósofos descreve uma situação em que:

- Cinco filósofos se sentam ao redor de uma mesa circular.
- Entre cada par de filósofos há um garfo.
- Para comer, o filósofo precisa usar **dois garfos** (esquerdo e direito).
- Enquanto não comem, eles **pensam**.
- O problema é tradicionalmente usado para estudar:
  - acesso concorrente a recursos,
  - estratégias de sincronização,
  - possíveis deadlocks.

Neste projeto, o foco está na **montagem da estrutura**, e **não** na implementação da concorrência real entre threads.

---

## 🧪 Funcionalidades implementadas

As seguintes classes compõem a lógica principal:

| Arquivo | Finalidade |
|---------|------------|
| `Garfo` | Representa um dos garfos compartilhados. |
| `Filosofo` | Define cada filósofo e os garfos associados a ele. |
| `Jantar` | Monta o ambiente inicial com os cinco filósofos e cinco garfos. |
| `JantarTest` | Realiza testes unitários verificando se a inicialização ocorre como esperado. |

O teste JUnit valida:

- criação correta das listas de filósofos e garfos;  
- quantidade de elementos (sempre 5);  
- cada filósofo possui dois garfos distintos;  
- estrutura circular da distribuição;  
- confirmação de que o jantar foi marcado como iniciado.