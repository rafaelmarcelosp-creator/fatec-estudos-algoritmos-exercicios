print("=== Cálculo Média Aluno === \n")

# Entrada com o nome do aluno
aluno = input("Digite o nome do aluno: ")

# Mensagem usando o nome digitado
print(f"\n Digite as três notas do aluno {aluno}")

# Entrada das notas para calculo de media
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Mostrar média formatada com 2 casas decimais
print(f"\n A nota média do aluno {aluno} foi: {media:.2f}")

# Verificação de codição de aprovação
if media >= 7:
    print(f"O Aluno {aluno} foi aprovado!")
else:
    print(f"O Aluno {aluno} foi reprovado!")
