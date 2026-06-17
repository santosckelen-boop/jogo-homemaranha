import pygame
import pyttsx3
import threading


escala_aranha = 1.0
direcao_escala = 1
tamanho_tela = (1000, 700)


def aranha_pulsante(tela, aranha_base):
    global escala_aranha, direcao_escala

    LIM_INF = 0.8
    LIM_SUP = 1.0
    PASSO_ESCALA = 0.01

    escala_aranha += direcao_escala * PASSO_ESCALA

    if escala_aranha >= LIM_SUP:
        escala_aranha = LIM_SUP
        direcao_escala = -1

    elif escala_aranha <= LIM_INF:
        escala_aranha = LIM_INF
        direcao_escala = 1

    nova_largura = int(50 * escala_aranha)
    nova_altura = int(50 * escala_aranha)

    aranha_escalada = pygame.transform.smoothscale(
        aranha_base,
        (nova_largura, nova_altura)
    )

    pos_x = tamanho_tela[0] - nova_largura - 10
    pos_y = 10

    tela.blit(aranha_escalada, (pos_x, pos_y))


def boas_vindas(nome):
    branco = (255, 255, 255)
    preto = (0, 0, 0)

    tamanho = (1000, 700)
    relogio = pygame.time.Clock()

    fundoStart = pygame.image.load("assets/fundoStart.jpg")

    fonteMenu = pygame.font.SysFont("comicsans", 18)
    fonteTitulo = pygame.font.SysFont("arial", 40)
    fonteTexto = pygame.font.SysFont("comicsans", 22)

    tela = pygame.display.set_mode(tamanho)

    larguraBotao = 300
    alturaBotao = 50

    textoExplicacao = [
        "Escute as instruções com atenção."
    ]

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    botaoStart = pygame.Rect(
        tamanho[0] // 2 - larguraBotao // 2,
        400,
        larguraBotao,
        alturaBotao
    )

    def falar_mensagem():
        mensagem = """
        Use as setas do teclado para mover o personagem.
        Desvie das bombas que caem do céu.
        A cada bomba desviada, você ganha pontos.
        Pressione espaço a qualquer momento para pausar.
        Clique em começar o jogo para dar início.
        """

        engine.say(mensagem)
        engine.runAndWait()

    falou = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                engine.stop()
                pygame.quit()
                quit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botaoStart.collidepoint(evento.pos):
                    engine.stop()
                    return

        tela.fill(branco)
        tela.blit(fundoStart, (0, 0))

        titulo = fonteTitulo.render("Bem-vindo(a), " + nome + "!", True, branco)
        tela.blit(titulo, (tamanho[0] // 2 - titulo.get_width() // 2, 50))

        for i, linha in enumerate(textoExplicacao):
            texto = fonteTexto.render(linha, True, branco)
            tela.blit(texto, (tamanho[0] // 2 - texto.get_width() // 2, 150 + i * 30))

        botaoStart = pygame.draw.rect(
            tela,
            branco,
            (
                tamanho[0] // 2 - larguraBotao // 2,
                400,
                larguraBotao,
                alturaBotao
            ),
            border_radius=20
        )

        textoBotao = fonteMenu.render("Começar o Jogo", True, preto)
        tela.blit(textoBotao, (tamanho[0] // 2 - textoBotao.get_width() // 2, 415))

        pygame.display.update()
        relogio.tick(60)

        if not falou:
            thread_fala = threading.Thread(target=falar_mensagem, daemon=True)
            thread_fala.start()
            falou = True