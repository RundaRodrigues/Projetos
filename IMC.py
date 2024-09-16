#Formula IMC = peso (kg) / altura (m)
#Abaixo do peso: IMC menor que 18,5
#Peso normal: IMC entre 18,5 e 24,9

peso = float(input('Insira seu peso em KG: (EX:. 70)'))
altura = float(input('Insira sua altura em metros: (EX:. 1.7)'))

IMC = peso / (altura**2)


if IMC < 18.5:
    print ('Voce esta abaixo do peso ideal e seu IMC é de: ', IMC)
else :
    print ('Voce esta em seu peso ideal e seu IMC é de: ', IMC)
