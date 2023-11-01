class ContaBancaria:
    def __init__(self,numero,nome,tipo):
        self.numero = numero
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.status = 0
        self.limite = 0
        self.StatusConta = False
        self.ativa = False
        self.desativa = False

    def depositar(self,deposito):
        if self.StatusConta == True:

            if deposito > 0:
                self.saldo = deposito - self.limite
                print(f"Deposito de R${deposito} concluído. Saldo atual é de R${self.saldo}")
            else:
                print(f"Valor inválido.")
        else:
            print("CONTA DESATIVADA,IMPOSSIVEL FAZER DEPOSITO")

    def sacar(self,saque):
        if self.StatusConta ==True:
          if saque > 0 and saque <= self.saldo + self.limite:
                    self.limite = self.saldo - (saque - self.limite)
                    self.saldo = self.saldo - saque
                    print(f"Seu saque de R${saque} foi concluido com sucesso.")
          elif saque > self.limite:
                print(f"SEU LIMITE É R${self.limite},E VOCE NAO PODE ULTRAPASSAR.")
          else:
                print("Você não possui saldo suficiente.")
        else:
            print("Conta desativada, impossível sacar.")


    def ativarConta(self):
        if self.StatusConta == False:
            self.ativa = True
            self.StatusConta = True
            print("Conta ativada.")
        else:
            print("Já está ativada.")

    def desativarConta(self):
        if self.saldo > 0:
            print("CONTA SÓ PODE SER DESATIVADA COM SALDO ZERADO")
        elif self.StatusConta == True:
            self.desativa == True
            self.StatusConta == False
            self.ativa = False
            print("CONTA FOI DESATIVADA")
        else:
            print("CONTA JA ESTA DESATIVADA")

    def verificarSaldo(self):
            print(f"SALDO DA CONTA: R${self.saldo}\nLIMITE R${self.limite}")

    def AtivarLimite (self,valor):
        self.limite = valor
        print (f"SEU CREDITO ESPECIAL É DE R${self.limite}")
    def DesativarLimite (self):
        self.limite = 0
        print (f"SEU CREDITO ESPECIAL É DE R${self.limite}")