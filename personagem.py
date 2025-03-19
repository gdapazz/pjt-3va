class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, idade, vida, ataque=0, defesa=0):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.vida_maxima = vida  # Adicionando vida_maxima para referência
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = []
        self.habilidades = {}
        self.historico = []

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        self.vida_maxima += incremento  # Atualizando vida_maxima também
        print(f'Vida de {self.nome} após upgrade: {self.vida}')

    def downgrade_vida(self):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > 15:
            self.vida -= 15
        else:
            self.vida = 0
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def atacar(self, alvo):
        """
        Personagem ataca um alvo.
        """
        dano = max(1, self.ataque - alvo.defesa // 2)
        alvo.receber_dano(dano)
        mensagem = f'{self.nome} atacou {alvo.nome} causando {dano} de dano!'
        self.registrar_acao(mensagem)
        return mensagem

    def defender(self):
        """
        Personagem assume postura defensiva.
        """
        bonus_defesa = 2
        self.defesa += bonus_defesa
        mensagem = f'{self.nome} assumiu postura defensiva! (+{bonus_defesa} de defesa)'
        self.registrar_acao(mensagem)
        return mensagem

    def receber_dano(self, dano):
        """
        Personagem recebe dano.
        """
        dano_real = max(1, dano - self.defesa // 2)
        self.vida -= dano_real
        if self.vida < 0:
            self.vida = 0
        mensagem = f'{self.nome} recebeu {dano_real} de dano! Vida atual: {self.vida}'
        self.registrar_acao(mensagem)
        return mensagem

    def esta_vivo(self):
        """
        Verifica se o personagem ainda está vivo.
        """
        return self.vida > 0

    def dialogar(self, mensagem):
        """
        Personagem fala uma mensagem.
        """
        dialogo = f'{self.nome}: "{mensagem}"'
        self.registrar_acao(dialogo)
        return dialogo

    def adicionar_item(self, item):
        """
        Adiciona um item ao inventário do personagem.
        """
        self.inventario.append(item)
        mensagem = f'{self.nome} adquiriu {item}!'
        self.registrar_acao(mensagem)
        return mensagem

    def adicionar_habilidade(self, nome_habilidade, poder):
        """
        Adiciona uma nova habilidade ao personagem.
        """
        self.habilidades[nome_habilidade] = poder
        mensagem = f'{self.nome} aprendeu a habilidade {nome_habilidade}!'
        self.registrar_acao(mensagem)
        return mensagem

    def usar_habilidade(self, nome_habilidade, alvo=None):
        """
        Usa uma habilidade específica.
        """
        if nome_habilidade in self.habilidades:
            poder = self.habilidades[nome_habilidade]
            if alvo:
                alvo.receber_dano(poder)
                mensagem = f'{self.nome} usou {nome_habilidade} em {alvo.nome} causando {poder} de dano!'
            else:
                mensagem = f'{self.nome} usou {nome_habilidade}!'
            self.registrar_acao(mensagem)
            return mensagem
        else:
            mensagem = f'{self.nome} não possui a habilidade {nome_habilidade}!'
            self.registrar_acao(mensagem)
            return mensagem

    def registrar_acao(self, mensagem):
        """
        Registra uma ação no histórico do personagem.
        """
        self.historico.append(mensagem)

    def mostrar_historico(self):
        """
        Exibe o histórico de ações do personagem.
        """
        print(f"\nHistórico de {self.nome}:")
        for i, acao in enumerate(self.historico, 1):
            print(f"{i}. {acao}")

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}/{self.vida_maxima}, Ataque: {self.ataque}, Defesa: {self.defesa}'