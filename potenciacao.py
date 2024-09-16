# Algoritmo para calcular a potência r = a^b
a = int(input("Informe o valor de a (base): "))
b = int(input("Informe o valor de b (expoente): "))

r = 1
contador = 0

while contador < b:
    r *= a
    contador += 1

print(f"O resultado de {a} elevado a {b} é {r}.")

