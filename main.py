from personagem import Personagem
from vilao import Vilao
from heroi import Heroi
from utils import limpar_tela, mostrar_titulo, pausar, exibir_menu, exibir_status, exibir_combate

def main():
    limpar_tela()
    mostrar_titulo("JOGO DE HERÓIS E VILÕES")
    print("Bem-vindo ao jogo de heróis e vilões!")
    pausar(1)
    
    # Criando personagens
    heroi = Heroi("Link", 17, 100, ataque=12, defesa=8)
    npc = Personagem("Zelda", 16, 80, ataque=0, defesa=0)
    vilao = Vilao("Ganon", 100, 120, ataque=14, defesa=6)
    
    # Criando estrutura para controlar locais explorados
    locais_explorados = set()
    
    # Iniciando o jogo
    historia_inicial(heroi, npc, vilao)
    
    # Loop principal do jogo
    while heroi.esta_vivo() and vilao.esta_vivo():
        limpar_tela()
        mostrar_titulo("MENU PRINCIPAL")
        print(f"Status atual de {heroi.nome}:")
        exibir_status(heroi)
        
        opcoes = ["Explorar", "Batalhar contra " + vilao.nome, "Usar poção", "Ver inventário", "Ver histórico", "Sair do jogo"]
        escolha = exibir_menu(opcoes)
        
        if escolha == 1:
            explorar(heroi, vilao, locais_explorados)
        elif escolha == 2:
            if not batalhar(heroi, vilao):
                break
        elif escolha == 3:
            print(heroi.usar_pocao())
            input("\nPressione ENTER para continuar...")
        elif escolha == 4:
            ver_inventario(heroi)
        elif escolha == 5:
            heroi.mostrar_historico()
            input("\nPressione ENTER para continuar...")
        elif escolha == 6:
            print("Obrigado por jogar!")
            break
    
    # Fim do jogo
    if not heroi.esta_vivo():
        mostrar_titulo("FIM DE JOGO")
        print(f"{vilao.nome} derrotou {heroi.nome}! A escuridão prevaleceu...")
    elif not vilao.esta_vivo():
        mostrar_titulo("VITÓRIA!")
        print(f"{heroi.nome} derrotou {vilao.nome}! A luz triunfou sobre a escuridão!")
    
    print("\nFim do jogo.")

def historia_inicial(heroi, npc, vilao):
    """Apresenta a história inicial do jogo"""
    limpar_tela()
    mostrar_titulo("HISTÓRIA")
    
    print(f"O reino de Hyrule está em perigo!")
    pausar(1)
    print(f"{vilao.nome}, o temível senhor das trevas, retornou após séculos de selamento.")
    pausar(1)
    
    print("\n" + heroi.dialogar("Preciso encontrar a Princesa Zelda antes que seja tarde demais!"))
    pausar(1)
    
    print("\nMas o pior já havia acontecido...")
    pausar(1)
    
    print("\n" + vilao.dialogar("Finalmente tenho a princesa! Ninguém pode me impedir agora!"))
    pausar(1)
    
    print("\n" + vilao.rir_malignamente())
    pausar(1)
    
    print("\n" + vilao.capturar_refem(npc))
    pausar(1)
    
    print("\n" + vilao.criar_base_secreta("Castelo das Sombras"))
    pausar(1)
    
    print("\nAgora, apenas o herói lendário pode salvar o reino...")
    pausar(1)
    
    print("\n" + heroi.dialogar("Não importa o que aconteça, eu salvarei a princesa e derrotarei Ganon!"))
    pausar(2)
    
    # Inicializar habilidades
    heroi.adicionar_habilidade("Espada Mestra", 15)
    heroi.adicionar_habilidade("Flecha de Luz", 20)
    vilao.adicionar_habilidade("Raio das Trevas", 18)
    vilao.adicionar_habilidade("Invocação Demoníaca", 22)
    
    input("\nPressione ENTER para continuar...")

