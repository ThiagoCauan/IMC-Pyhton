peso = float(input("Informe o seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura*altura)

print(f"Seu imc é de: {imc:.2f}")

if imc < 18.5:
    print("Você está muito magro!")
elif imc >= 18.5 and imc <= 24.9:
    print("Você está no peso ideal!")
elif imc >= 25.0 and imc <= 29.9:
    print("Você está com sobrepeso!")
elif imc >= 30.0 and imc <= 39.9:
    print("Você está obeso!")
elif imc >= 40.0:
    print("Você está com obesidade grave")
else:
 print("erro")
