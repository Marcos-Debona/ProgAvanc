class Cartao():
    def __init__(self,b,c,d):
        self.cardIdentifier = b
        self.senhaDoCartao = c
        self.saldoCartao = d

    def senhaCartao(self):
        return self.senhaDoCartao
    def identifier(self):
        return self.cardIdentifier
    def saldo(self):
        return self.saldoCartao
