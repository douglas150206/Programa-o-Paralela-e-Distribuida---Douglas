# Lista 02 — Governança de TI

**Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas
**Disciplina:** Governança e Conformidade Tecnológica — JCRGCTC
**Prof.:** Lineu Mialaret
**Aluno:** Douglas
**Data:** 02/09/2026

---

## Questão 1 — Artigo "IT Governance on One Page"

> Referência: WEILL, Peter; ROSS, Jeanne W. **IT Governance on One Page**.
> MIT Sloan School of Management, Center for Information Systems Research (CISR),
> CISR Working Paper No. 349 / Sloan Working Paper No. 4516-04, novembro de 2004.

O artigo é resultado de duas pesquisas conduzidas pelo CISR do MIT: um levantamento com
CIOs de 256 empresas das Américas, Europa e Ásia-Pacífico e um conjunto de 40 estudos de
caso baseados em entrevistas, totalizando cerca de 300 organizações em 23 países.

---

### a) O que é Governança de TI?

Governança de TI é o **arcabouço de direitos de decisão e de responsabilização (accountability)
que serve para incentivar comportamentos desejáveis no uso da Tecnologia da Informação**. Em
outras palavras, é o conjunto de regras e estruturas que define **quem tem o direito de decidir
cada assunto de TI dentro da organização e quem responde pelos resultados dessas decisões**.

Alguns pontos que o artigo deixa claro sobre essa definição:

- **Ela reflete a governança corporativa como um todo.** A governança de TI não é uma ilha:
  ela espelha os princípios mais amplos de governança da organização, só que focada na gestão
  e no uso da TI para alcançar as metas de desempenho do negócio. Como a TI está ligada aos
  outros ativos da empresa (financeiro, humano, propriedade intelectual, físico e de
  relacionamento), é comum que ela compartilhe mecanismos com a governança desses outros
  ativos — comitês executivos e processos de orçamento, por exemplo.

- **Ela precisa ser desenhada de propósito.** A frase que resume o artigo é: *"governança de TI
  eficaz não acontece por acidente"*. Ela não pode ser o resultado acidental de mecanismos
  isolados (um comitê aqui, um SLA ali, um escritório de arquitetura depois) criados em momentos
  diferentes para apagar o incêndio da vez. As organizações de melhor desempenho **desenham**
  a governança conscientemente.

- **Ela precisa ser conhecida.** A pesquisa mostrou que, em média, **apenas 38% dos gestores
  seniores** sabiam como a TI era governada em suas empresas. E o grau de conhecimento da alta
  gestão sobre os processos de governança foi o **melhor indicador isolado de eficácia da
  governança**: nas empresas de melhor desempenho, 60%, 70% ou 80% dos executivos seniores
  sabiam como a TI era governada.

- **Ela dá retorno financeiro.** Empresas com governança de TI eficaz apresentaram **lucros cerca
  de 20% maiores** do que empresas que seguiam estratégias semelhantes com governança mais fraca
  (comparação feita com ROA, dentro da mesma estratégia). O desempenho da governança também se
  correlacionou estatisticamente com medidas financeiras de três anos, como ROE e crescimento do
  valor de mercado.

Para medir isso, os autores propõem uma autoavaliação em que a organização pondera a importância
de quatro objetivos e nota o próprio desempenho em cada um, gerando uma pontuação de 0 a 100:

1. uso da TI com boa relação custo-benefício;
2. uso eficaz da TI para **utilização de ativos**;
3. uso eficaz da TI para **crescimento**;
4. uso eficaz da TI para **flexibilidade do negócio**.

Na pesquisa, a média foi 69 pontos; só 17% das empresas passaram de 80 e apenas 7% passaram de 90.

---

### b) Qual a diferença entre Governança de TI e gestão de TI?

A diferença está em **"quem decide" versus "o que se decide e como se executa"**:

