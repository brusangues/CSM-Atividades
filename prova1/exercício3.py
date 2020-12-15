# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np

# Questão 3

sqrt2 = np.sqrt(2)
H4 =   [[    1,     1,     1,     1],
        [    1,     1,    -1,    -1],
        [sqrt2,-sqrt2,     0,     0],
        [    0,     0, sqrt2,-sqrt2]]
H4 = np.array(H4)/2


RA = 11201721076
R1,R2,R3,R4 = 1,72,10,76

F =[[R1, 0, 0,R1],
    [ 0,R2,R2, 0],
    [ 0,R3,R3, 0],
    [R4, 0, 0,R4]]
F = np.array(F)

print("H4\n",H4)
print("F\n",F)


# %%
# a) (1,5) Calcule a transforma de Haar para a imagem F4x4 que você montou com seu RA.
def Haar(F):
    H4F = np.matmul(H4,F)
    T = np.matmul(H4F,H4.T)
    return T

T = Haar(F)

print("T\n", T)

print("\nArrendondando para tornar mais legível")
print("T_round\n", np.round(T,2))


# %%
# b) (1,0) Faça a reconstrução da imagem, a partir de T, obtendo novamente F e mostre todos os Cálculos efetuados.

### Cálculos
# Legenda:
#   H_t     = Transposta de H
#   H_inv   = Inversa de H
#   H_t_inv = Inversa da Transposta de H


#               T = H F H_t
#         H_inv T = H_inv H F H_t
#         H_inv T = F H_t
# H_inv T H_t_inv = F H_t H_t_inv
# H_inv T H_t_inv = F
#   H_t T H_t_inv = F
#               F = H_t T H_t_inv

def Haar_inv(T):
    # F = H_t T H_t_inv
    H_t     = H4.T
    H_t_inv = np.linalg.inv(H4.T)

    H_tT = np.matmul(H_t,T)
    F = np.matmul(H_tT,H_t_inv)
    return F

F_reconstructed = Haar_inv(T)

print("F_original\n", F)
print("F_reconstructed (Arrendondado para tornar mais legível)\n", np.round(F_reconstructed))

null.tpl [markdown]
# <img src="exercício3b.jpeg" width=500px>

