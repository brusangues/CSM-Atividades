# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np

# Questão 1
RA = 11201721076
R1,R2,R3,R4 = 1,72,10,76
A = [[01.4,72.5],[10.9,76.7]]
A = np.array(A)


# %%
# a) (1,5) Calcule a DCT-2D através da equação de definição 2D, conforme a lista 1 de exercícios no Tidia4. Obs. Utilize duas casas decimais.

# Definindo funções para a a dct 2d
def C(w,k):
    if w == 0:
        return (1/k)**(1/2)
    return (2/k)**(1/2)

def summation1(block,u,v):
    h,w = block.shape
    res = 0
    for x in range(w):
        for y in range(h):
            res+= block[x,y]* np.cos(((2*x+1)*u*np.pi)/(2*w))* np.cos(((2*y+1)*v*np.pi)/(2*h))
    return res

def F(block,u,v):
    h,w = block.shape
    return C(u,w)*C(v,h)*summation1(block,u,v)

def dct(block):
    block = np.float32(block)
    dctBlock = np.zeros(block.shape)
    h,w = block.shape
    for u in range(w):
        for v in range(h):
            dctBlock[u,v] = F(block,u,v)
    return np.float32(dctBlock) 

A_dct = dct(A)
A_dct = np.round(A_dct,2)

# Print
print("A")
print(A)

print("\nA_dct")
print(A_dct)


# %%
# b) (0,5) Com o valor obtido no item anterior, faça o arredondamento simples para um número inteiro (como a função round(.)), e calcule o erro quadrático médio da DCT deste bloco.
A_dct_round = np.round(A_dct)
print("A_dct_round")
print(A_dct_round)

def MSE(a,b):
    h,w = a.shape
    c = np.subtract(a,b)
    c = np.multiply(c,c)
    res = np.sum(c)/(h*w)
    return res

print("\nMSE entre imagem original e DCT")
print(MSE(A,A_dct))

print("\nMSE entre DCT e DCT arredondada")
print(MSE(A_dct,A_dct_round))


# %%
# c) (0,5) Efetue a quantização dos coeficientes, obtendo o valor inteiro quantizado, através da tabela:
q = np.array([[5, 8],
              [8,12]])

# Quantização
def quantize(a,q):
    b = np.divide(a,q)
    b = np.round(b)
    return b

print(quantize(A_dct,q))


