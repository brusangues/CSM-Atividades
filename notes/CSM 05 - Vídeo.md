# Acuidade visual
* Acuidade Visual
    * Muitos animais possuem visão com resolução muito melhor q os humanos
    * A acuidade é uma função de modulação
* Resolução retina
    * Sistema com resolução retina é aquele que atinge o limiar da acuidade humana
* Razão de tiro do projetor
# Codificação de Vídeo
* Taxa de quadros na transmissão de televisão
* Codificação (compressão)
    * Qualquer banda é estreita
* Source Coding
* Compressão de vídeo
# Componentes da Codificação de Video
* Componentes da Codificação de video
    * COdificação por entropia é sem perdas
* Predição
    * Intra - dentro do quadro
    * Inter - no tempo
    * MPEG
    * Funcionamento
        * Existe um preditor no codificador
        * O erro entre o sinal e a saída do preditor é quantizado
        * O mesmo preditor está no receptor, e apenas o erro é transmitido
    * Intra frame prediction
        * Varrendo as linhas
        * Matriz
        * Planar
    * Motion Compensated prediction
        * Inter frame
        * É enviado um frame inicial. Depois,
        * É enviado o erro da predição e um vetor de movimento
* Transformada
    * dct e dwt
    * DWT - JPEG2000 MPEG7
    * *acuidade não tem a ver com movimento.
* Quantização
    * Vetorial - em blocos
    * Codificação por entropia
        * É utilizada para protejer informações do cabeçalho
        * Huffman e Codificação Aritmética
* Quantização Escalar
    * Exemplo: arredondamento
    * Mapeamento: divide o intervalo de valores que a fonte gera
    * Cada intervalo é então mapeado para uma palavra-código
    * Em muitos casos é um mapeamento irreversível.
    * (... sleepy)
    * Compressão de imagem
        * 2bits/pixel - 1bit/pixel
* Quantização Vetorial
    * Com perdas. Mais perdas que a escalar
    * No passado era inviável, mas um algoritmo tornou possível
    * Centróides
        * Regiôes do espaço com um centroide no centro
        * Regiões de voronori 
    * Termos técnicos
        * Codebook = segredo
        * Codeword -> Codevector = elemento do código
        * Codeindex
        * (...sleepy)
    * VQ para compressão de imagem
        * Cada bloco de uma imagem é representado pror uma codeword
        * Métrica para proximidade dos vetores: Distância euclidiana
    * K-Means
    * (...)