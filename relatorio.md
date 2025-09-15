# Resultados da Simulação

## 1) Cenário padrão
Rodei a simulação com **mu = 5,0**, **sigma = 0,5**, **N = 100** e **1000 rodadas**.  
A **média das médias** ficou perto de **5 minutos** e o **desvio das médias** ficou por volta de **0,05 min**.Ou seja, os resultados ficam bem concentrados perto do valor esperado.

## 2) Número de caixas (1, 2 e 3)
Troquei o número de caixas, mas **nesta versão do código isso ainda não muda a conta** (o campo existe, só não afeta o cálculo).  
Mesmo assim, a ideia por trás é simples: **mais caixas é igual ao atendimento em paralelo e filas menores**, então quando o modelo considerar filas a tendência é os tempos médios caírem.

## 3) Testes com sigma (0,25; 1,0; 2,0)
Quando aumentei o **sigma**, a **média** continuou próxima de 5 min, mas o **desvio** das médias **cresceu** (faz sentido, visto que mais variabilidade no atendimento individual acarreta em resultados mais espalhados entre rodadas).

## 4) Por que é estocástico?
É estocástico porque os tempos de atendimento são **sorteados** de uma distribuição normal.  
Mesmo com os mesmos parâmetros, cada execução dá números um pouco diferentes, o que parece com a vida real, ou seja, cada cliente leva um tempo diferente no caixa.
