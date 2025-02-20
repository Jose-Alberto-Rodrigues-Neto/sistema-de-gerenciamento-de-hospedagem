from checkin import checkin
from checkout import checkout

lista_checkin = checkin.lista_checkin
lista_agendamentos = checkin.lista_agendamentos
lista_checkout = checkout.lista_checkout

# mostra usuários alocados em quartos do hotel
def mostrar_dashboard_checkin():
    return

# mostra usuários que não estão mais no hotel
def mostrar_dashboard_checkout():
    return

def mostrar_dashboard_agendamentos():
    return

def menu():
    return
    
def mostrar_dashboard_historico():
    if not lista_checkout:
        print("Nenhum hóspede realizou check-out ainda.")
        return
    print("=== Histórico de Hóspedes que Fizeram Check-Out ===")
    for hospede in lista_checkout:
        print(f"Nome: {hospede['nome']}, Quarto: {hospede['numero_quarto']}, Check-in: {hospede['data_entrada'].strftime('%d-%m-%Y')}, Check-out: {hospede['data_saida'].strftime('%d-%m-%Y')}")