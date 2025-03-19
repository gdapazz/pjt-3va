from personagem import Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, ataque=10, defesa=8):
        super().__init__(nome, idade, vida, ataque, defesa)
        self.pocoes = 3
        self.pessoas_salvas = []
        self.nivel_heroismo = 1
        
    def usar_pocao(self):
        """
        Usa uma poção para recuperar vida.
        """
        if self.pocoes > 0:
            self.pocoes -= 1
            recuperacao = 30
            self.vida = min(self.vida_maxima, self.vida + recuperacao)
            mensagem = f'{self.nome} usou uma poção e recuperou {recuperacao} pontos de vida! Poções restantes: {self.pocoes}'
            self.registrar_acao(mensagem)
            return mensagem
        else:
            mensagem = f'{self.nome} não tem mais poções!'
            self.registrar_acao(mensagem)
            return mensagem
    
    def salvar_refem(self, vilao, refem):
        """
        Herói tenta salvar um refém de um vilão.
        """
        if refem in vilao.refens:
            vilao.refens.remove(refem)
            self.pessoas_salvas.append(refem)
            self.nivel_heroismo += 1
            mensagem = f'{self.nome} salvou {refem} das garras de {vilao.nome}!'
            self.registrar_acao(mensagem)
            return mensagem
        else:
            mensagem = f'{refem} não está entre os reféns de {vilao.nome}.'
            self.registrar_acao(mensagem)
            return mensagem
    
    def ataque_heroico(self, alvo):
        """
        Realiza um ataque poderoso baseado no nível de heroísmo.
        """
        dano = self.ataque + (self.nivel_heroismo * 2)
        alvo.receber_dano(dano)
        mensagem = f'{self.nome} realizou um ATAQUE HEROICO em {alvo.nome} causando {dano} de dano!'
        self.registrar_acao(mensagem)
        return mensagem
    
    def inspirar(self):
        """
        Herói faz um discurso inspirador, aumentando seu ataque.
        """
        bonus = 3 + self.nivel_heroismo
        self.ataque += bonus
        mensagem = f'{self.nome} faz um discurso inspirador! (+{bonus} de ataque)'
        self.registrar_acao(mensagem)
        return mensagem
    
    def adquirir_pocao(self, quantidade=1):
        """
        Herói adquire poções de cura.
        """
        self.pocoes += quantidade
        mensagem = f'{self.nome} adquiriu {quantidade} poção(ões). Total: {self.pocoes}'
        self.registrar_acao(mensagem)
        return mensagem
    
    def __str__(self):
        return f'Herói: {self.nome}, Idade: {self.idade}, Vida: {self.vida}/{self.vida_maxima}, Ataque: {self.ataque}, Defesa: {self.defesa}, Poções: {self.pocoes}, Nível de Heroísmo: {self.nivel_heroismo}'