| | **Governança de TI** | **Gestão de TI** |
|---|---|---|
| **Pergunta que responde** | *Quem* tem o direito de tomar cada decisão e *quem* presta contas pelo resultado? | *O que* decidir e *como* executar no dia a dia? |
| **Natureza** | Arcabouço, desenho, regras do jogo | Tomada de decisão e execução dentro dessas regras |
| **Quem faz** | Desenhada pela alta administração | Exercida pelos gestores em todos os níveis, diariamente |
| **Horizonte** | Mais estável; tende a durar mais que a própria estrutura organizacional | Contínua e operacional |
| **Exemplo** | Definir que o comitê executivo decide os princípios e o investimento de TI, e que o CIO responde por arquitetura e infraestrutura (arranjo da UPS) | Escolher o fornecedor do storage, aprovar o cronograma do projeto, resolver um incidente |

A governança **não substitui** a gestão: ela cria as condições para que a gestão aconteça de forma
coerente. O artigo mostra isso quando diz que o primeiro passo para desenhar a governança de TI é
**determinar quem deve tomar — e por quem deve responder — cada área de decisão**. Depois disso é
que entram os **mecanismos** (comitês, processos de orçamento, acordos de nível de serviço,
chargeback, processos de arquitetura), e são justamente esses mecanismos que os **gestores
manipulam no dia a dia**, colocando a governança em prática.

Outra distinção importante do artigo: os arranjos de governança **transcendem a estrutura
organizacional** e costumam ser mais estáveis do que ela. Ou seja, em vez de reorganizar a empresa
toda vez que as prioridades mudam, é possível mudar mecanismos de governança para induzir novos
comportamentos — o que é mais barato e menos traumático do que uma reestruturação.

---

### c) Por que a definição de responsabilidades é importante?

Por três motivos que o artigo desenvolve:

**1. Porque os resultados da TI são difíceis de medir.** O artigo afirma diretamente que, como os
resultados de TI frequentemente são difíceis de mensurar, as organizações **precisam atribuir
responsabilidade pelos resultados desejados e avaliar o quanto eles foram atingidos**. Sem um
responsável nomeado, não há a quem cobrar — e o que não é cobrado não é entregue.

**2. Porque, sem responsabilidades formais, as decisões individuais se contradizem.** Sem
governança formal, cada gestor resolve os problemas isolados conforme eles aparecem, e essas ações
individuais podem ser **contraditórias entre si**. O artigo traz um caso concreto e didático:

> Em uma empresa global de transportes, o CIO foi instruído a cortar o orçamento corporativo de TI.
> Ele criou um sistema de *chargeback* para reduzir a demanda por serviços de TI. Insatisfeitos com
> as novas cobranças, os gestores das unidades de negócio passaram a **contratar especialistas
> técnicos próprios** por um preço que consideravam aceitável. Como essas contratações não
> apareciam no orçamento corporativo de TI, **parecia** que o CIO havia cumprido a meta — mas o
> gasto total da empresa com TI **aumentou** em vez de diminuir. Pior: as soluções locais criadas
> pelas unidades **comprometeram a integridade dos dados corporativos** e degradaram o atendimento
> aos clientes atendidos por mais de uma unidade de negócio.

Esse caso mostra que um mecanismo isolado (o chargeback), sem responsabilidades claras pelo
resultado final, produziu exatamente o contrário do que se queria.

**3. Porque a responsabilização clara é o que transforma a TI de fato.** O contraponto do artigo é
a **UNICEF**: quando a alta gestão percebeu que a TI tinha papel cada vez mais estratégico na missão
de entregar serviços a crianças, a equipe executiva **assumiu a responsabilidade** de garantir que a
TI atendesse aos objetivos organizacionais. Os diretores de divisão foram **responsabilizados pela
implantação dos sistemas globais** e o CIO foi **responsabilizado pela entrega dos serviços-chave de
infraestrutura**. O resultado é que a TI transformou a forma como a UNICEF opera, levando serviços de
TI a escritórios de campo remotos e melhorando fluxo de informação, transparência e comunicação.

Há ainda um quarto efeito, ilustrado pela **UPS**: quando as responsabilidades são claras e a
governança é **transparente**, todo mundo entende e segue os processos estabelecidos para propor,
implementar e usar TI — o que **limita o papel da política organizacional** nas decisões de TI.

---

