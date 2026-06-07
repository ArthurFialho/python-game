"""Configurações centrais do jogo (janela, cores, gameplay e caminhos de arquivos)."""

# --- Janela ---
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
TITULO_JOGO = "Perdido no Algoritmo"

# --- Cores ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212, 212, 212)
AMARELO = (245, 200, 66)
VERMELHO = (220, 80, 80)
AZUL = (66, 135, 245)

# --- Caminhos de arquivos ---
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_RANKING = "data/ranking.txt"

# --- Estados do jogo ---
ESTADO_MENU = "menu"
ESTADO_JOGANDO = "jogando"
ESTADO_GAME_OVER = "game_over"

# --- Parâmetros de gameplay ---
VELOCIDADE_JOGADOR = 5
VIDAS_INICIAIS = 3
PONTOS_POR_GEMA = 10
DANO_POR_INIMIGO = 1
TAMANHO_RANKING = 5

# --- Reposicionamento de entidades após colisão ---
SALTO_REPOSICIONAR_X = 80
SALTO_REPOSICIONAR_Y = 50
MARGEM_REPOSICIONAR = 50

# --- Posições iniciais (topleft) ---
POSICAO_INICIAL_JOGADOR = (100, 100)
POSICAO_INICIAL_GEMA = (500, 300)
POSICAO_INICIAL_INIMIGO = (200, 500)

# --- Recorte dos sprites na spritesheet ---
ATLAS_JOGADOR = {"x": 110, "y": 120, "width": 190, "height": 190, "scale": 0.5}
ATLAS_GEMA = {"x": 900, "y": 690, "width": 200, "height": 200, "scale": 0.5}
ATLAS_INIMIGO = {"x": 905, "y": 1060, "width": 200, "height": 130, "scale": 0.5}

# --- Fontes ---
TAMANHO_FONTE_TITULO = 48
TAMANHO_FONTE_TEXTO = 28
TAMANHO_FONTE_HUD = 24
