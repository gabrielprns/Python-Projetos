print("Bem-Vindo a calculadora de equações do segundo grau:")
a=float(input("digite um número para a: "))
b=float(input("digite um número para b: "))
c=float(input("digite um número para c: "))
A=(b**2)-(4*a*c)
x_1=(-b+(A**(1/2)))/2*a
x_2=(-b-(A**(1/2)))/2*a
if a==0:
    print("como o valor de a é igual a zero não será possível realizar uma equação do segundo grau")
    print("Obrigado por Jogar!!!!")
if A>0 and a!=0:
    print("O delta será: ",A,"como o valor de delta é positivo, haverão duas raízes reais, que serão as seguintes: " "a primeira será: ",x_1,"a segunda será: ",x_2)
    print("Obrigado por Jogar!!!!")
elif A==0 and a!=0:
    print("O delta será: ",A,"como o valor de delta é igual a 0, haverá apenas uma raíz real: ",x_1)
    print("Obrigado por Jogar!!!!")
elif A<0 and a!=0:
    print("O delta será: ",A,"como o valor de delta é menor que 0, não será possível obter raízes reais")
    print("Obrigado por Jogar!!!!")



