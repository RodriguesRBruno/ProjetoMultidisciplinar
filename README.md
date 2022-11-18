# Projeto Interdisciplinar: Machine Learning na Detecção de Fake News

![](https://github.com/camilasp/ProjetoMultidisciplinar/blob/dev/images/banner.png)


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
<p>Os dados foram salvos em um bucket na AWS S3, sendo pré-processados e tratados em notebooks no Sagemaker. Com os dados limpos, foi feita uma análise com visualização dos dados e por fim, os textos foram vetorizados para que pudessem ser utilizados em modelos de machine learning.</p>
<p>Foram treinados modelos para os dois datasets separadamente afim de realizar uma avaliação. Como as bases isoladamente produziram modelos ruins, elas foram unificadas, aumentando assim a variedade de notícias. Os modelos unificados produziram resultados melhores.</p>
<p> O melhor modelo foi o XXXX que obteve uma precisão de XXXX.</p>


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
<p> Os dados utilizados no treinamento e validação dos modelos desenvolvidos são corpus desenvolvidos em Língua Portuguesa já categorizados como noticía verdadeira ou falsa. Os dados estavam em repositórios dos projetos de que fazem parte - descrito abaixo - em arquivos do tipo csv e txt. Os dados foram obtidos das seguintes fontes:</p>

* Fake.Br: trata-se de uma base de dados com 7200 notícias coletadas em 2018 de diferentes agências de notícias, na proporção de 1 notícia fake para 1 verdadeira. As notícias foram coletadas de forma semi-automática com uso de web crawlers, sendo analisadas e categorizadas pelos participantes do projeto. Mais informações podem ser encontradas [aqui](https://github.com/roneysco/Fake.br-Corpus) e [aqui](https://sites.icmc.usp.br/taspardo/OpenCor2018-SantosEtAl.pdf).
* FakeRecogna: trata-se de uma base com 11,902 amostras de notícias, sendo a maior parte dos anos de 2020 e 2021, sendo que as notícias verdadeiras foram retiradas de sites de agências de notícias renomadas e as fake news foram colhidas de sites de agências de chegagem de fake news brasileiras, na proporção de 1 para 1. As notícias são de assuntos diversos, dentre os quais destacam-se entretenimento, saúde e política.
Mais informações podem ser obtidas no repositório do [projeto](https://github.com/Gabriel-Lino-Garcia/FakeRecogna).


<p>Apesar de haver outras informações nas bases, como nome de autor, título, etc. as informações utilizadas na construção desse projeto foram apenas o texto da notícia e a classificação da notícia em verdadeira ou falsa. Posteriormente, o grupo criou novas features baseadas nos textos, como o número de palavras do texto, por exemplo.</p>

<a name="infra"></a>
## Arquitetura e Infraestrutura de Dados

Foi feito o upload dos dados para um bucket da Amazon S3. Os arquivos em txt de uma das bases foram processados em um notebook no Amazon Sagemaker e salvos em formato csv. Após esse tratamento, os csvs de ambas as bases foram preparados para visualização de dados e modelagem em outro notebook no sagemaker e salvos em um bucket de dados pré-processados. Utilizando os dados pré-processados, foi realizada uma análise de dados e a modelagem, em notebooks separados no Sagemaker. Os modelos treinados foram salvos em um terceiro bucket. Os códigos feitos nos notebooks no sagemaker foram disponibilizados no github.

### Diagrama da Arquitetura de dados:

![](https://github.com/camilasp/ProjetoMultidisciplinar/blob/dev/images/diagrama_arquitetura.png)

<a name="prep"></a>
## Preparação dos dados

As bases não apresentavam dados nulos ou faltantes e a preparação dos dados consistiu no processamento dos textos, incluindo a exclusão de pontuação, acentuação, exclusão de stopwords e lemmatização. Para permitir o uso por algoritmos de machine learning, os textos foram vetorizados utilizando o TfidfVectorizer.

A preparação dos dados pode ser vista em detalhes neste [notebook](https://github.com/RodriguesRBruno/ProjetoMultidisciplinar/blob/main/preprocessing.ipynb).


<a name="eda"></a>
## Análise Exploratória

Os dados das bases Fake.Br e FakeRecogna foram explorados separadamente para que pudéssemos entender melhor as diferenças entre os assuntos tratados em uma base e outra, o que era esperado, devido a diferença temporal. A análise exploratória completa pode ser vista nesse [notebook](https://github.com/RodriguesRBruno/ProjetoMultidisciplinar/blob/main/visualizations.ipynb). 

Abaixo, as nuvens de palavras de cada um dos datasets. Pode-se notar a variação nos assuntos principais.

![](https://github.com/camilasp/ProjetoMultidisciplinar/blob/main/images/nuvens_de_palavras.png)

<a name="model"></a>
## Modelagem e Validação

Usamos como modelo base o XGBoost do Sagemaker.Primeiro, utilizamos os datasets separadamente para treinar dois modelos, usando como teste um dataset de testes da base treinada e também um dataset de teste da outra base. Quando testamos amostras de uma base no modelo treinado com amostras da outra base, os resultados não foram bons, enquanto que nos testes feitos com amostras das próprias bases, em cada caso, os resultados eram excelentes. A principal razão para isso é a diferença no conteúdo das bases, que apresentam notícias de períodos diferentes, sendo uma mais recente e mais abrangente.  

Usamos então o XGBoost para treinar outro modelo, agora com todos os dados e os resultados obtidos foram muito bons. Aparentemente, o modelo conseguiu generalizar melhor.

Foram treinados então outros modelos...
* falta treinar outros modelos
* falta a parte de validação cruzada/gridsearch

Os notebooks com os modelos estão nos links abaixo:

<a name="conclusao"></a>
## Conclusão

Para garantir que o modelo está generalizando bem seria importante testar a classificação de notícias ainda mais recentes e verificar o desempenho das métricas novamente.

<a name="ref"></a>
## Referências

* Fake News database Fake.Br from the [Fake.br-Corpus repository](https://github.com/roneysco/Fake.br-Corpus)

* Fake Recogna database from the [FakeRecogna repository](https://github.com/Gabriel-Lino-Garcia/FakeRecogna)

* [O perigo das fake news]( https://www.tjpr.jus.br/noticias-2-vice/-/asset_publisher/sTrhoYRKnlQe/content/o-perigo-das-fake-news/14797?inheritRedirect=false)

* Monteiro R.A., Santos R.L.S., Pardo T.A.S., de Almeida T.A., Ruiz E.E.S., Vale O.A. (2018) Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results. In: Villavicencio A. et al. (eds) Computational Processing of the Portuguese Language. PROPOR 2018. Lecture Notes in Computer Science, vol 11122. Springer, Cham 

* Silva, Renato M., Santos R.L.S, Almeida T.A, and Pardo T.A.S. (2020) "Towards Automatically Filtering Fake News in Portuguese." Expert Systems with Applications, vol 146, p. 113199.

* [Banner Photo]( https://www.pexels.com/photo/white-and-black-letter-blocks-3989901/) by Joshua Miranda

* [Documentação do modelo built-in XGBoost]( https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html ) by AWS

* [Documentação do modelo built-in Linear Learner]( https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html ) by AWS

* [Documentação do modelo built-in Factorization Machines]( https://docs.aws.amazon.com/sagemaker/latest/dg/fact-machines.html ) by AWS