def explorar(heroi, vilao, locais_explorados):
    """Função de exploração do mapa com limites de exploração"""
    limpar_tela()
    mostrar_titulo("EXPLORAÇÃO")
    
    locais = ["Floresta Perdida", "Deserto Gerudo", "Montanha da Morte", "Lago Hylia", "Vila Kakariko"]
    print("Para onde você deseja ir?")
    
    # Mostrar quais locais já foram explorados
    for i, local in enumerate(locais, 1):
        status = " (Explorado)" if local in locais_explorados else ""
        print(f"{i}. {local}{status}")
    
    try:
        escolha = int(input("\nEscolha uma opção: "))
        if 1 <= escolha <= len(locais):
            local = locais[escolha-1]
        else:
            print("Opção inválida.")
            input("\nPressione ENTER para continuar...")
            return
    except ValueError:
        print("Por favor, digite um número válido.")
        input("\nPressione ENTER para continuar...")
        return
    
    limpar_tela()
    print(f"{heroi.nome} está explorando {local}...")
    pausar(1)
    
    # Verificar se o local já foi explorado
    if local in locais_explorados:
        print(f"{heroi.nome} já explorou este local. Não há mais nada de valor para encontrar aqui.")
        input("\nPressione ENTER para continuar...")
        return
    
    # Eventos baseados no local escolhido
    if local == "Floresta Perdida":
        print(f"{heroi.nome} encontrou uma entrada secreta!")
        pausar(1)
        print(heroi.adicionar_item("Mapa do Castelo das Sombras"))
        heroi.nivel_heroismo += 1
        print(f"Nível de heroísmo aumentado para {heroi.nivel_heroismo}!")
    
    elif local == "Deserto Gerudo":
        print(f"{heroi.nome} encontrou uma fonte mágica!")
        heroi.usar_pocao()
        print(heroi.adquirir_pocao(2))
    
    elif local == "Montanha da Morte":
        print(f"{heroi.nome} encontrou um ferreiro que fortaleceu sua espada!")
        heroi.ataque += 3
        print(f"Ataque aumentado para {heroi.ataque}!")
    
    elif local == "Lago Hylia":
        print(f"{heroi.nome} encontrou uma fada que concedeu proteção!")
        heroi.defesa += 2
        print(f"Defesa aumentada para {heroi.defesa}!")
    
    elif local == "Vila Kakariko":
        print(f"{heroi.nome} encontrou informações sobre um refém!")
        print(heroi.dialogar("Tenho que salvar essa pessoa!"))
        heroi.pessoas_salvas.append("Aldeão")
        heroi.nivel_heroismo += 1
        print(f"Nível de heroísmo aumentado para {heroi.nivel_heroismo}!")
    
    # Adicionar o local à lista de locais explorados
    locais_explorados.add(local)
    
    input("\nPressione ENTER para continuar...")

