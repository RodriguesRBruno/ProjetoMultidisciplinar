# Projeto Interdisciplinar: Machine Learning na Detecção de Fake News


##  Conteúdo:

   * [Resumo](#resumo)
   * [Introdução](#intro)
   * [Objetivo](#objetivo)
   * [Dados](#dados)
   * [Arquitetura e Infraestrutura de Dados](#infra)
   * [Preparação dos dados](#prep)
   * [Análise Exploratória](#eda)
   * [Modelagem e Validação](#model)   
   * [Conclusão](#conclusao)
   * [Referências](#ref)

 
<a name="resumo"></a>
## Resumo 
<p>Trata-se do projeto interdisciplinar desenvolvido por alunos do 2º semestre do curso de Especialização em Ciência de Dados do Instituto Federal de São Paulo. O trabalho engloba os conceitos estudados na disciplina de Aprendizagem de Máquina e Reconhecimento de Padrões e na disciplina Tecnologias de Big Data. O objetivo do trabalho é praticar, utilizando uma base de dados, a aplicação de conceitos de aprendizagem de máquina na resolução de um problema, com processamento de algoritmos de Machine Learning em ambiente distribuído na AWS.</p>
<p>O tema da base de dados escolhido pelo grupo foi Fake News, por se tratar de um problema atual, relevante e que demanda soluções, tendo em vista os problemas já causados pela disseminação de  informações falsas. Foram escolhidas bases de dados contendo notícias previamente categorizadas como falsas ou verdadeiras com o objetivo de criar uma solução de classificação automatizada dessas notícias, acelerando a detecção das fake news.</p>

<h2> Falta incluir também info resumida da infra usada, algoritmos testados e resultados</h2>

<a name="intro"></a>
## Introdução 

<p>Com o advento da internet, tornou-se possível obter informações não apenas através de jornais, telejornais e rádios, que eram antes os principais fornecedores de notícias. Podemos dizer que tanto o acesso quanto o compartilhamento de informações se tornou muito mais democrático, dando voz àqueles que antes não tinham espaço para compartilhar suas ideologias. Entretanto, essa imensa quantidade de informações disponíveis traz também um grande desafio: como separar fato de opinião e mais importante ainda, como separar uma notícia verdadeira de uma notícia falsa, a chamada fake news?</p>
<p>Em 2018, o Instituto Mundial de Pesquisa (IPSO) divulgou um estudo intitulado: “Fake news, filter bubbles, post-truth and trust (Notícias falsas, filtro de bolhas, pós-verdade e verdade)”, que revela dados importantes. De acordo com o levantamento, 62% dos entrevistados do Brasil admitiram ter acreditado em notícias falsas, valor acima da média mundial que é de 48%. Apesar de parecerem inofensivas para alguns, as fake news são potencialmente perigosas. No Brasil, em 2014, a disseminação de uma fake news provou uma verdadeira tragédia.  Na ocasião, uma mulher foi linchada até a morte por moradores da cidade de Guarujá, em São Paulo. Fabiane Maria de Jesus tinha 33 anos, era dona de casa, casada, mãe de duas crianças, e foi confundida com uma suposta sequestradora de crianças, cujo retrato falado, que havia sido feito dois anos antes, estava circulando nas redes sociais. E este é apenas um exemplo dos danos que podem ser causados por informações falsas. No âmbito da saúde, por exemplo, a desinformação têm levado muitas pessoas a duvidar da segurança de vacinas, ocasionando o aumento de casos de doenças que estavam controladas devido aos baixos níveis de vacinação da população.</p>
<p>Levando em consideração esse cenário, surgiram as agências de checagem, que têm por objetivo avaliar o conteúdo postado em diferentes meios de comunicação e informar ao público se a informação veículada é verdadeira.</p>
<p>Dado o grande volume de dados, algoritmos de machine learning são ferramentas que podem acelerar e contribuir na análise dessa massa de informações, podendo ser usada não só por agências de checagem, mas pelos próprios meios de comunicação, por partidos políticos, entre outros, afim de se descobrir informações falsas divulgadas nas redes.</p>

<a name="objetivo"></a>
## Objetivo 

<p> O trabalho realizado propõe a criação de um modelo de machine learning que classifica notícias, objetivando sobretudo destacar o que é conteúdo falso. </p>

<a name="dados"></a>
## Dados 
<p> Os dados utilizados no treinamento e validação dos modelos desenvolvidos são corpus desenvolvidos em Língua Portuguesa já categorizados como noticía verdadeira ou falsa. Os dados foram obtidos das seguintes fontes:</p>

* FakeRecogna: trata-se de uma base com 11,902 amostras de notícias, sendo que as notícias verdadeiras foram retiradas de sites de agências de notícias renomadas e as fake news foram colhidas de sites de agências de chegagem de fake news brasileiras, na proporção de 1 para 1. As notícias são de assuntos diversos, dentre os quais destacam-se entretenimento, saúde e política.
Mais informações podem ser obtidas no repositório do [projeto](https://github.com/Gabriel-Lino-Garcia/FakeRecogna).
* Fake.Br: trata-se de uma base de dados com 7200 notícias coletadas de diferenetes agências de notícias, na proporção de 1 notícia fake para 1 verdadeira. As notícias foram coletadas de forma semi-automática com uso de web crawlers, sendo analisadas e categorizadas pelos participantes do projeto. Mais informações podem ser encontradas [aqui](https://github.com/roneysco/Fake.br-Corpus) e [aqui](https://sites.icmc.usp.br/taspardo/OpenCor2018-SantosEtAl.pdf).

<p>Apesar de haver outras informações nas bases, como nome de autor, título, etc. as informações utilizadas na construção desse projeto foram apenas o texto da notícia e a classificação da notícia em verdadeira ou falsa. Posteriormente, o grupo criou novas features baseadas nos textos, como o número de palavras do texto, por exemplo.</p>

<a name="infra"></a>
## Arquitetura e Infraestrutura de Dados

<h2>Incluir explicação do esquema na aws e o diagrama da solução</h2>

<a name="prep"></a>
## Preparação dos dados

As bases não apresentavam dados nulos ou faltantes e a preparação dos dados consistiu no processamento dos textos, incluindo a exclusão de pontuação, acentuação, exclusão de stopwords e lemmatização. Para permitir o uso por algoritmos de machine learning, os textos foram vetorizados utilizando o TfidfVectorizer.

A preparação dos dados pode ser vista em detalhes neste [notebook](https://github.com/RodriguesRBruno/ProjetoMultidisciplinar/blob/main/preprocessing.ipynb).


<a name="eda"></a>
## Análise Exploratória

<a name="model"></a>
## Modelagem e Validação

<a name="conclusao"></a>
## Conclusão

<a name="ref"></a>
## Referências

* Fake News database Fake.Br from the [Fake.br-Corpus repository](https://github.com/roneysco/Fake.br-Corpus)

* Fake Recogna database from the [FakeRecogna repository](https://github.com/Gabriel-Lino-Garcia/FakeRecogna)

* [O perigo das fake news]( https://www.tjpr.jus.br/noticias-2-vice/-/asset_publisher/sTrhoYRKnlQe/content/o-perigo-das-fake-news/14797?inheritRedirect=false)

* Monteiro R.A., Santos R.L.S., Pardo T.A.S., de Almeida T.A., Ruiz E.E.S., Vale O.A. (2018) Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results. In: Villavicencio A. et al. (eds) Computational Processing of the Portuguese Language. PROPOR 2018. Lecture Notes in Computer Science, vol 11122. Springer, Cham 

* Silva, Renato M., Santos R.L.S, Almeida T.A, and Pardo T.A.S. (2020) "Towards Automatically Filtering Fake News in Portuguese." Expert Systems with Applications, vol 146, p. 113199.

* 
[Banner Photo]( https://www.pexels.com/photo/white-and-black-letter-blocks-3989901/) by Joshua Miranda