### d) O que significa alinhamento entre TI e objetivos organizacionais?

Significa que **as ações e os comportamentos relacionados à TI — não só as grandes decisões, mas as
decisões do dia a dia tomadas por muita gente na organização — apontam na mesma direção das metas de
desempenho da organização**, e que existe alguém responsabilizado por cada um desses resultados. O
próprio artigo define governança de TI como *o processo pelo qual as empresas alinham as ações de TI
às suas metas de desempenho e atribuem responsabilidade por essas ações e seus resultados*.

Na prática, o alinhamento aparece em três níveis:

**1. Alinhamento de objetivo.** A organização precisa saber *para quê* quer a TI. O artigo mostra que
o desenho de governança dos melhores desempenhos **varia conforme o direcionador estratégico**:

| Direcionador estratégico | Métricas-chave | Governança predominante |
|---|---|---|
| **Lucro** (integração corporativa, foco em competências centrais) | ROI/ROE, custo dos processos de negócio | Mais **centralizada** — monarquias e federal |
| **Utilização de ativos** (compartilhamento e reúso) | ROA, custo unitário de TI | **Híbrida** — federal e duopólios |
| **Crescimento** (inovação e time-to-market nas unidades) | Crescimento de receita | Mais **descentralizada** — arranjos feudais, ênfase em gestão de risco |

Ou seja, não existe um "melhor modelo" universal: alinhar é **escolher o desenho de governança que
produz os comportamentos que aquela estratégia específica exige**.

**2. Alinhamento por processos (os *alignment processes*).** O artigo é claro ao dizer que governança
eficaz é tanto sobre **ações** quanto sobre decisões. Os processos de alinhamento são as técnicas de
gestão de TI que garantem envolvimento amplo na gestão e no uso eficaz da TI, tanto dando entrada nas
decisões quanto formalizando a execução delas. Os principais citados são:

- processo de proposta de investimento em TI;
- processo de exceção à arquitetura;
- acordos de nível de serviço (SLAs);
- chargeback;
- acompanhamento de projetos;
- **acompanhamento formal do valor de negócio gerado pela TI**.

**3. Alinhamento é via de mão dupla.** O caso do **ING DIRECT** mostra que o alinhamento não é a TI
correndo atrás da estratégia: o Conselho de TI e Operações reúne CIOs e COOs dos países, e o resultado
dessas reuniões **alimenta a reunião executiva onde a estratégia internacional é definida**. Dessa
forma, *as capacidades de TI influenciam a estratégia de negócio assim como a estratégia influencia a TI*.

Vale registrar também o trade-off central que o artigo coloca como primeiro passo do desenho:
**sinergia versus autonomia**. Alinhar exige decidir conscientemente quanto a organização quer ganhar
com padronização e compartilhamento (sinergia) e quanto quer preservar de liberdade das unidades
(autonomia) — e comunicar essa decisão para toda a organização.

---

### e) Quais são as cinco categorias de decisões de TI apresentadas por Weill e Ross?

As cinco decisões (os cinco **domínios de decisão**) são:

**1. Princípios de TI (*IT principles*)**
Decisões de alto nível sobre o **papel estratégico da TI no negócio**. Perguntas típicas: Qual é o
papel da TI no negócio? Como os princípios do negócio se traduzem em princípios de TI? Quais são os
comportamentos desejáveis em relação à TI? Como a TI será financiada?

**2. Arquitetura de TI (*IT architecture*)**
Um **conjunto integrado de escolhas técnicas** que orienta a organização no atendimento às
necessidades do negócio. Perguntas típicas: Quais são os processos de negócio centrais e como se
relacionam? Quais informações movem esses processos e como os dados devem ser integrados? Que
capacidades técnicas devem ser padronizadas em toda a organização? Que escolhas tecnológicas guiarão
as iniciativas de TI?

**3. Infraestrutura de TI (*IT infrastructure*)**
**Serviços de TI compartilhados e coordenados centralmente**, que formam a base da capacidade de TI da
organização e que **tipicamente são criados antes de se conhecerem as necessidades exatas de uso**.
Perguntas típicas: Quais serviços de infraestrutura são mais críticos para os objetivos estratégicos?
Quais devem valer para toda a organização e com quais níveis de serviço? Como esses serviços devem ser
precificados? Qual o plano para manter as tecnologias atualizadas? O que deve ser terceirizado?

