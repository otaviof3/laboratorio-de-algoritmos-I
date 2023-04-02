nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
frequencia = float(input("Digite a sua frequência de aula(%): "))
if media >= 7.0 and frequencia >= 75:
    print("Você foi aprovado!")
elif media >= 4.0 and media < 7.0 and frequencia > 75:
    print("Você está de exame.")
else:
    print("Você está reprovado...")