# Data-augmentation-using-Python-Keras
Data Augmentation é uma técnica para gerar novos exemplares de dados de treinamento a fim de aumentar a generalidade do modelo.

Basicamente, toda modificação feita em um algoritmo com a intenção de reduzir o erro de generalização (mas não o erro de treinamento) é uma técnica de regularização (Goodfellow et al). Bom, a técnica de data augmentation se encaixa exatamente nesse perfil.

Aplicando essa técnica, veremos a nossa precisão no treinamento piorar, porém a precisão sobre o dataset de teste vai melhorar: o modelo CNN se tornará mais genérico.

## Como que é possível, usando uma imagem, gerar outras?

São muitas maneiras possíveis, mas os métodos mais comuns são aplicando combinações de operações sobre a imagem original, como:

Translação;

Rotação;

Modificação a perspectiva;

Achatamento e alongamento;

Distorção de Lentes.



## Data augmentation usando Python + Keras
A biblioteca keras possui uma classe que facilita muito o nosso trabalho na hora de gerar novas imagens para alimentar o modelo.

Vamos supor que eu quisesse treinar uma CNN para classificar aviões militares, dentre elas o T-27 Tucano – aeronave que tive o privilégio de voar e dar instrução na Academia da Força Aérea (AFA) por 4 anos.



### Fonte: https://sigmoidal.ai/reduzindo-overfitting-com-data-augmentation/
As Linhas 9 e 10 especificam o caminho do arquivo de entrada (imagem do T-27) e o diretório onde as 10 imagens geradas devem ser salvas.

Após carregar a imagem e transformá-la em um array, é acrescentada uma nova dimensão a este array (Linha 17). Esse procedimento para muita coisa relacionada a CNN. Se a dimensão extra não for incluída, o código vai dar ValueError na execução.

Na Linha 21, é criado um objeto ImageDataGenerator, onde especificamos os valores máximos para o range (em graus) no qual a imagem pode rotacionar, os deslocamentos laterais e verticais (porcentagem em relação à imagem toda), quantidade de zoom e se a imagem pode ser espelhada em relação ao eixo y (horizontal flip).

Na sequência (Linha 24), é criado um generator com os argumentos relacionados à imagem de origem, diretório de output, formato do arquivo e prefixo (nome) das imagens a serem geradas.

O próximo passo para gerar 10 novas imagens é chamar a variável imgGen por 10 vezes, dentro do loop. Como a variável aponta para o generator imgAug.flow, a cada nova chamada um novo arquivo é criado.
