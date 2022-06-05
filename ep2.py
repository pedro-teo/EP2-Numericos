###     MAP3121 - Calculo Numerico - Escola Politecnica                  ###
###     Tarefa 2 - Formulas de Integracao Numerica de Gauss              ###

###     Alunos deste grupo:                                              ###       
###     Fabio Akira Yonamine   - NUSP 11805398                           ###
###     Pedro H. Teodoro Silva - NUSP 11805314                           ###

## Importacao da biblioteca numpy, com abreviacao np
import numpy as np

##  Funcao principal.  ##
def main():
    ##  Menu de selecao do usuario.  ##
    print("Opcao 1: Calculo do exercicio 1.")
    print("Opcao 2: Calculo do exercicio 2.")
    print("Opcao 3: Calculo do exercicio 3.")
    print("Opcao 4: Calculo do exercicio 4.")
    print("Opcao 5: Calculo de uma integral simples a ser inputada.")
    print("Opcao 6: Calculo de uma integral dupla a ser inputada.")
    opcaoDesejada = int(input("Digite a opcao desejada: "))

    if(opcaoDesejada==1): ##  Executa os calculos do Exemplo 1.  ## ## CHECKCHECK ##
        print("")

        print("Volume do cubo")
        a = 0
        b = 1
        funcaoC = "0"
        funcaoD = "1"
        funcaoXY = "1"
        print("Para n = 6,  integral = ", calculaIntegralDupla(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDupla(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDupla(10,a,b,funcaoC,funcaoD,funcaoXY))
        print("")

        print("Volume do tetraedro")
        a = 0
        b = 1
        funcaoC = "0"
        funcaoD = "1-x"
        funcaoXY = "1-x-y"
        print("Para n = 6,  integral = ", calculaIntegralDupla(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDupla(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDupla(10,a,b,funcaoC,funcaoD,funcaoXY))
        print("")

    elif(opcaoDesejada==2): ##  Executa os calculos do Exemplo 2.  ## ## CHECKCHECK ##
        print("")

        print("Area A, considerando a primeira integral com limites em dydx, nesta ordem: ")
        a = 0
        b = 1
        funcaoC = "0"
        funcaoD = "1 - pow(x,2)"
        funcaoXY = "1"
        print("Para n = 6,  integral = ", calculaIntegralDupla(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDupla(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDupla(10,a,b,funcaoC,funcaoD,funcaoXY))
        print("")

        print("Area A, considerando a segunda integral com limites em dxdy, nesta ordem: ")
        a = 0
        b = 1
        funcaoC = "0"
        funcaoD = "np.sqrt(1-y)"
        funcaoXY = "1"
        print("Para n = 6,  integral = ", calculaIntegralDuplaDxDy(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDuplaDxDy(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDuplaDxDy(10,a,b,funcaoC,funcaoD,funcaoXY))
        print("")

    elif(opcaoDesejada==3): ##  Executa os calculos do Exemplo 3.  ## ## CHECKCHECK ##
        print("")
        
        print("Calculo da area da regiao descrita:")
        a = 0.1
        b = 0.5
        funcaoC = "pow(x,3)"
        funcaoD = "pow(x,2)"
        funcaoXY = "np.sqrt(( (pow(y,2)/pow(x,4))*np.exp(2*y/x) + np.exp(2*y/x)/pow(x,2) + 1 ))"
        print("Para n = 6,  integral = ", calculaIntegralDupla(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDupla(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDupla(10,a,b,funcaoC,funcaoD,funcaoXY))
        print("")
        
        print("Calculo do volume da regiao descrita:")
        a = 0.1
        b = 0.5
        funcaoC = "pow(x,3)"
        funcaoD = "pow(x,2)"
        funcaoXY = "np.exp(y/x)"
        print("Para n = 6,  integral = ", calculaIntegralDupla(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDupla(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDupla(10,a,b,funcaoC,funcaoD,funcaoXY))
        print("")

    elif(opcaoDesejada==4): ##  Executa os calculos do Exemplo 4.  ##
        print("")
        
        print("Calculo do volume da calota esferica descrita:")
        a = 0
        b = 1/4
        funcaoC = "0"
        funcaoD = "np.sqrt(1-pow(y+3/4,2))"
        funcaoXY = "2*x*np.pi"
        print("Para n = 6,  integral = ", calculaIntegralDuplaDxDy(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDuplaDxDy(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDuplaDxDy(10,a,b,funcaoC,funcaoD,funcaoXY))
        print("")

        print("Calculo do volume do solido de revolucao descrito:")
        print("Check aqui??")
        a = -1
        b = 1
        funcaoC = "0"
        funcaoD = "np.exp(-pow(y,2))"
        funcaoXY = "2*x*np.pi"
        print("Para n = 6,  integral = ", calculaIntegralDuplaDxDy(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDuplaDxDy(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDuplaDxDy(10,a,b,funcaoC,funcaoD,funcaoXY))
        print("")
    
    elif(opcaoDesejada==5):
        a = np.exp(-1)
        b = 1
        funcaoC = "-1"
        funcaoD = "np.exp(-pow(x,2))"
        funcaoXY = "x"
        print("Para n = 6,  integral = ", calculaIntegralDupla(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDupla(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDupla(10,a,b,funcaoC,funcaoD,funcaoXY))
        
        print("Para n = 6,  integral = ", calculaIntegralDupla(6,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 8,  integral = ", calculaIntegralDupla(8,a,b,funcaoC,funcaoD,funcaoXY))
        print("Para n = 10, integral = ", calculaIntegralDupla(10,a,b,funcaoC,funcaoD,funcaoXY))

    elif(opcaoDesejada==6):
        a = int(input("Qual o valor do limite de integracao a? "))
        b = int(input("Qual o valor do limite de integracao b? "))
        funcaoC = input("Qual a funcao c(x) do limite inferior? ")
        funcaoD = input("Qual a funcao d(x) do limite superior? ")
        funcaoXY = input("Qual a funcao em termos de X e Y que se deseja integrar? ")
        limiteInterno = input("A integral mais interna eh em relacao a X ou Y? Digite 1 para X, ou 2 para Y: ")

        if (limiteInterno == 1):
            print("ola")
        elif (limiteInterno == 2):
            print("ola2")
        else:
            print("Opcao invalida para a integral mais interna. Tente novamente!")

##  Funcao que resolve integrais duplas, com limite dydx, obrigatoriamente nesta ordem.  ##
def calculaIntegralDupla (n,a,b,funcaoC,funcaoD,funcaoXY):
    ##  Armazenamento dos valores para n = 6,8 e 10, fornecidos nas instrucoes.  ## 
    n6 = np.zeros((6,2))
    n6 = [[-0.9324695142031520278123016,0.1713244923791703450402961],[-0.6612093864662645136613996,0.3607615730481386075698335],[-0.2386191860831969086305017,0.4679139345726910473898703],[0.2386191860831969086305017,0.4679139345726910473898703],[0.6612093864662645136613996,0.3607615730481386075698335],[0.9324695142031520278123016,0.1713244923791703450402961]]

    n8  = np.zeros((8,2))
    n8 = [[-0.9602898564975362316835609,0.1012285362903762591525314],[-0.7966664774136267395915539,0.2223810344533744705443560],[-0.5255324099163289858177390,0.3137066458778872873379622],[-0.1834346424956498049394761,0.3626837833783619829651504],[0.1834346424956498049394761,0.3626837833783619829651504],[0.5255324099163289858177390,0.3137066458778872873379622],[0.7966664774136267395915539,0.2223810344533744705443560],[0.9602898564975362316835609,0.1012285362903762591525314]]

    n10 = np.zeros((10,2))
    n10 = [[-0.9739065285171717200779640,0.0666713443086881375935688],[-0.8650633666889845107320967,0.1494513491505805931457763],[-0.6794095682990244062343274,0.2190863625159820439955349],[-0.4333953941292471907992659,0.2692667193099963550912269],[-0.1488743389816312108848260,0.2955242247147528701738930],[0.1488743389816312108848260,0.2955242247147528701738930],[0.4333953941292471907992659,0.2692667193099963550912269],[0.6794095682990244062343274,0.2190863625159820439955349],[0.8650633666889845107320967,0.1494513491505805931457763],[0.9739065285171717200779640,0.0666713443086881375935688]]
    
    ##  Inicializa a variavel que guardara o valor final da integral dupla desejada em zero.  ##
    resultado = 0

    ##  Funcoes genericas que definem X e Y, dada a transformação para S e T, respectivamente, para  ##
    ##  que os limites de integracao das duas integrais sejam -1 e 1, de modo a usar os nos e pesos  ##
    ##  pre-fornecidos no enunciado.                                                                 ##                               
    funcaoX = "((b-a)*t + a + b)/2"
    funcaoY = "((d-c)*s + c + d)/2"

    ##  Caso em que escolheu-se n = 6.  ##
    if(n==6):
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

    ##  Caso em que escolheu-se n = 8.  ##
    elif(n==8):
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
    
    ##  Caso em que escolheu-se n = 10.  ##
    elif(n==10):
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

    ##  Caso em que nao foi escolhido n com nos e pesos cadastrados.  ##
    else:
        resultado = 0
        print("O n escolhido nao esta cadastrado. Tente novamente, com n = 6, 8 ou 10!")

    ##  Retorna o resultado para a chamada de funcao.  ##
    return resultado

##  Funcao que resolve integrais duplas, com limite dxdy, obrigatoriamente nesta ordem.  ##
def calculaIntegralDuplaDxDy (n,a,b,funcaoC,funcaoD,funcaoXY):
    ##  Armazenamento dos valores para n = 6,8 e 10, fornecidos nas instrucoes.  ## 
    n6 = np.zeros((6,2))
    n6 = [[-0.9324695142031520278123016,0.1713244923791703450402961],[-0.6612093864662645136613996,0.3607615730481386075698335],[-0.2386191860831969086305017,0.4679139345726910473898703],[0.2386191860831969086305017,0.4679139345726910473898703],[0.6612093864662645136613996,0.3607615730481386075698335],[0.9324695142031520278123016,0.1713244923791703450402961]]

    n8  = np.zeros((8,2))
    n8 = [[-0.9602898564975362316835609,0.1012285362903762591525314],[-0.7966664774136267395915539,0.2223810344533744705443560],[-0.5255324099163289858177390,0.3137066458778872873379622],[-0.1834346424956498049394761,0.3626837833783619829651504],[0.1834346424956498049394761,0.3626837833783619829651504],[0.5255324099163289858177390,0.3137066458778872873379622],[0.7966664774136267395915539,0.2223810344533744705443560],[0.9602898564975362316835609,0.1012285362903762591525314]]

    n10 = np.zeros((10,2))
    n10 = [[-0.9739065285171717200779640,0.0666713443086881375935688],[-0.8650633666889845107320967,0.1494513491505805931457763],[-0.6794095682990244062343274,0.2190863625159820439955349],[-0.4333953941292471907992659,0.2692667193099963550912269],[-0.1488743389816312108848260,0.2955242247147528701738930],[0.1488743389816312108848260,0.2955242247147528701738930],[0.4333953941292471907992659,0.2692667193099963550912269],[0.6794095682990244062343274,0.2190863625159820439955349],[0.8650633666889845107320967,0.1494513491505805931457763],[0.9739065285171717200779640,0.0666713443086881375935688]]
    
    ##  Inicializa a variavel que guardara o valor final da integral dupla desejada em zero.  ##
    resultado = 0

    ##  Funcoes genericas que definem X e Y, dada a transformação para S e T, respectivamente, para  ##
    ##  que os limites de integracao das duas integrais sejam -1 e 1, de modo a usar os nos e pesos  ##
    ##  pre-fornecidos no enunciado.                                                                 ##                               
    funcaoY = "((b-a)*t + a + b)/2"
    funcaoX = "((d-c)*s + c + d)/2"

    ##  Caso em que escolheu-se n = 6.  ##
    if(n==6):
        for i in range (0,n):
            fMaiusculo = 0
            t = n6[i][0]
            for j in range (0,n):
                s = n6[j][0]
                y = eval(funcaoY) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
                c = eval(funcaoC) 
                d = eval(funcaoD)
                x = eval(funcaoX)
                fMaiusculo = fMaiusculo + n6[j][1] * eval(funcaoXY) * (d-c)
            resultado = resultado + n6[i][1] * fMaiusculo
        resultado = resultado * (b-a) / 4

    ##  Caso em que escolheu-se n = 8.  ##
    elif(n==8):
        for i in range (0,n):
            fMaiusculo = 0
            t = n8[i][0]
            for j in range (0,n):
                s = n8[j][0]
                y = eval(funcaoY) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
                c = eval(funcaoC) 
                d = eval(funcaoD)
                x = eval(funcaoX)
                fMaiusculo = fMaiusculo + n8[j][1] * eval(funcaoXY) * (d-c)
            resultado = resultado + n8[i][1] * fMaiusculo
        resultado = resultado * (b-a) / 4
    
    ##  Caso em que escolheu-se n = 10.  ##
    elif(n==10):
        for i in range (0,n):
            fMaiusculo = 0
            t = n10[i][0]
            for j in range (0,n):
                s = n10[j][0]
                y = eval(funcaoY) # x precisa ser obtido antes, porque ele vai em c(x) e d(x), que vao entao pra y 
                c = eval(funcaoC) 
                d = eval(funcaoD)
                x = eval(funcaoX)
                fMaiusculo = fMaiusculo + n10[j][1] * eval(funcaoXY) * (d-c)
            resultado = resultado + n10[i][1] * fMaiusculo
        resultado = resultado * (b-a) / 4

    ##  Caso em que nao foi escolhido n com nos e pesos cadastrados.  ##
    else:
        resultado = 0
        print("O n escolhido nao esta cadastrado. Tente novamente, com n = 6, 8 ou 10!")

    ##  Retorna o resultado para a chamada de funcao.  ##
    return resultado

##  Comanda o programa a voltar para a funcao main.  ##
if __name__ == '__main__':
    main()