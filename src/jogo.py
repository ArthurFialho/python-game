import pygame

from src.config import (
    ALTURA_TELA,
    CAMINHO_RANKING,
    CAMINHO_RECORDE,
    CINZA,
    DANO_POR_INIMIGO,
    ESTADO_GAME_OVER,
    ESTADO_JOGANDO,
    ESTADO_MENU,
    FPS,
    LARGURA_TELA,
    PONTOS_POR_GEMA,
    TAMANHO_RANKING,
    TITULO_JOGO,
    VELOCIDADE_JOGADOR,
    VIDAS_INICIAIS,
)
from src.dados import (
    carregar_ranking,
    carregar_recorde,
    inserir_no_ranking,
    salvar_ranking,
    salvar_recorde,
)
from src.entidades import (
    criar_gema,
    criar_inimigo,
    criar_jogador,
    manter_dentro_da_tela,
    mover_jogador,
    reposicionar_apos_colisao,
)
from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    tomar_dano,
    verificar_colisao,
)
from src.interface import (
    criar_fontes,
    desenhar_game_over,
    desenhar_hud,
    desenhar_menu,
)


def _criar_partida():
    """Cria o estado inicial de uma partida nova."""
    return {
        "jogador": criar_jogador(),
        "gema": criar_gema(),
        "inimigo": criar_inimigo(),
        "pontos": 0,
        "vidas": VIDAS_INICIAIS,
    }


def _processar_eventos(estado):
    """Trata eventos discretos e devolve (continuar_executando, deve_iniciar_partida)."""
    continuar = True
    iniciar = False

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            continuar = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                continuar = False
            elif estado == ESTADO_MENU and evento.key == pygame.K_SPACE:
                iniciar = True
            elif estado == ESTADO_GAME_OVER and evento.key == pygame.K_r:
                iniciar = True

    return continuar, iniciar


def _atualizar_partida(partida, teclas):
    """Atualiza a partida em curso e devolve True quando o jogador perde."""
    jogador = partida["jogador"]
    gema = partida["gema"]
    inimigo = partida["inimigo"]

    mover_jogador(jogador, teclas, VELOCIDADE_JOGADOR)
    manter_dentro_da_tela(jogador, LARGURA_TELA, ALTURA_TELA)

    if verificar_colisao(jogador["rect"], gema["rect"]):
        partida["pontos"] = calcular_pontos(partida["pontos"], PONTOS_POR_GEMA)
        reposicionar_apos_colisao(gema, LARGURA_TELA, ALTURA_TELA)

    if verificar_colisao(jogador["rect"], inimigo["rect"]):
        partida["vidas"] = tomar_dano(partida["vidas"], DANO_POR_INIMIGO)
        reposicionar_apos_colisao(inimigo, LARGURA_TELA, ALTURA_TELA)

    return jogador_perdeu(partida["vidas"])


def _desenhar_partida(tela, partida, fontes, recorde):
    """Desenha cenário, entidades e HUD da partida."""
    tela.fill(CINZA)
    tela.blit(partida["gema"]["imagem"], partida["gema"]["rect"])
    tela.blit(partida["inimigo"]["imagem"], partida["inimigo"]["rect"])
    tela.blit(partida["jogador"]["imagem"], partida["jogador"]["rect"])
    desenhar_hud(tela, fontes, partida["pontos"], partida["vidas"], recorde)


def _finalizar_partida(pontos, recorde):
    """Persiste recorde e ranking ao fim de uma partida; devolve o novo recorde."""
    if pontos > recorde:
        recorde = pontos
        salvar_recorde(CAMINHO_RECORDE, recorde)

    if pontos > 0:
        ranking = carregar_ranking(CAMINHO_RANKING)
        ranking = inserir_no_ranking(ranking, pontos, TAMANHO_RANKING)
        salvar_ranking(CAMINHO_RANKING, ranking)

    return recorde


def executar_jogo():
    """Executa o loop principal do jogo gerenciando os estados de menu, partida e fim."""
    pygame.init()
    pygame.display.set_caption(TITULO_JOGO)
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    relogio = pygame.time.Clock()
    fontes = criar_fontes()

    estado = ESTADO_MENU
    partida = None
    pontos_finais = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)
    rodando = True

    while rodando:
        relogio.tick(FPS)

        rodando, iniciar = _processar_eventos(estado)
        if iniciar:
            partida = _criar_partida()
            estado = ESTADO_JOGANDO

        if estado == ESTADO_JOGANDO and partida is not None:
            teclas = pygame.key.get_pressed()
            perdeu = _atualizar_partida(partida, teclas)

            if partida["pontos"] > recorde:
                recorde = partida["pontos"]

            _desenhar_partida(tela, partida, fontes, recorde)

            if perdeu:
                pontos_finais = partida["pontos"]
                recorde = _finalizar_partida(pontos_finais, recorde)
                estado = ESTADO_GAME_OVER
        elif estado == ESTADO_MENU:
            ranking = carregar_ranking(CAMINHO_RANKING)
            desenhar_menu(tela, fontes, recorde, ranking)
        else:
            desenhar_game_over(tela, fontes, pontos_finais, recorde)

        pygame.display.flip()

    pygame.quit()