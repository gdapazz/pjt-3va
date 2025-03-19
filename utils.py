import os
import time

def limpar_tela():
    """Limpa a tela do console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_titulo(texto):
    """Exibe um título formatado"""
    print("\n" + "=" * 50)
    print(f"{texto.center(50)}")
    print("=" * 50 + "\n")

def pausar(segundos=1):
    """Pausa a execução por um tempo determinado"""
    time.sleep(segundos)

def exibir_menu(opcoes):
    """Exibe um menu de opções e retorna a escolha do usuário"""
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    
    while True:
        try:
            escolha = int(input("\nEscolha uma opção: "))
            if 1 <= escolha <= len(opcoes):
                return escolha
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")

def exibir_status(personagem):
    """Exibe o status atual de um personagem"""
    print(f"{personagem.nome}: Vida: {personagem.vida}/{personagem.vida_maxima} | Ataque: {personagem.ataque} | Defesa: {personagem.defesa}")

def exibir_combate(personagem1, personagem2):
    """Exibe o status de dois personagens em combate"""
    print("\n" + "-" * 50)
    exibir_status(personagem1)
    exibir_status(personagem2)
    print("-" * 50)