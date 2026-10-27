# CLIENTE E VEIULOS

cientes = {}

cpf = input("CPF: ")
nome = input("Nome: ")

veiculos = []

while True:
    placa = input("Placa do veículo (ou 0 para parar): ")

    if placa == "0":
        break
    veiculos.append(placa)
print(clientes)

# ATENDIMENTO

normal = []
guincho = []

while True:
    placa = input("Placa (ou 0 para atender): ")

    if placa == "0":
        if guincho:
            print("Atendendo guincho:", guincho.pop(0))
        elif normal:
            print("Atendendo veículo:", normal.pop(0))
        else:
            print("Não há veículos na fila!")
        break

    tipo = input("Veículo normal ou guincho? (n/g): ")

    if tipo == "g":
        guincho.append(placa)
    else:
        normal.append(placa)

# ESTOQUE

estoque = {}

while True:
    peca = input("Peça (ou 0 para sair): ")

    if peca == "0":
        break

    quantidade = int(input("Quantidade: "))

    if peca in estoque:
        estoque[peca] += quantidade
    else:
        estoque[peca] = quantidade
print(estoque)

# ORDENS DE SERVIÇO

ordens = []

while True:
    placa = input("Placa do veículo (ou 0 para sair): ")

    if placa == "0":
        break

    cliente = input("Nome do cliente: ")
    servico = input("Serviço realizado: ")

    ordens.append([placa, cliente, servico])

print(ordens)