def batalhar(heroi, vilao):
    """Sistema de batalha entre herói e vilão"""
    limpar_tela()
    mostrar_titulo("BATALHA")
    
    print(f"{heroi.nome} encontrou {vilao.nome}!")
    pausar(1)
    
    print(vilao.dialogar("Então você veio, herói tolo. Você não pode me derrotar!"))
    pausar(1)
    
    print(heroi.dialogar("Seu reinado de terror acaba hoje, Ganon!"))
    pausar(1)
    
    # Loop de batalha
    turno = 1
    # Rastrear habilidades já usadas nesta batalha
    habilidades_usadas = set()
    
    while heroi.esta_vivo() and vilao.esta_vivo():
        limpar_tela()
        mostrar_titulo(f"BATALHA - Turno {turno}")
        exibir_combate(heroi, vilao)
        
        # Turno do herói
        print(f"\nÉ o seu turno, {heroi.nome}!")
        opcoes = ["Atacar", "Defender", "Usar poção", "Usar habilidade", "Ataque heroico", "Inspirar"]
        escolha = exibir_menu(opcoes)
        
        if escolha == 1:  # Atacar
            print(heroi.atacar(vilao))
        elif escolha == 2:  # Defender
            print(heroi.defender())
        elif escolha == 3:  # Usar poção
            print(heroi.usar_pocao())
        elif escolha == 4:  # Usar habilidade
            if heroi.habilidades:
                print("\nEscolha uma habilidade:")
                habilidades = list(heroi.habilidades.keys())
                
                # Mostrar quais habilidades já foram usadas
                for i, hab in enumerate(habilidades, 1):
                    status = " (Já usada)" if hab in habilidades_usadas else ""
                    print(f"{i}. {hab} (Poder: {heroi.habilidades[hab]}){status}")
                
                try:
                    hab_escolha = int(input("\nEscolha uma habilidade: "))
                    if 1 <= hab_escolha <= len(habilidades):
                        hab_nome = habilidades[hab_escolha-1]
                        
                        # Verificar se a habilidade já foi usada
                        if hab_nome in habilidades_usadas:
                            print(f"Você já usou {hab_nome} nesta batalha e não pode usá-la novamente!")
                        else:
                            print(heroi.usar_habilidade(hab_nome, vilao))
                            # Marcar a habilidade como usada
                            habilidades_usadas.add(hab_nome)
                    else:
                        print("Habilidade inválida!")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Você não possui habilidades!")
        elif escolha == 5:  # Ataque heroico
            print(heroi.ataque_heroico(vilao))
        elif escolha == 6:  # Inspirar
            print(heroi.inspirar())
        
        pausar(1)
        
        # Verificar se o vilão ainda está vivo
        if not vilao.esta_vivo():
            break
        
        # Turno do vilão
        print(f"\nÉ o turno de {vilao.nome}!")
        pausar(1)
        
        # Lógica para o vilão escolher sua ação
        if vilao.vida < vilao.vida_maxima * 0.3:
            # Vilão está com pouca vida, mais chances de usar habilidades fortes
            if len(vilao.habilidades) > 0:
                habilidade = list(vilao.habilidades.keys())[1]  # Usa a segunda habilidade, mais forte
                print(vilao.usar_habilidade(habilidade, heroi))
            else:
                print(vilao.ataque_especial(heroi))
        elif vilao.vida < vilao.vida_maxima * 0.6:
            # Vilão com vida média, mais agressivo
            acao = turno % 3  # Alterna entre ações
            if acao == 0:
                print(vilao.atacar(heroi))
            elif acao == 1:
                print(vilao.intimidar(heroi))
            else:
                print(vilao.ataque_especial(heroi))
        else:
            # Vilão com vida alta, mais estratégico
            acao = turno % 4  # Mais variedade de ações
            if acao == 0:
                print(vilao.atacar(heroi))
            elif acao == 1:
                if len(vilao.habilidades) > 0:
                    habilidade = list(vilao.habilidades.keys())[0]  # Usa a primeira habilidade
                    print(vilao.usar_habilidade(habilidade, heroi))
                else:
                    print(vilao.atacar(heroi))
            elif acao == 2:
                print(vilao.intimidar(heroi))
            else:
                print(vilao.rir_malignamente())
        
        pausar(2)
        turno += 1
    
    # Verificar resultado da batalha
    if not heroi.esta_vivo():
        print(f"\n{vilao.nome} derrotou {heroi.nome}!")
        print(vilao.dialogar("HAHAHA! Eu disse que você não poderia me derrotar!"))
        return False
    else:
        print(f"\n{heroi.nome} derrotou {vilao.nome}!")
        print(heroi.dialogar("A luz sempre vence a escuridão!"))
        
        # Salvar a princesa
        print(heroi.salvar_refem(vilao, "Zelda"))
        heroi.nivel_heroismo += 2
        print(f"Nível de heroísmo aumentado para {heroi.nivel_heroismo}!")
        
        input("\nPressione ENTER para continuar...")
        return True

def ver_inventario(heroi):
    """Exibe o inventário do herói"""
    limpar_tela()
    mostrar_titulo("INVENTÁRIO")
    
    if heroi.inventario:
        print("Itens:")
        for i, item in enumerate(heroi.inventario, 1):
            print(f"{i}. {item}")
    else:
        print("Inventário vazio!")
    
    if heroi.habilidades:
        print("\nHabilidades:")
        for hab, poder in heroi.habilidades.items():
            print(f"- {hab} (Poder: {poder})")
    
    print(f"\nPoções de cura: {heroi.pocoes}")
    print(f"Pessoas salvas: {', '.join(heroi.pessoas_salvas) if heroi.pessoas_salvas else 'Nenhuma'}")
    
    input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()