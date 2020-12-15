# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np

# Questão 2
RA = 11201721076
R1,R2,R3,R4 = 1,72,10,76

DCTY = [[352,-R1],[-R2,-10]]
DCTCb= [[265, R3],[ R1,  5]]
DCTCr= [[271,-R4],[-R4, R2]]

DCTY = np.array(DCTY )
DCTCb= np.array(DCTCb)
DCTCr= np.array(DCTCr)

print(DCTY )
print(DCTCb)
print(DCTCr)


# %%
# a) (1,0) Obtenha a inversa DCT das componentes Y, Cb e Cr, através da forma matricial, sendo que para isso deverá ser mostrada a matriz de transformação (2x2).

# Definindo funções para a a dct 2d inversa
def C(w,k):
    if w == 0:
        return (1/k)**(1/2)
    return (2/k)**(1/2)

def summation2(dctBlock,x,y):
    res = 0
    h,w = dctBlock.shape
    for u in range(w):
        for v in range(h):
            res_temp = C(u,w)*C(v,h)*dctBlock[u,v]
            res_temp*= np.cos(((2*x+1)*u*np.pi)/(2*w))* np.cos(((2*y+1)*v*np.pi)/(2*h))
            res+= res_temp
    return res

def dct_inv(dctBlock):
    dctBlock = np.float32(dctBlock)
    dctInvBlock = np.zeros(dctBlock.shape)
    h,w = dctBlock.shape
    for x in range(w):
        for y in range(h):
            dctInvBlock[x,y] = summation2(dctBlock,x,y)
    return np.float32(dctInvBlock)

# Aplicando DCT inversa
DCTY_inv = dct_inv(DCTY )
DCTCb_inv= dct_inv(DCTCb)
DCTCr_inv= dct_inv(DCTCr)

print("Resultados das DCTs Inversas")
print("DCTY_inv \n",DCTY_inv )
print("DCTCb_inv\n",DCTCb_inv)
print("DCTCr_inv\n",DCTCr_inv)

# Encontrando matriz de transformação
def getTmatrix(A,B):
    A_inv = np.linalg.inv(A)
    X = np.matmul(A_inv,B)
    return X

TY = getTmatrix(DCTY,DCTY_inv)
TCb= getTmatrix(DCTCb,DCTCb_inv)
TCr= getTmatrix(DCTCr,DCTCr_inv)

print("\nMatrizes de Transformação")
print("TY \n",TY )
print("TCb\n",TCb)
print("TCr\n",TCr)

print("\nTeste de Sanidade - Multiplicando DCTY por TY")
print("np.matmul(DCTY,TY)=\n",np.matmul(DCTY,TY))


# %%
# b) (1,0) Faça a transformação para o espaço RGB, para todos os quatro pixels:  pixel(1,1)/ pixel (1,2)/ pixel (2,1)/ pixel (2,2).

def YCbCr2RGB(Y,Cb,Cr):
    Y = np.array(Y)
    Cb = np.array(Cb)
    Cr = np.array(Cr)

    R = 1.164*(Y-16)+1.596*(Cr-128)
    G = 1.164*(Y-16)-0.813*(Cr-128)-0.392*(Cb-128)
    B = 1.164*(Y-16)+2.017*(Cb-128)
    RGB = np.stack([R,G,B])
    return RGB
RGB = YCbCr2RGB(DCTY_inv,DCTCb_inv,DCTCr_inv)
print("RGB\n",RGB)


# %%
# c) (0,5) Converta este pixel obtido para o espaço XYZ e xyz. Obs.: não é necessário fazer a correção gamma.

def RGB2XYZ(RGB):
    X = 0.4125*RGB[0,:,:]+0.3576*RGB[1,:,:]+0.1804*RGB[2,:,:]
    Y = 0.2127*RGB[0,:,:]+0.7152*RGB[1,:,:]+0.0722*RGB[2,:,:]
    Z = 0.0193*RGB[0,:,:]+0.1192*RGB[1,:,:]+0.9503*RGB[2,:,:]
    return np.stack([X,Y,Z])

XYZ = RGB2XYZ(RGB)
print("XYZ\n",XYZ)


