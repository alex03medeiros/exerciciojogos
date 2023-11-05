import random

# Lista de palavras para o jogo
palavras = ["python", "java", "ruby", "javascript", "html", "css"]

def escolher_palavra(palavras):
    # Escolhe uma palavra aleatória da lista
    palavra = random.choice(palavras)
    return palavra

def desenhar_forca(erros):
    forca = [
        """
           -------
           |     |
                 |
                 |
                 |
                 |
        """,
        """
           -------
           |     |
           O     |
                 |
                 |
                 |
        """,
        """
           -------
           |     |
           O     |
           |     |
                 |
                 |
        """,
        """
           -------
           |     |
           O     |
          /|     |
                 |
                 |
        """,
        """
           -------
           |     |
           O     |
          /|\\    |
                 |
                 |
        """,
        """
           -------
           |     |
           O     |
          /|\\    |
          /      |
                 |
        """,
        """
           -------
           |     |
           O     |
          /|\\    |
          / \\    |
                 |
        """
    ]
    return forca[erros]

def jogar_forca(palavra):
    # Inicialização de variáveis
    letras_corretas = []
    tentativas = 6
    erros = 0

    # Cria uma lista de "_" para representar as letras da palavra
    palavra_oculta = ["_" for _ in palavra]

    while True:
        # Mostra o estado atual da palavra e a forca
        print("Palavra: " + " ".join(palavra_oculta))
        print("Tentativas restantes:", tentativas)
        print(desenhar_forca(erros))

        # Solicita uma letra do jogador
        letra = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi usada
        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # Verifica se a letra está na palavra
        if letra in palavra:
            print("Letra correta!")
            letras_corretas.append(letra)

            # Atualiza a palavra oculta
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            print("Letra errada. Tente novamente.")
            tentativas -= 1
            erros += 1

        # Verifica se o jogador ganhou
        if "".join(palavra_oculta) == palavra:
            print("Parabéns! Você venceu. A palavra era:", palavra)
            break

        # Verifica se o jogador perdeu
        if erros == 6:
            print("Você perdeu. A palavra era:", palavra)
            break

if __name__ == "__main__":
    palavra = escolher_palavra(palavras)
    print("Bem-vindo ao Jogo da Forca!")
    jogar_forca(palavra)