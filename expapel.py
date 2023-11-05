def determinar_vencedor(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate!"
    if (
        (jogador1 == "pedra" and jogador2 == "tesoura") or
        (jogador1 == "papel" and jogador2 == "pedra") or
        (jogador1 == "tesoura" and jogador2 == "papel")
    ):
        return "Jogador 1 venceu!"
    return "Jogador 2 venceu!"

def jogar_novo_jogo():
    jogador1 = input("Jogador 1, escolha Pedra, Papel ou Tesoura: ").lower()
    jogador2 = input("Jogador 2, escolha Pedra, Papel ou Tesoura: ").lower()

    if jogador1 not in ["pedra", "papel", "tesoura"] or jogador2 not in ["pedra", "papel", "tesoura"]:
        print("Escolha inválida. Tente novamente.")
        return jogar_novo_jogo()

    print(f"Jogador 1 escolheu {jogador1}. Jogador 2 escolheu {jogador2}.")
    resultado = determinar_vencedor(jogador1, jogador2)
    print(resultado)

    jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower()
    if jogar_novamente == "sim":
        jogar_novo_jogo()
    else:
        print("Obrigado por jogar!")

# Iniciar o jogo
print("Bem-vindo ao jogo Pedra, Papel e Tesoura para dois jogadores!")
jogar_novo_jogo()