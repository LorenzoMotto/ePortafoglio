class Conto:
    def __init__(self, soldi,pin):
        self.soldi = soldi
        self.pin = pin

    def getPin(self):
        return self.pin
    def getSoldi(self):
        return self.soldi
    def transfer(self):
        if int (input("Inserire il PIN: "))== self.pin:
            s = input("Selezionare importo: ")
            if int(s) > self.soldi:
                print("Transazione fallita, saldo insufficiente.")
            else:
                print("Transazione completata")
                self.soldi= self.soldi - int(s)
                print("Importo restante: $ " + str(self.soldi))
        else:
            print("Pin Errato")



if __name__ == "__main__":
    Utente = Conto(25000, 0000)
    Utente.transfer()
