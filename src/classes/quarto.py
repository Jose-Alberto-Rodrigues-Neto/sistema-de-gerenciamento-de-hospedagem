class Quarto:
    def __init__(self, nome, valor_dia, ocupacao_total, hospedes):
        self.nome = nome
        self.valor_dia = valor_dia
        self.ocupacao_total = ocupacao_total
        self.hospedes = hospedes
    
    def quarto_esta_cheio(self):
        return len(self.hospedes) == self.ocupacao_total #True or False

    
    def listar_hospedes(self):
        lotacao = self.quarto_esta_cheio()
        if(lotacao == False):
            print("O quarto está vazio")
            return
        print(f"O quarto {self.nome} está hospedado por:")
        for hospede in self.hospedes:
            print(hospede)