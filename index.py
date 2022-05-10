import os
import time
import requests
import wikipedia
import json
import webbrowser
from dev import DEV, version
from colorama import Fore as color
from pesquisa import pesquisara

site = "https://github.com"

errormsg = "Error 604 - Algo deu errado! Voltando em 5 segundos"

dev = DEV
versao = version

result = os.environ['COMPUTERNAME']
bannerinicial = f"""
{color.LIGHTRED_EX}
   _____ _             _    _______          _ 
  / ____| |           | |  |__   __|        | |
 | (___ | |_ _   _  __| |_   _| | ___   ___ | |
  \___ \| __| | | |/ _` | | | | |/ _ \ / _ \| |
  ____) | |_| |_| | (_| | |_| | | (_) | (_) | |
 |_____/ \__|\__,_|\__,_|\__, |_|\___/ \___/|_|
                          __/ |                
                         |___/                 
{color.RESET}

Criador: {dev}
Versão: {versao}

"""

#Menu inicial 🏡

def menu():
    os.system('cls')
    print(f"Você está conectado em {result}")
    print(bannerinicial)
    print("- 1 - Consulta Google")
    print("- 2 - Calculadora")
    print("- 3 - Wikipedia")
    print("- 4 - Pesquisa Google")
    inputini = input('Escolha algum: ')
    if inputini == "1" or inputini == "01":
        consultagoogle()
    if inputini == "2":
        calculadora()
    if inputini == "3":
        wikipedia()
    if inputini == "4":
        pesquisa_google()
    else:
        print(errormsg)
        time.sleep(5)
        menu()

# Configurações

def consultagoogle():
    os.system('cls')
    new=2
    site =str(input('Digite um site (nome do site + dominio (.com, .com.br, .co)): '))
    url="https://www."+site+"/"
    webbrowser.open(url,new=new)
    os.system('cls')
    menu()

# Calculadora

def calculadora():
    print("Você deseja subitrair, somar, dividir ou multiplicar?")
    print("Subtração: sub | Multiplicação: mult | Adição: adic | Divisão: div")
    calc = input('[Escolha um]:')
    if calc == "sub":
        os.system('cls')
        subi()
    if calc == "mult":
        os.system('cls')
        multi()
    if calc == "adic":
        os.system('cls')
        adicao()
    if calc == "div":
        os.system('cls')
        divi()
    else:
        print(errormsg)
        time.sleep(5)
        menu()


# Calculadora

def subi():
    inputsub = int(input('Escolha o primeiro número para subitrair: '))
    inputsub2 = int(input('Escolha o segundo número para subitrair: '))
    resultadosub = inputsub - inputsub2
    print(f"O resultado é: {resultadosub}")
    time.sleep(5)
    menu()

def multi():
    inputmulti = int(input('Escolha o primeiro número para multiplicar: '))
    inputmulti2 = int(input('Escolha o segundo número para multiplicar: '))
    resultadomulti = inputmulti * inputmulti2
    print(f"O resultado é: {resultadomulti}")
    time.sleep(5)
    menu()

def adicao():
    inputadi = int(input('Escolha o primeiro número para somar: '))
    inputadi2 = int(input('Escolha o segundo número para somar: '))
    resultadoadi = inputadi + inputadi2
    print(f"O resultado é: {resultadoadi}")
    time.sleep(5)
    menu()

def divi():
    inputdiv = int(input('Escolha o primeiro número para dividir: '))
    inputdiv2 = int(input('Escolha o segundo número para dividir: '))
    resultdiv = inputdiv / inputdiv2
    print(f"O resultado é: {resultdiv}")
    time.sleep(5)
    menu()

# Pesquisa

def wikipedia():
    palavra = input('O que você deseja pesquisar?\n>>')
    pesquisara(palavra)

def pesquisa_google():
		word = input('Fale oque deseja pesquisar \n>>')
		tete = requests.get(f'https://kgsearch.googleapis.com/v1/entities:search?query={word}&key=AIzaSyAkSdDu4hAB8I0hH9ub6w05JSLUY6l94Gw&limit=1&indent=True&languages=pt').json() # Puxando os dados apartir da API
		try:
				jo = tete['itemListElement'][0]['result']
		except:
				pass
		os.system('clear')
		# resultados
		print("-== Google ==-")
		try:
				print('Nome:', jo['name'])
				print('Detalhes:', jo['detailedDescription']['articleBody'])
				print('Sobre:',jo['description'])
				print('Links', jo['detailedDescription']['url'])
				print('Tipo da resposta(Em inglês):')
				print(jo['@type'][0])
		except:
			menu()

menu()