**4. Necessidades de aplicações de negócio (*business application needs*)**
Os **requisitos de negócio** para aplicações compradas ou desenvolvidas internamente. Perguntas
típicas: Quais são as oportunidades de mercado e de processo para novas aplicações? Como atender a uma
necessidade de negócio dentro dos padrões de arquitetura — e quando uma necessidade justifica uma
exceção ao padrão? **Quem será o dono do resultado de cada projeto** e conduzirá as mudanças
organizacionais necessárias para garantir o valor?

**5. Priorização e investimento (*prioritization and investment*)**
Decisões sobre **quanto e onde investir em TI**, incluindo técnicas de aprovação e justificativa de
projetos. Perguntas típicas: Quais mudanças de processo são estrategicamente mais importantes? Como
está distribuído o portfólio atual de TI e ele é coerente com os objetivos estratégicos? Qual a
importância relativa dos investimentos corporativos frente aos das unidades de negócio? Qual o
equilíbrio certo entre projetos *top-down* e *bottom-up*, para balancear padronização e inovação?

#### A "governança em uma página"

Essas cinco decisões formam as **colunas** de uma matriz. As **linhas** são os seis **arquétipos de
tomada de decisão**, listados do mais centralizado para o menos centralizado:

1. **Monarquia de negócio** — um executivo sênior ou um grupo de executivos seniores, às vezes
   incluindo o CIO;
2. **Monarquia de TI** — executivos de TI, individualmente ou em grupo;
3. **Federal** — executivos de nível C e representantes de negócio de todos os grupos operacionais,
   podendo incluir a TI (equivale ao governo central e os estados trabalhando juntos);
4. **Duopólio de TI** — decisão a duas partes, envolvendo executivos de TI e um grupo de líderes de
   negócio;
5. **Feudal** — líderes de unidade de negócio ou de processo decidindo separadamente conforme as
   necessidades das suas áreas;
6. **Anarquia** — cada usuário individual ou pequeno grupo decidindo por conta própria.

Cruzando as 5 decisões com os 6 arquétipos, chega-se à **matriz 5x6** que dá nome ao artigo: a
"governança de TI em uma página". Ela permite **especificar, analisar e comunicar** onde cada decisão
de TI é tomada. É comum também separar, em cada célula, quem dá **entrada (input)** e quem de fato
**decide** — como no exemplo da Carlson Companies.

Exemplo da **UPS**: um subconjunto da alta direção responde por princípios e investimento (monarquia
de negócio); a equipe do CIO responde por arquitetura e infraestrutura (monarquia de TI); os líderes
de unidade e quatro gestores de processos corporativos respondem pelas necessidades de aplicações
(feudal). Um arranjo claro e relativamente centralizado.

---

### f) Por que não basta simplesmente criar um comitê de TI para que exista Governança de TI?

Porque **um comitê é apenas um mecanismo**, e governança é um **sistema coordenado** de mecanismos
ancorado num desenho consciente de direitos de decisão e responsabilidades. O artigo é explícito:
para ser eficaz, a governança de TI **deve ser ativamente desenhada, e não o resultado de mecanismos
isolados** (comitê diretivo, escritório de arquitetura de TI, acordos de nível de serviço)
implementados em momentos diferentes para responder ao desafio do momento.

Os motivos, em detalhe:

**1. Um comitê sozinho não responde às perguntas essenciais.** Criar um comitê não define, por si só,
quem decide princípios, arquitetura, infraestrutura, aplicações e investimento, nem quem **responde**
pelos resultados de cada um desses domínios. Sem preencher a matriz, o comitê vira mais um fórum de
discussão sem accountability.

**2. São necessários três tipos de mecanismos, não um.** O artigo diz que as organizações desenham
**três tipos** de mecanismos de governança, e todos precisam existir e estar coordenados:

