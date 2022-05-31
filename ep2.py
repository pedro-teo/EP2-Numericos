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

#x = 3
#y = 4
#print(eval("np.sqrt(pow(x,2)+pow(y,2))"))
#print(eval("x-y"))

## Input do usuario dos limites de integracao
#option = int(input("Qual a variavel de integracao da integral mais interna? "))
#a = int(input("Qual o valor do limite de integracao a? "))
#b = int(input("Qual o valor do limite de integracao b? "))
#c = input("Qual a funcao c(x) do limite inferior? ")
#d = input("Qual a funcao d(x) do limite superior? ")

## Exemplo 2 do enunciado do EP
a = 0
b = 1
funcaoC = "0"
funcaoD = "1 - pow(x,2)"
funcaoXY = "1"

##isto nao funciona
##print(eval(d-f))

#t = n6[0][1]
#x = "((b-a)*t + a + b)/2"
#print(eval(x))
#comentado so pra vc lembrar que isso funciona
#print(eval(f)+1)

n = 6
resultado = 0
funcaoX = "((b-a)*t + a + b)/2"
funcaoY = "((d-c)*s + c + d)/2"

for i in range (0,n):
    fMaiusculo = 0
    t = n6[i][0]
    for j in range (0,n):
        s = n6[j][0]
        x = eval(funcaoX) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
        c = eval(funcaoC) 
        d = eval(funcaoD)
        y = eval(funcaoY)
        fMaiusculo = fMaiusculo + n6[j][1] * eval(funcaoXY) * (d-c)
    resultado = resultado + n6[i][1] * fMaiusculo

resultado = resultado * (b-a) / 4
print(resultado)



n = 8
resultado = 0
for i in range (0,n):
    fMaiusculo = 0
    t = n8[i][0]
    for j in range (0,n):
        s = n8[j][0]
        x = eval(funcaoX) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
        c = eval(funcaoC) 
        d = eval(funcaoD)
        y = eval(funcaoY)
        fMaiusculo = fMaiusculo + n8[j][1] * eval(funcaoXY) * (d-c)
    resultado = resultado + n8[i][1] * fMaiusculo

resultado = resultado * (b-a) / 4
print(resultado)

n = 10
resultado = 0
for i in range (0,n):
    fMaiusculo = 0
    t = n10[i][0]
    for j in range (0,n):
        s = n10[j][0]
        x = eval(funcaoX) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
        c = eval(funcaoC)
        d = eval(funcaoD)
        y = eval(funcaoY)
        fMaiusculo = fMaiusculo + n10[j][1] * eval(funcaoXY) * (d-c)
    resultado = resultado + n10[i][1] * fMaiusculo

resultado = resultado * (b-a) / 4
print(resultado)

# teste da funcao x + 2 + y
n = 6
resultado = 0
funcaoX = "((b-a)*t + a + b)/2"
funcaoY = "((d-c)*s + c + d)/2"
a = 0
b = 1
funcaoC = "0"
funcaoD = "1"
funcaoXY = "x + 2 + y"

for i in range (0,n):
    fMaiusculo = 0
    t = n6[i][0]
    for j in range (0,n):
        s = n6[j][0]
        x = eval(funcaoX) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
        c = eval(funcaoC) 
        d = eval(funcaoD)
        y = eval(funcaoY)
        fMaiusculo = fMaiusculo + n6[j][1] * eval(funcaoXY) * (d-c)
    resultado = resultado + n6[i][1] * fMaiusculo

resultado = resultado * (b-a) / 4
print(resultado)


# teste da funcao x + 2 + y
n = 8
resultado = 0
funcaoX = "((b-a)*t + a + b)/2"
funcaoY = "((d-c)*s + c + d)/2"
a = 0
b = 1
funcaoC = "0"
funcaoD = "1"
funcaoXY = "x + 2 + y"

for i in range (0,n):
    fMaiusculo = 0
    t = n8[i][0]
    for j in range (0,n):
        s = n8[j][0]
        x = eval(funcaoX) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
        c = eval(funcaoC) 
        d = eval(funcaoD)
        y = eval(funcaoY)
        fMaiusculo = fMaiusculo + n8[j][1] * eval(funcaoXY) * (d-c)
    resultado = resultado + n8[i][1] * fMaiusculo

resultado = resultado * (b-a) / 4
print(resultado)

#teste do ex 3 com n = 6
n = 6
resultado = 0
funcaoX = "((b-a)*t + a + b)/2"
funcaoY = "((d-c)*s + c + d)/2"
a = 0.1
b = 0.5
funcaoC = "pow(x,3)"
funcaoD = "pow(x,2)"
funcaoXY = "np.sqrt(pow((-y/x)*np.exp(y/x),2)+pow(np.exp(y/x)/x,2)+1)"

for i in range (0,n):
    fMaiusculo = 0
    t = n6[i][0]
    for j in range (0,n):
        s = n6[j][0]
        x = eval(funcaoX) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
        c = eval(funcaoC) 
        d = eval(funcaoD)
        y = eval(funcaoY)
        fMaiusculo = fMaiusculo + n6[j][1] * eval(funcaoXY) * (d-c)
    resultado = resultado + n6[i][1] * fMaiusculo

resultado = resultado * (b-a) / 4
print(resultado)


#teste do ex 3 com n = 8
n = 8
resultado = 0
funcaoX = "((b-a)*t + a + b)/2"
funcaoY = "((d-c)*s + c + d)/2"
a = 0.1
b = 0.5
funcaoC = "pow(x,3)"
funcaoD = "pow(x,2)"
funcaoXY = "np.sqrt(pow((-y/x)*np.exp(y/x),2)+pow(np.exp(y/x)/x,2)+1)"

for i in range (0,n):
    fMaiusculo = 0
    t = n8[i][0]
    for j in range (0,n):
        s = n8[j][0]
        x = eval(funcaoX) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
        c = eval(funcaoC) 
        d = eval(funcaoD)
        y = eval(funcaoY)
        fMaiusculo = fMaiusculo + n8[j][1] * eval(funcaoXY) * (d-c)
    resultado = resultado + n8[i][1] * fMaiusculo

resultado = resultado * (b-a) / 4
print(resultado)

#teste do ex 3 com n = 10
n = 10
resultado = 0
funcaoX = "((b-a)*t + a + b)/2"
funcaoY = "((d-c)*s + c + d)/2"
a = 0.1
b = 0.5
funcaoC = "pow(x,3)"
funcaoD = "pow(x,2)"
funcaoXY = "np.sqrt(pow((-y/x)*np.exp(y/x),2)+pow(np.exp(y/x)/x,2)+1)"

for i in range (0,n):
    fMaiusculo = 0
    t = n10[i][0]
    for j in range (0,n):
        s = n10[j][0]
        x = eval(funcaoX) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
        c = eval(funcaoC) 
        d = eval(funcaoD)
        y = eval(funcaoY)
        fMaiusculo = fMaiusculo + n10[j][1] * eval(funcaoXY) * (d-c)
    resultado = resultado + n10[i][1] * fMaiusculo

resultado = resultado * (b-a) / 4
print(resultado)