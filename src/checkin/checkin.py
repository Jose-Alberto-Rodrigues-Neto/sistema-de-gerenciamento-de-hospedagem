import datetime

valor_dia = 0.0 #valor em reais, precisa ser iniciado assim que o programa é iniciado
total_quartos = 0 #valor em inteiros

lista_checkin = [] #lista de hospedes hospedados no momento
lista_agendamentos = [] #lista de agendamentos

def quartos_livres (lista_checkin, total_quartos):
    numero_quarto=0
    nenhum_livre = True
    
    while numero_quarto < total_quartos:
        if lista_checkin[numero_quarto] is None:
            print(f"Quarto {numero_quarto} está livre.")
            nenhum_livre = False  
        numero_quarto += 1  
    
    if nenhum_livre:
        print(" Todos estão ocupados.")
# cria um dicionário de hospede
def criar_novo_hospede(nome: str, numero_quarto: int, data_entrada: datetime.datetime, data_saida: datetime.datetime, status_hospedagem: bool) -> dict:
    novo_hospede = {
        "nome": nome, 
        "numero_quarto": numero_quarto, 
        "data_entrada": data_entrada, 
        "data_saida" : data_saida, 
        "status_hospedagem": status_hospedagem
    }
    return novo_hospede

#adiciona o hospede na lista de check-in
def fazer_checkin(lista_checkin: list) -> None:
    nome = input("Adicione o nome do hospede que vai ser hospedado: ")
    numero_quarto = input("Adicione o número do quarto que o usuário vai ser hospedado: ")
    if(numero_quarto > total_quartos):
        print("Não temos esse quarto em nosso hotel! Os quartos livres estão abaixo:")
        quartos_livres(lista_checkin, total_quartos)
        numero_quarto = input("Escolha o número do quarto: ")

    # Verificar se o quarto está com hospede no momento
    # Caso tenha, perguntar se quer fazer um agendamento
    data_entrada = input("Adicione a data em que o hospede irá fazer check-in: ")
    data_saida = input("Adicione a data em que o hospede irá fazer check-out: ")
    status_hospedagem = True
    
    novo_hospede = criar_novo_hospede(nome, numero_quarto, data_entrada, data_saida, status_hospedagem)

    #verifica se o hotel tem algum hospede
    if len(lista_checkin) == 0:
        lista_checkin[numero_quarto] = novo_hospede
        return

    #verifica se tem algum hospede hospedado no quarto
    for hospede in lista_checkin:
        if novo_hospede["numero_quarto"] == numero_quarto:
            print(f"Erro: o novo hospede não pode ser alocado no quarto {novo_hospede['numero_quarto']}, pois o quarto já tem o hospede {hospede['nome']} alocado!")
            return
        
    lista_checkin[numero_quarto] = novo_hospede

def fazer_agendamento() -> None:
    nome = input("Adicione o nome do hospede que vai ser hospedado: ")
    numero_quarto = input("Adicione o número do quarto que o usuário vai ser hospedado: ")
    data_entrada = input("Adicione a data em que o hospede irá fazer check-in: ")
    # Verificar se existe algum agendamento no mesmo quarto com a mesma data
    # Caso tenha algum agendamento na mesma data, mostrar a próxima data possível criar um agendamento
    data_saida = input("Adicione a data em que o hospede irá fazer check-out: ")
    status_hospedagem = False

    novo_agendamento = criar_novo_hospede(nome, numero_quarto, data_entrada, data_saida, status_hospedagem)

    lista_agendamentos.append(novo_agendamento) # Cria agendamento