- **Estruturas de tomada de decisão** — os comitês e papéis organizacionais que alocam as
  responsabilidades de decisão conforme os arquétipos pretendidos. *(É aqui, e só aqui, que o comitê
  de TI se encaixa.)*
- **Processos de alinhamento** — as técnicas que garantem envolvimento amplo: processo de proposta de
  investimento, processo de exceção à arquitetura, SLAs, chargeback, acompanhamento de projetos e
  acompanhamento formal do valor de negócio gerado pela TI.
- **Comunicações formais** — os meios de "espalhar a palavra" sobre as decisões, os processos e os
  comportamentos desejáveis: anúncios da alta gestão, comitês formais, escritório do CIO ou de
  governança de TI, portais web e até o trabalho individual com quem não adere. O artigo registra que
  **quanto mais a gestão comunicava formalmente a existência dos mecanismos, mais eficaz era a
  governança**.

O exemplo da **UPS** ilustra bem: não foi *um* comitê, foram **quatro mecanismos coordenados** —
(a) um comitê diretivo de TI com quatro altos executivos, responsável por princípios e investimento;
(b) um comitê de governança de TI com executivos seniores de TI, responsável pelas decisões-chave de
arquitetura; (c) um processo formal de *charter*, que filtra todas as propostas de projeto de TI da
organização e mantém só as mais alinhadas aos objetivos estratégicos; e (d) um **processo de
escalonamento** para tratar exceções aos padrões de arquitetura no nível organizacional adequado.

**3. Mecanismo isolado pode produzir o efeito contrário.** É exatamente a lição do caso da empresa de
transportes descrito no item (c): existia um mecanismo (o chargeback), mas sem um desenho coerente de
responsabilidades ele gerou gasto total maior, perda de integridade dos dados e piora no atendimento.

**4. Um comitê não garante que as pessoas saibam que ele existe.** Se só 38% dos gestores seniores
sabem como a TI é governada, e esse conhecimento é o melhor preditor de eficácia, então **comunicar**
é parte constitutiva da governança, não um detalhe posterior. Uma grande barreira à governança eficaz
é justamente a falta de entendimento sobre como as decisões são tomadas.

**5. O comitê precisa ser o certo para aquela organização.** Como não existe um único melhor modelo, o
desenho eficaz depende dos **objetivos estratégicos** e da **estrutura organizacional** da empresa. Um
comitê centralizado imposto a uma organização que compete por crescimento e inovação local pode
sufocar exatamente o comportamento que ela precisa incentivar.

**6. A governança é aprendizado e precisa ser revista — mas não o tempo todo.** O caso da **Dow
Corning** mostra que o comitê executivo se reuniu regularmente por vários anos para redefinir o papel
da TI, articular o papel do CIO, estabelecer princípios de arquitetura e gerir prioridades de
investimento; só **depois** que a TI se consolidou como função-chave é que a responsabilidade foi
passada a um subconjunto menor do comitê executivo. Ou seja, o formato do comitê acompanhou a
maturidade. E o artigo observa que empresas com governança eficaz mudavam algum aspecto da governança
cerca de **uma vez por ano**, enquanto as de governança menos eficaz mudavam **até três vezes por ano**
— trocar de comitê à toa é sintoma de problema, não solução.

#### Os quatro passos recomendados pelos autores

Para fechar: em vez de "criar um comitê", o artigo recomenda desenhar a governança em quatro passos:

1. **Identificar as necessidades de sinergia e autonomia** da organização, avaliando de forma realista
   tanto os benefícios quanto os custos das sinergias;
2. **Estabelecer o papel da estrutura organizacional** — declarar primeiro a estrutura, reconhecendo
   suas limitações e sua instabilidade;
3. **Identificar os comportamentos desejáveis relacionados à TI que ficam fora do alcance da
   estrutura** — são esses que os mecanismos de governança precisam induzir, evitando reestruturações
   a cada mudança de prioridade;
4. **Desenhar conscientemente a governança de TI em uma página** — primeiro os arranjos (a matriz),
   depois os mecanismos que vão implementá-los.

> *"Governança de TI eficaz não acontece acidentalmente."* — Weill & Ross (2004)
