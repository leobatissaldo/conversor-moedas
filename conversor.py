import requests
from datetime import datetime

def fazer_conversao(opcao):
    resposta = requests.get("https://api.exchangerate-api.com/v4/latest/" + opcao)
    dados = resposta.json()
    print(f"1 {opcao} = R$ {dados['rates']['BRL']}")
    return dados['rates']['BRL']

def criar_arquivo(valor, moeda):
    agora = datetime.now()
    hora_formatada = agora.strftime('%Y-%m-%d %H:%M:%S')
    with open("resultado.txt", "a") as arquivo:
        arquivo.write(f"O {moeda} valia {str(valor)} em Reais no horario: {hora_formatada}")


moeda = ''

resposta_usuario = int(input("Qual moeda deseja consultar?\n1 - Dolar\n2 - Euro\n3 - Libras\n4 - Pesos\n(0 para parar)\nDigite: "))

while resposta_usuario != 0:
    match resposta_usuario:
        case 1:
            moeda = 'USD'
        case 2:
            moeda = 'EUR'
        case 3:
            moeda = 'GBP'       
        case 4:
            moeda = 'ARS'         
    moeda_convertida = fazer_conversao(moeda)
    criar_arquivo(moeda_convertida, moeda)
    resposta_usuario = int(input("Qual moeda deseja consultar?\n1 - Dolar\n2 - Euro\n3 - Libras\n4 - Pesos\n(0 para parar)\nDigite: "))
