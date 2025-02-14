from checkin.checkin import checkin, valor_dia
import datetime

lista_checkout = []

#função para tirar o hospede da lista de hospedes e adicinar na lista de checkout
def fazer_checkout(quarto_hospede: int) -> None:
    #caso 1: não há hospedes
    if len(checkin.lista_checkin) == 0:
        print("Não existe hospedes no hotel")
        return

    # Procurar o hospede na lista de check-in e retira-lo da lista
    aux = None #variavel auxiliar para guardar o hospede a ser retirado da lista de checkin
    for hospede in checkin.lista_checkin:
        if hospede['quarto'] == quarto_hospede:
            aux = hospede
            checkin.lista_checkin.remove(hospede)
            break

    if aux is None:
        print("Erro: Hospede não encontrado.")
        return
    
    # Printar valor pago na hospedagem total
    valor_pago = calcular_estadia(aux, valor_dia)
    
    print(f"Total pago pelo hospede {aux['nome']} foi R${valor_pago}.")

    # Alocar ele na lista de Check-Out
    aux["status_hospedagem"] = False
    lista_checkout.append(aux) #adicionar o hospede a ser alocado na lista de checkout

def calcular_estadia(hospede: dict, valor_dia: float) -> float:
    formato_data = "%d/%m/%Y"
    data_entrada = datetime.datetime.strptime(hospede["data_entrada"], formato_data)
    data_saida = datetime.datetime.strptime(hospede["data_saida"], formato_data)

    dias_hospedados = (data_saida - data_entrada).days
    return dias_hospedados * valor_dia