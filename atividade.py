class ContaBancaria:
    def _init_(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo:.2f}")

ContaBancaria()

ContaBancaria.depositar(1000)
ContaBancaria.ver_saldo()

ContaBancaria.sacar(500)
ContaBancaria.ver_saldo()

ContaBancaria.sacar(800)
ContaBancaria.ver_saldo()