import os
import math
import random

def calculos():
    num1 = float(input("Digite o primeiro número para fazer os calculos: "))
    num2 = float(input("Digite o segundo número para fazer os calculos: "))
    adicao = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    potencia = math.pow(num1, num2)
    print(f"adição: {num1} + {num2} = {adicao}")
    print(f"subtração: {num1} - {num2} = {subtracao}")
    print(f"multiplicação: {num1} x {num2} = {multiplicacao}")
    print(f"divisão: {num1} / {num2} = {divisao}")
    print(f"potencia: {num1} elevado a {num2} = {potencia}")
    input("pressione qualquer tecla para continuar...")

def raiz_quadrada():
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    if numero < 0:
        print("não é possivel calcular a raiz quadrada de número negativo!")
    else:
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {resultado}")
    input("pressione qualquer tecla para continuar...")

def potencia():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"{base} elevado a {expoente} é igual a {resultado}")
    input("pressione qualquer tecla para continuar...")

def numero_aleatorio():
    inicio = int(input("digite o valor inicial do intervalo: "))
    fim = int(input("digite o valor final do intervalo: "))
    if inicio > fim:
        print("o valor inicial deve ser maior ou igual ao final")
    else:
        numero = random.randint(inicio, fim)
        print(f"Número aleatório gerado entre {inicio} e {fim}: {numero}")
    input("pressione qualquer tecla para continuar...")

def main():
    while True:
        os.system("cls")
        print("\n ---menu de operações---")
        print("1 - raiz quadrada")
        print("2 - potencia")
        print("3 - Número aleatório")
        print("4 - calculos")
        print("5 - sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            raiz_quadrada()
        elif opcao == '2':
            potencia()
        elif opcao == '3':
            numero_aleatorio()
        elif opcao == '4':
            calculos()
        elif opcao == '5':
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida! tente novamente.")

if __name__ == "__main__":
    main()

        
