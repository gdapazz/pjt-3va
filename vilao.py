from personagem import Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa um antagonista no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, ataque=12, defesa=5):
        super().__init__(nome, idade, vida, ataque, defesa)
        self.refens = []
        self.bases_secretas = []
        
    def rir_malignamente(self):
        """
        Vilão ri malignamente.
        """
        mensagem = f"{self.nome}: 'MUAHAHAHAHA! O MUNDO SERÁ MEU!'"
        self.registrar_acao(mensagem)
        return mensagem
    
    def intimidar(self, alvo):
        """
        Vilão tenta intimidar um alvo, reduzindo sua defesa.
        """
        reducao = 2
        alvo.defesa = max(0, alvo.defesa - reducao)
        mensagem = f"{self.nome} intimida {alvo.nome}, reduzindo sua defesa em {reducao}!"
        self.registrar_acao(mensagem)
        return mensagem
    
    def ataque_especial(self, alvo):
        """
        Vilão realiza um ataque especial mais poderoso.
        """
        dano = self.ataque * 1.5
        alvo.receber_dano(dano)
        mensagem = f"{self.nome} realiza um ATAQUE ESPECIAL em {alvo.nome} causando {dano} de dano!"
        self.registrar_acao(mensagem)
        return mensagem
    
    def capturar_refem(self, refem):
        """
        Vilão captura um refém.
        """
        self.refens.append(refem.nome)
        mensagem = f"{self.nome} capturou {refem.nome} como refém!"
        self.registrar_acao(mensagem)
        return mensagem
    
    def criar_base_secreta(self, nome_base):
        """
        Vilão cria uma nova base secreta.
        """
        self.bases_secretas.append(nome_base)
        mensagem = f"{self.nome} estabeleceu uma base secreta em {nome_base}!"
        self.registrar_acao(mensagem)
        return mensagem
    
    def __str__(self):
        return f"Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}/{self.vida_maxima}, Ataque: {self.ataque}, Defesa: {self.defesa}"