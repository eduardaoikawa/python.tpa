import os
import math
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
