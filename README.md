# jogo-homemaranha[readme.md](https://github.com/user-attachments/files/29028153/readme.md)
# Jogo 2D em Python

Este projeto foi desenvolvido como atividade avaliativa da disciplina de Pensamento Computacional, pertencente ao primeiro nanodegree do curso de Ciência da Computação da Atitus Educação, com o objetivo de demonstrar o aprendizado em programação com Python. O jogo foi feito em Python, usando principalmente Pygame para a parte visual e interativa. Também usa Tkinter para entrada do nome do jogador, JSON para salvar pontuação, pyttsx3 para fala do computador e cx_Freeze para transformar o projeto em executável.

**Desenvolvedora:** Kélen Camargo dos Santos

**RA:** 1102339

# 🎮 Sobre o jogo

Neste jogo 2D, o participante controla o personagem Homem-Aranha, que deve desviar das bombas que caem do céu. A cada sequência de bombas evitada, o jogador acumula pontos, enquanto a dificuldade aumenta progressivamente ao longo da partida. O jogo conta com uma tela inicial com instruções, uma fase principal de jogabilidade e uma tela de Game Over, com possibilidade de reiniciar a partida. O objetivo é sobreviver pelo maior tempo possível, alcançar a maior pontuação e superar o próprio recorde.

# 🧠 Tecnologias e Bibliotecas Utilizadas
`pygame`- Criar a tela do jogo, mostrar imagens, controlar eventos do teclado/mouse, sons, música, colisões e atualização da tela.
`random` - Sortear posições aleatórias, como a posição das bombas e do brilho decorativo.
`os`- Limpar o terminal com `os.system("cls")`.
`tkinter` - Abrir a pequena janela para o jogador digitar nickname.
`messagebox` - Mostrar aviso caso o usuário não digite o nome.
`json`- Ler e salvar os registros de pontuação no arquivo `log.dat`.
`datetime` - Salvar a data e a hora da pontuação do jogador.
`time` - Criar pausas com `time.sleep()`, usado na função `aguarde()`.
`pyttsx3` - Fazer o computador falar mensagens, como as boas-vindas e “Game Over”.
`threading` - Permitir que a fala das instruções aconteça enquanto a tela de boas-vindas continua funcionando.
`cx_Freeze` - Gerar o executável do jogo a partir do código Python.
