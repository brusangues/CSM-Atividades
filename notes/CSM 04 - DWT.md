# Introdução à transformada Wavelet Discreta (DWT) em codificação visual
* Modelo geral de codificação de fonte
* Modelo de codificação com transformada wavelet
* Revisão
    * Fourier
        * $$ F(\omega) = \int_{-\inf}^{\inf} f(t)e^{j\omega t} dt $$
        * Perdemos informações temporais
        * Opção para termos informação temporal: STFT
    * STFT
        * Ao aumentar a resolução do tempo, a frequência aumenta também, e vice versa
    * Fourier utiliza função sync
* Transformada Wavelet
    * Generalização para usar outras funções
    * Fourier gera frequência. Na wavelet vai depender da função
* CWT
    * Multi-resolução
    * em frequências diferentes
    * Análise com resolução variável
* Janelas Gaussianas para S-Transform
    * Para transformar função qualquer em wavelet?(?)
* DWT
    * Vantagem sobre a CWT: reduz complexidade computacional
    * a e b são parâmetros discretos
    * a = escala; b = ponto de análise
* Codificação em Subband. 2 bandas:
    * Banda alta e baixa
    * Sinal inicial dividido em 2 -> divisão por 2 em ambas as bandas para equalizar -> decodificação
* Para filtros com coeficientes reais, as soluções para a reconstrução perfeita...
* Compressão por WT
    * Wavelet de Haar
        * g(n) = 1/2 para n=-1,0
        * h(0) = 1/2, h(-1)=-1/2
        * mais antiga e simples
* Transformada de Haar
    * Separação Horizontal e Vertical
    * Diagonais são codificadas com menos energia
* Exemplo
    * (...)
* Banco de Filtros
    * (...)
* FWT-2d - só com a Haar
* Características DWT 2D
    * DWT é aplicada independentemente e descorrelaciona a imagem (tamanhos de escala), preservando a correlação espacial.
    * DWT-1D = filtro passa-baixa (L) + passa-alta (H)
    * Divide uma linha de pixels em duas sub-bandas,
    * Cada banda contém metade do tamanho original da linha após downsampling.
    * A aplicação dos filtros a imagens bidimensionais gera 4 sub-bandas (LL, LH, HL e HH)
    * sub-banda LL é imagem original com menos resol., com os detalhes filtrados nas outras sub-bandas.
    * Bordas horizontal (LH), vertical (HL) e diagonal (HH) no tamanho da escala definido pela wavelet. 