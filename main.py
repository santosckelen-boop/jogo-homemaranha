import pygame
import random
import os
import tkinter as tk
from tkinter import messagebox
from recursos.funcoes import inicializarBancoDeDados, escreverDados
import json
from recursos.novaFuncao import aranha_pulsante, boas_vindas
import pyttsx3


pygame.init()
inicializarBancoDeDados()

tamanho = (1000, 700)
relogio = pygame.time.Clock()

tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Jogo Kélen")

icone = pygame.image.load("assets/aranha.png")
pygame.display.set_icon(icone)

branco = (255, 255, 255)
preto = (0, 0, 0)

homemaranha = pygame.image.load("assets/homemaranha.png")
fundoStart = pygame.image.load("assets/fundoStart.jpg")
fundoJogo = pygame.image.load("assets/fundoJogo.jpg")
fundoDead = pygame.image.load("assets/fundoDead.jpg")
bomba = pygame.image.load("assets/bombas.png")
aranha_base = pygame.image.load("assets/aranha.png").convert_alpha()

lançarSound = pygame.mixer.Sound("assets/lançar.mp3")
explosaoSound = pygame.mixer.Sound("assets/explosao.mp3")

fonteMenu = pygame.font.SysFont("comicsans", 18)
fonteMorte = pygame.font.SysFont("arial", 120)

pygame.mixer.music.load("assets/sound.mp3")


def falar(texto):
    try:
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
    except:
        print("Não foi possível executar a fala do computador.")


