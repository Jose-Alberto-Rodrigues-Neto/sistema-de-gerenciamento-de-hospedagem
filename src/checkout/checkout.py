from checkin import checkin
lista_checkout = []

#função para tirar o hospede da lista de hospedes e adicinar na lista de checkout
def fazer_checkout(nome_hospede, quarto_hospede):
    if len(checkin.lista_checkin) == 0:
        print("Não existe hospedes no hotel")
    
    # Procurar o hospede na lista de check-in e retira-lo da lista
    ####

    # Printar valor pago na hospedagem total
    valor_pago = calcular_estadia(hospede)
    print(f"Total pago pelo hospede{hospede["nome"]} foi R${valor_pago}.")

    # Alocar ele na lista de Check-Out
    lista_checkout.append() #adicionar o hospede a ser alocado na lista de checkout


def calcular_estadia(hospede):
    ##calcular estadia
    return 0.0 #retronar valor em double