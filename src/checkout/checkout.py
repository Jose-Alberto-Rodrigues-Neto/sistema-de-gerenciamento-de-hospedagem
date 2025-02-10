from checkin import checkin

lista_checkout = []

hospede1 = {
    "nome": "João",
    "quarto": 101,
    "data_entrada": "05/05/2022",
    "data_saida": "10/05/2022"
}

# Add the guest to the check-in list
checkin.lista_checkin.append(hospede1)

# Room number of the guest to check out
quarto_hospede = 101

#função para tirar o hospede da lista de hospedes e adicinar na lista de checkout
def fazer_checkout(quarto_hospede: int) -> None:
    #caso 1: não há hospedes
    if len(checkin.lista_checkin) == 0:
        print("Não existe hospedes no hotel")


    # Procurar o hospede na lista de check-in e retira-lo da lista
    aux = None #variavel auxiliar para guardar o hospede a ser retirado da lista de checkin
    for hospede in checkin.lista_checkin:
        if hospede['quarto'] == quarto_hospede:
            aux = hospede
            checkin.lista_checkin.remove(hospede)
            break
    ####
    
    # Printar valor pago na hospedagem total
    valor_pago = calcular_estadia(aux)
    
    print(f"Total pago pelo hospede{aux['nome']} foi R${valor_pago}.")

    # Alocar ele na lista de Check-Out
    lista_checkout.append(aux) #adicionar o hospede a ser alocado na lista de checkout


def calcular_estadia(hospede: dict) -> float:
    ##calcular estadia
    valor_diaria = 100.0 #valor da diaria (Não especificado na elicitação de requisitos)
    data_saida = int(hospede["data_saida"].split("/")[0]) ## seleciona apenas o dia, considerando o formato DD/MM/AAAA
    data_entrada = int(hospede["data_entrada"].split("/")[0])

    valor_pago = float((data_saida - data_entrada) * valor_diaria)
    return valor_pago #retornar valor em float