def jogar():
    largura_janela = 300
    altura_janela = 50

    def obter_nome():
        global nome
        nome = entry_nome.get()

        if not nome:
            messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
        else:
            root.destroy()

    root = tk.Tk()

    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2

    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    root.title("Informe seu nickname")
    root.protocol("WM_DELETE_WINDOW", obter_nome)

    entry_nome = tk.Entry(root)
    entry_nome.pack()

    botao = tk.Button(root, text="Enviar", command=obter_nome)
    botao.pack()

    root.mainloop()

    boas_vindas(nome)

    posicaoXPersona = 500
    posicaoYPersona = 500
    movimentoXPersona = 0

    posicaoXBombas = 400
    posicaoYBombas = -240
    velocidadeBombas = 1

    brilho_img = pygame.image.load("assets/teia.png").convert_alpha()
    brilho_pos = [random.randint(0, 950), random.randint(0, 650)]
    brilho_vel = [random.choice([-1, 1]), random.choice([-1, 1])]
    brilho_tamanho = brilho_img.get_size()

    pygame.mixer.Sound.play(lançarSound)
    pygame.mixer.music.play(-1)

    pontos = 0
    em_pausa = False

    larguraPersona = 80
    alturaPersona = 200

    larguraBombas = 50
    alturaBombas = 250

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 15

            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -15

            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0

            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0

            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                em_pausa = not em_pausa

        posicaoXPersona = posicaoXPersona + movimentoXPersona

        if posicaoXPersona < 0:
            posicaoXPersona = 15
        elif posicaoXPersona > 920:
            posicaoXPersona = 910

        tela.fill(branco)
        tela.blit(fundoJogo, (0, 0))

        aranha_pulsante(tela, aranha_base)

        tela.blit(homemaranha, (posicaoXPersona, posicaoYPersona))

        posicaoYBombas = posicaoYBombas + velocidadeBombas

        if posicaoYBombas > 600:
            posicaoYBombas = -240
            pontos = pontos + 1
            velocidadeBombas = velocidadeBombas + 1
            posicaoXBombas = random.randint(0, 800)
            pygame.mixer.Sound.play(lançarSound)

        tela.blit(bomba, (posicaoXBombas, posicaoYBombas))

        texto = fonteMenu.render("Pontos: " + str(pontos), True, branco)
        tela.blit(texto, (15, 15))

        mensagem_pausa = fonteMenu.render("Press Space to Pause Game", True, branco)
        tela.blit(mensagem_pausa, (150, 15))

        os.system("cls")

        personagemRect = pygame.Rect(
            posicaoXPersona,
            posicaoYPersona,
            larguraPersona,
            alturaPersona
        )

        bombaRect = pygame.Rect(
            posicaoXBombas,
            posicaoYBombas,
            larguraBombas,
            alturaBombas
        )

        if personagemRect.colliderect(bombaRect):
            escreverDados(nome, pontos)
            dead()
            return
        else:
            print("Ainda Vivo")

        brilho_pos[0] += brilho_vel[0]
        brilho_pos[1] += brilho_vel[1]

        if brilho_pos[0] <= 0 or brilho_pos[0] + brilho_tamanho[0] >= 1000:
            brilho_vel[0] *= -1

        if brilho_pos[1] <= 0 or brilho_pos[1] + brilho_tamanho[1] >= 700:
            brilho_vel[1] *= -1

        tela.blit(brilho_img, brilho_pos)

        if em_pausa:
            tela.fill(branco)
            tela.blit(fundoJogo, (0, 0))

            texto_pause = fonteMorte.render("PAUSE", True, branco)
            rect = texto_pause.get_rect(center=(tamanho[0] // 2, tamanho[1] // 2))
            tela.blit(texto_pause, rect)

            texto = fonteMenu.render("Pontos: " + str(pontos), True, branco)
            tela.blit(texto, (15, 15))

            mensagem_pausa = fonteMenu.render("Press Space to Pause Game", True, branco)
            tela.blit(mensagem_pausa, (150, 15))

            pygame.display.update()
            relogio.tick(10)
            continue

        pygame.display.update()
        relogio.tick(60)


def start():
    larguraButtonStart = 150
    alturaButtonStart = 40

    larguraButtonQuit = 150
    alturaButtonQuit = 40

    startButton = pygame.Rect(10, 10, larguraButtonStart, alturaButtonStart)
    quitButton = pygame.Rect(10, 60, larguraButtonQuit, alturaButtonQuit)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart = 35

                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 140
                    alturaButtonQuit = 35

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 150
                    alturaButtonStart = 40
                    jogar()

                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 150
                    alturaButtonQuit = 40
                    pygame.quit()
                    quit()

        tela.fill(branco)
        tela.blit(fundoStart, (0, 0))

        startButton = pygame.draw.rect(
            tela,
            branco,
            (10, 10, larguraButtonStart, alturaButtonStart),
            border_radius=15
        )

        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (25, 12))

        quitButton = pygame.draw.rect(
            tela,
            branco,
            (10, 60, larguraButtonQuit, alturaButtonQuit),
            border_radius=15
        )

        quitTexto = fonteMenu.render("Sair do Game", True, preto)
        tela.blit(quitTexto, (25, 62))

        pygame.display.update()
        relogio.tick(60)


def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)

    larguraButtonStart = 150
    alturaButtonStart = 40

    larguraButtonQuit = 150
    alturaButtonQuit = 40

    falou_game_over = False

    try:
        with open("log.dat", "r") as arquivo:
            registros = json.load(arquivo)
    except:
        registros = {}

    lista_registros = [
        (nickname, info[0], info[1], info[2])
        for nickname, info in registros.items()
    ]

    ultimos_registros = lista_registros[-5:] if len(lista_registros) > 5 else lista_registros

    startButton = pygame.Rect(10, 10, larguraButtonStart, alturaButtonStart)
    quitButton = pygame.Rect(10, 60, larguraButtonQuit, alturaButtonQuit)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart = 35

                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 390
                    alturaButtonQuit = 35

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 150
                    alturaButtonStart = 40
                    jogar()
                    return

                if quitButton.collidepoint(evento.pos):
                    pygame.quit()
                    quit()

        tela.fill(branco)
        tela.blit(fundoDead, (0, 0))

        texto_game_over = fonteMorte.render("GAME OVER", True, branco)
        rect_game_over = texto_game_over.get_rect(center=(tamanho[0] // 2, 180))
        tela.blit(texto_game_over, rect_game_over)

        startButton = pygame.draw.rect(
            tela,
            branco,
            (10, 10, larguraButtonStart, alturaButtonStart),
            border_radius=15
        )

        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (25, 12))

        quitButton = pygame.draw.rect(
            tela,
            branco,
            (10, 60, larguraButtonQuit, alturaButtonQuit),
            border_radius=15
        )

        quitTexto = fonteMenu.render("Sair do Game", True, preto)
        tela.blit(quitTexto, (25, 62))
        
        titulo = fonteMenu.render("Últimos Registros:", True, branco)
        tela.blit(titulo, (25, 300))

        for i, (nome, pontos, data, hora) in enumerate(reversed(ultimos_registros)):
            texto = f"{i + 1}. {nome} - {pontos} pts em {data} às {hora}"
            linha = fonteMenu.render(texto, True, branco)
            tela.blit(linha, (25, 340 + i * 30))

        pygame.display.update()

        relogio.tick(60)


start()