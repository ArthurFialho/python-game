"""Renderização do HUD e telas auxiliares do jogo (menu e fim de jogo)."""

import pygame

from src.config import (
    AMARELO,
    AZUL,
    CINZA,
    LARGURA_TELA,
    PRETO,
    TAMANHO_FONTE_HUD,
    TAMANHO_FONTE_TEXTO,
    TAMANHO_FONTE_TITULO,
    TITULO_JOGO,
    VERMELHO,
)


def criar_fontes():
    """Cria e retorna as fontes utilizadas pela interface do jogo."""
    return {
        "titulo": pygame.font.SysFont(None, TAMANHO_FONTE_TITULO),
        "texto": pygame.font.SysFont(None, TAMANHO_FONTE_TEXTO),
        "hud": pygame.font.SysFont(None, TAMANHO_FONTE_HUD),
    }


def _desenhar_texto_centralizado(tela, fonte, texto, cor, y):
    """Desenha um texto horizontalmente centralizado na tela."""
    superficie = fonte.render(texto, True, cor)
    rect = superficie.get_rect(center=(LARGURA_TELA // 2, y))
    tela.blit(superficie, rect)


def desenhar_hud(tela, fontes, pontos, vidas, recorde):
    """Desenha o HUD com pontuação, recorde e vidas no topo da tela."""
    fonte = fontes["hud"]

    texto_pontos = fonte.render(f"Pontos: {pontos}", True, PRETO)
    texto_recorde = fonte.render(f"Recorde: {recorde}", True, AZUL)
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, VERMELHO)

    tela.blit(texto_pontos, (10, 10))
    tela.blit(
        texto_recorde,
        (LARGURA_TELA // 2 - texto_recorde.get_width() // 2, 10),
    )
    tela.blit(texto_vidas, (LARGURA_TELA - texto_vidas.get_width() - 10, 10))


def desenhar_menu(tela, fontes, recorde, ranking):
    """Desenha a tela inicial com instruções e ranking."""
    tela.fill(CINZA)

    _desenhar_texto_centralizado(tela, fontes["titulo"], TITULO_JOGO, PRETO, 100)
    _desenhar_texto_centralizado(
        tela, fontes["texto"], "Pressione ESPACO para jogar", PRETO, 190
    )
    _desenhar_texto_centralizado(
        tela, fontes["texto"], "Setas ou WASD para mover", PRETO, 230
    )
    _desenhar_texto_centralizado(tela, fontes["texto"], "ESC para sair", PRETO, 270)

    _desenhar_texto_centralizado(
        tela, fontes["texto"], f"Recorde atual: {recorde}", AZUL, 340
    )
    _desenhar_texto_centralizado(tela, fontes["texto"], "Ranking:", AMARELO, 390)

    if not ranking:
        _desenhar_texto_centralizado(
            tela, fontes["hud"], "(ainda nao ha pontuacoes registradas)", PRETO, 430
        )
    else:
        for indice, pontuacao in enumerate(ranking, start=1):
            _desenhar_texto_centralizado(
                tela, fontes["hud"], f"{indice}. {pontuacao}", PRETO, 410 + indice * 28
            )


def desenhar_game_over(tela, fontes, pontos, recorde):
    """Desenha a tela de fim de jogo com a pontuação final e instruções."""
    tela.fill(CINZA)

    _desenhar_texto_centralizado(tela, fontes["titulo"], "Fim de jogo", VERMELHO, 150)
    _desenhar_texto_centralizado(
        tela, fontes["texto"], f"Pontuacao final: {pontos}", PRETO, 240
    )
    _desenhar_texto_centralizado(
        tela, fontes["texto"], f"Recorde: {recorde}", AZUL, 280
    )

    _desenhar_texto_centralizado(
        tela, fontes["texto"], "R para reiniciar", PRETO, 370
    )
    _desenhar_texto_centralizado(tela, fontes["texto"], "ESC para sair", PRETO, 410)
