# Programa para verificar se o numero é Impar ou Par.

# Loop principal do programa.
# O programa continuará executando até o usuário escolher a opção 2.
while True:

    # Exibe o menu principal
    print("\n╔════════════════════════════════════════╗")
    print("║          🔢 VERIFICADOR                ║")
    print("╠════════════════════════════════════════╣")
    print("║  1 - Verificar número                  ║")
    print("║  2 - Sair                              ║")
    print("╚════════════════════════════════════════╝")

    # Solicita ao usuário uma opção do menu
    opcao = input("\n👉 Escolha uma opção: ")

    # Verifica se o usuário escolheu a opção 1
    if opcao == "1":

        # Solicita um número e converte o valor recebido para inteiro
        numero = int(input("\n🔢 Digite um número: "))

        # Exibe uma linha para separar as informações
        print("─" * 42)

        # Verifica se o número é divisível por 2.
        # Se o resto da divisão for 0, o número é par.
        if numero % 2 == 0:
            print(f"✅ O número {numero} é PAR!")

        # Caso o resto seja diferente de 0, o número é ímpar.
        else:
            print(f"❌ O número {numero} é ÍMPAR!")

        # Exibe outra linha para finalizar o resultado
        print("─" * 42)

    # Verifica se o usuário escolheu a opção 2
    elif opcao == "2":

        # Mensagem de encerramento
        print("\n👋 Programa encerrado. Até mais!")

        # Encerra o loop e finaliza o programa
        break

    # Caso o usuário digite uma opção que não existe
    else:
        print("\n⚠️ Opção inválida! Escolha 1 ou 2.")
