###     MAP3121 - Calculo Numerico - Escola Politecnica                  ###
###     Tarefa 2 - Formulas de Integracao Numerica de Gauss              ###

###     Alunos deste grupo:                                              ###       
###     Fabio Akira Yonamine   - NUSP 11805398                           ###
###     Pedro H. Teodoro Silva - NUSP 11805314                           ###

## Importacao da biblioteca numpy, com abreviacao np
import numpy as np

## Armazenamento dos valores para n = 6,8 e 10, fornecidos nas instrucoes ## 
n6 = np.zeros((6,2))
n6 = [[-0.9324695142031520278123016,0.1713244923791703450402961],[-0.6612093864662645136613996,0.3607615730481386075698335],[-0.2386191860831969086305017,0.4679139345726910473898703],[0.2386191860831969086305017,0.4679139345726910473898703],[0.6612093864662645136613996,0.3607615730481386075698335],[0.9324695142031520278123016,0.1713244923791703450402961]]

n8  = np.zeros((8,2))
n8 = [[-0.9602898564975362316835609,0.1012285362903762591525314],[-0.7966664774136267395915539,0.2223810344533744705443560],[-0.5255324099163289858177390,0.3137066458778872873379622],[-0.1834346424956498049394761,0.3626837833783619829651504],[0.1834346424956498049394761,0.3626837833783619829651504],[0.5255324099163289858177390,0.3137066458778872873379622],[0.7966664774136267395915539,0.2223810344533744705443560],[0.9602898564975362316835609,0.1012285362903762591525314]]

n10 = np.zeros((10,2))
n10 = [[-0.9739065285171717200779640,0.0666713443086881375935688],[-0.8650633666889845107320967,0.1494513491505805931457763],[-0.6794095682990244062343274,0.2190863625159820439955349],[-0.4333953941292471907992659,0.2692667193099963550912269],[-0.1488743389816312108848260,0.2955242247147528701738930],[0.1488743389816312108848260,0.2955242247147528701738930],[0.4333953941292471907992659,0.2692667193099963550912269],[0.6794095682990244062343274,0.2190863625159820439955349],[0.8650633666889845107320967,0.1494513491505805931457763],[0.9739065285171717200779640,0.0666713443086881375935688]]

#so pra lembrar como chamar uma linha/casa especifica
#n6 = [[1,2],[2,3],[4,3],[5,4],[2,3],[1,2]]
#print(n6)
#print(n6[2][1])
#print(n10[9][:])

x = 3
y = 4
print(eval("np.sqrt(pow(x,2)+pow(y,2))"))
print(eval("x-y"))

## Input do usuario dos limites de integracao
#a = int(input("Qual o valor do limite de integracao a? "))
#b = int(input("Qual o valor do limite de integracao b? "))
#c = input("Qual a funcao c(x) do limite inferior? ")
#d = input("Qual a funcao d(x) do limite superior? ")

## Exemplo 2 do enunciado do EP
a = 0
b = 1
c = "0"
d = "1 - pow(x,2)"
f = "1"

#t = n6[0][1]
#x = "((b-a)*t + a + b)/2"
#print(eval(x))
#comentado so pra vc lembrar que isso funciona
#print(eval(f)+1)

n=6
resultado = 0
for i in range (0,n-1):
    fMaiusculo = 0
    t = n6[i][1]
    for j in range (0,n-1):
        s = n6[j][1]
        x = "((b-a)*t + a + b)/2"
        fMaiusculo = fMaiusculo + n6[i][j] * eval() * eval()
    resultado = resultado + n6[i][0] * fMaiusculo

#resultado = resultado * (b-a) / 4
#print(resultado)


