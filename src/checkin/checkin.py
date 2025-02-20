import datetime

valor_diaria = 0.0 #valor em reais, precisa ser iniciado assim que o programa é iniciado
total_quartos = 0 #valor em inteiros

lista_checkin = [] #lista de hospedes hospedados no momento
lista_agendamentos = [] #lista de agendamentos

def popular_listas(total_quartos: int, lista: list):
    for i in range(total_quartos):
        lista.append(None)

def mostrar_quartos_livres(lista_checkin, total_quartos):
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

#Verifica se a data está disponível para o hóspede se hospedar.
def verificar_agendamento_na_data(numero_quarto: int, data_desejada: datetime.datetime) -> bool:
   
    for agendamento in lista_agendamentos:
        if agendamento["numero_quarto"] == numero_quarto:
     
            if agendamento["data_entrada"] <= data_desejada < agendamento["data_saida"]:
                return True  
    return False  

    data_desejada = datetime.datetime.strptime("15-02-2025", "%d-%m-%Y")

#adiciona o hospede na lista de check-in
def fazer_checkin(lista_checkin: list) -> None:
    nome = input("Adicione o nome do hospede que vai ser hospedado: ")
    numero_quarto = input("Adicione o número do quarto que o usuário vai ser hospedado: ")
    if(numero_quarto > total_quartos):
        print("Não temos esse quarto em nosso hotel! Os quartos livres estão abaixo:")
        mostrar_quartos_livres(lista_checkin, total_quartos)
        numero_quarto = input("Escolha o número do quarto: ")
    if lista_checkin[quarto_numero-1] is not None:
        print("quarto indisponível no momento, gostaria de fazer agendamento?")
    resp = input()
    if resp.lower() == "sim":
        fazer_agendamento()
        return
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
    if verificar_agendamento_na_data(numero_quarto, data_desejada):
        print(f"Quarto {numero_quarto} já está reservado para a data {data_desejada.strftime('%d-%m-%Y')}.")
        # TODO
        # Caso tenha algum agendamento na mesma data, mostrar a próxima data possível criar um agendamento
    else:
        print(f"Quarto {numero_quarto} está disponível para a data {data_desejada.strftime('%d-%m-%Y')}.")
        
    data_saida = input("Adicione a data em que o hospede irá fazer check-out: ")
    status_hospedagem = False

    novo_agendamento = criar_novo_hospede(nome, numero_quarto, data_entrada, data_saida, status_hospedagem)

    lista_agendamentos.append(novo_agendamento) # Cria agendamento

