from colorama import Fore, Style

# Lista das situações do reservatório
situacao_do_reservatorio = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]


# Função para definir a cor do nível de água
def definir_cor_nivel_de_agua(nivel_de_agua):
    if nivel_de_agua == 1:
        return Fore.RED
    elif nivel_de_agua == 2:
        return Fore.YELLOW
    elif nivel_de_agua == 3:
        return Fore.GREEN
    elif nivel_de_agua == 4:
        return Fore.CYAN
    elif nivel_de_agua == 5:
        return Fore.BLUE


# Entrada de dados
nivel_de_agua = int(input("Informe o nível de água atual: "))

print(f"O valor digitado é: {nivel_de_agua}")


# Validação do nível de água
if nivel_de_agua >= 1 and nivel_de_agua <= 5:

    # Localizar a situação na lista
    posicao_situacao_do_reservatorio = nivel_de_agua - 1

    # Definir a cor correspondente
    cor = definir_cor_nivel_de_agua(nivel_de_agua)

    # Exibir a situação com a cor
    print(cor + situacao_do_reservatorio[posicao_situacao_do_reservatorio])

    # Restaurar a formatação do terminal
    print(Style.RESET_ALL)

else:
    print("Nível inválido! Digite um número entre 1 e 5.")