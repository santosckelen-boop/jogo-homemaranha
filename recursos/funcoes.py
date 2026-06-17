import os, time
import json
from datetime import datetime
import pyttsx3


def limpar_tela():
    os.system("cls")
    

def aguarde(segundos):
    time.sleep(segundos)
    

def inicializarBancoDeDados():
    # r - read, w - write, a - append
    try:
        banco = open("log.dat", "r")
        banco.close()
    except:
        print("Banco de Dados Inexistente. Criando...")
        banco = open("log.dat", "w")
        banco.close()
    

def escreverDados(nome, pontos):
    # INI - inserindo no arquivo
    banco = open("log.dat", "r")
    dados = banco.read()
    banco.close()

    print("dados", type(dados))

    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}
        
    data_br = datetime.now().strftime("%d/%m/%Y")
    hora_br = datetime.now().strftime("%H:%M:%S")

    dadosDict[nome] = (pontos, data_br, hora_br)
    
    banco = open("log.dat", "w")
    banco.write(json.dumps(dadosDict))
    banco.close()


def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()