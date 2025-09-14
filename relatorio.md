# Relatório – Simulação de Atendimento em Caixa de Supermercado

### 1) Resultados iniciais
A simulação com μ = 5,0, σ = 0,5, N = 100 e 1000 rodadas deu como resultado:  
- Média ≈ 252,9 minutos  
- Desvio-padrão ≈ 2,8 minutos  

---

### 2) Variação do número de caixas
Quando usei 1 caixa o tempo médio ficou em torno de 252 minutos.  
Com 2 caixas caiu para cerca de 127 minutos.  
Com 3 caixas diminuiu ainda mais, para perto de 86 minutos.  

Ou seja, quanto mais caixas, menor o tempo médio de atendimento, pois os clientes são atendidos em paralelo. O ganho é bem grande de 1 para 2 caixas, e um pouco menor de 2 para 3.

---

### 3) Variação de σ
Com σ = 0,25 o tempo médio ficou próximo de 252,7 minutos, com pouca variação.  
Com σ = 1,0 subiu levemente para 253,3 minutos e o desvio aumentou bastante.  
Com σ = 2,0 chegou a 254,5 minutos, e a variação entre rodadas ficou bem maior.  

Isso mostra que quanto maior o desvio padrão, maior a incerteza e a variabilidade dos resultados.

---

### 4) Por que o simulador é estocástico?
O simulador é estocástico porque os tempos de atendimento são sorteados de forma aleatória.  
Por isso, cada simulação dá um resultado um pouco diferente. Isso é parecido com a vida real, já que cada cliente demora tempos diferentes no caixa, dependendo da quantidade de compras e de imprevistos.
