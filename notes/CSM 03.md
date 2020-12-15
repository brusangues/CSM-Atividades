# Introdução à Codificação de Imagem
* *instalar blender 2.8
## Codificação Visual
* Processamento para armazenamento das imagens na memória de longo prazo
    * Sentido da audição geralmente é fundido com as imagens
    * Codificação é predominantemente feita durante ao sono
* Redundância de Informações nas imagens
    * Fóvea já realiza uma grande redução na quantidade de informação
    * Abordagem geral da codificação: redução da redundância
## Reduzindo a Redundância de pixels
* Teoria da Informação
    * H(x) é uma medida de quanta informação em média é necessária para descrever a variável aleatória x
* Técnicas de codificação
    * Sem perdas
        * Qualidade permanece intacta
    * Com perdas
        * Atingem proporção de compressão muito elevada
        * Podem introduzir artefatos de compressão
## Sub-amostragem no espaço de cores
* Correção Gamma
    * Filmadoras analógicas
        * Correção de fatiamento de imagens
        * Correção da luminosidade/saturação em alguns pontos da imagem
    * $$Vout = Vin \up{\gamma}$$
    * A maioria dos arquivos de imagem usa uma gama de 1/2.2
    * Função: adaptar analógico-digital
    * Geralmente representado com ' (linha)
* Espaço de Luminância e Crominância
    * Podemos perder mais informação de cor do que de brilho
        * Discernimento das bordas já é possível com tons de cinza
    * YUV(PAL) YIQ(NTSC) - Para analógicos
        * Y = luma, composto por uma multiplicação dos canais de cor
        * PAL M - brasil
        * Senos e cossenos
    *YCbCr - Sistema digital
* Sub-Amostragem de Crominância
    * Após a transformação, o compontente de luminância é deixado em resolução total
    * Redução de CbCr pode ser feita desigualmente entre Cb e Cr, além de horizontalmente e verticalmente
    * Y :Cb:Cr
    * 4 :4 :4 ; 4:2:2 ; 4:2:0
    * JPEG
## Codificações por Transformadas
* Codificações por Transformadas
    * Sinal é mapeado a partir de um domínio, espacial ou temporal, para o domínio da transformada
    * Um sinal pode ser uni ou multidimensional (fotos são bidimensionais)
    * Transformadas ortogonais são mais usandas pois o mapeamento é único e reversivo
    * Energia é preservada no domínio da transformada
    * As principais transformadas discretassão DCT e DWT
* Vantagem da Ortogonalidade
    * C uma matriz
    * demonstração da codificação e decodificação que são sem perdas
* Codificador Estruturado Típico
    * Transform (sem perdas) -> Quantizer (perdas) -> Encoder (sem perdas)-> (bit stream)
    * Inverse Tr <- Dequantizer(perdas) <- Decoder
* Codificação por DCT - Transf Discreta de Cosseno
    * Por blocos lxl (8x8 é o mais utilizado)
    * Quantizador -> buffer -> 
    * Encoder = Scramble, embaralhamento - robustez ao ruído
    * Dos coeficientes do DCT, apenas os de baixa frequência são mantidos
        * Sinais de alta frequência significam informações pequenas
    * A DCT precisa de técnicas complementares para compressão, como Quantização, Classificação, codificação de linha (VLC,RLC), sub-amostragem de crominância, etc
* Definindo a DCT 1D
    * C(0) = valor médio
* *KLT é a transformada ótima porém não possui algoritmo rápido
* JPEG - DCT 2D
    * Bloco 8x8 -> DCT -> Q(Quantization Table) -> DPCM para frequências baixas para robustez ->...
    * Funções base DCT -> Discretização -> Padrões Base
* Separabilidade
    * Pode-se fazer o processamento das linhas primeiro, ou contrário
* Características dos coeficientes dct
* Resumo da DCT
    * Coeficientes de baixa freq tem maior magnitude
    * Alta freq tem menor amplitude
    * A maior parte das informações são compactadas nos coeficientes de maior energia
    * DCT prevê compactação de energia
* Exercício de casa
    * 2 matrizes
    * Calcular F e G usando a definição de DCT2D
* Exemplo
## Quantização dos Coeficientes DCT
* Tabela de coeficientes da DCT
* DPCM
    * Diferença entre frame anterior para robustez do stream
# Introdução à Animação
* Percepção visual de acordo com o tempo
* Persistência da visão pode causar efeito de continuidade
* Frame Rate
    * Frequência de quadros
* Keyframes
    * Quadros importantes para perceber o movimento
    * Tweening - Interpolação
* GPU faz a interpolação dos Keyframes dados pela CPU
    * Quatérnios e interpolação linear
* Principais métodos de animação
    * Tradicional
    * 2d baseada em vetores
    * 3d por computação gráfica
* Renderizar
    * Completar elementos que a luz agiria