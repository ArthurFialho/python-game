"""Criação e atualização de entidades do jogo (jogador, gema e inimigo)."""

import pygame

from src.config import (
    ATLAS_GEMA,
    ATLAS_INIMIGO,
    ATLAS_JOGADOR,
    CAMINHO_SPRITES,
    MARGEM_REPOSICIONAR,
    POSICAO_INICIAL_GEMA,
    POSICAO_INICIAL_INIMIGO,
    POSICAO_INICIAL_JOGADOR,
    SALTO_REPOSICIONAR_X,
    SALTO_REPOSICIONAR_Y,
)
from src.funcoes import limitar_valor
from src.sprites import pegar_sprite


def criar_entidade(atlas, posicao):
    """Cria uma entidade (imagem e rect) a partir de um recorte do atlas de sprites."""
    imagem = pegar_sprite(
        CAMINHO_SPRITES,
        x=atlas["x"],
        y=atlas["y"],
        width=atlas["width"],
        height=atlas["height"],
        scale=atlas["scale"],
    )
    return {"imagem": imagem, "rect": imagem.get_rect(topleft=posicao)}


def criar_jogador():
    """Cria o jogador na posição inicial padrão."""
    return criar_entidade(ATLAS_JOGADOR, POSICAO_INICIAL_JOGADOR)


def criar_gema():
    """Cria a gema na posição inicial padrão."""
    return criar_entidade(ATLAS_GEMA, POSICAO_INICIAL_GEMA)


def criar_inimigo():
    """Cria o inimigo na posição inicial padrão."""
    return criar_entidade(ATLAS_INIMIGO, POSICAO_INICIAL_INIMIGO)


def mover_jogador(jogador, teclas, velocidade):
    """Atualiza a posição do jogador com base nas teclas pressionadas (setas e WASD)."""
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        jogador["rect"].x -= velocidade
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        jogador["rect"].x += velocidade
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        jogador["rect"].y -= velocidade
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        jogador["rect"].y += velocidade


def manter_dentro_da_tela(entidade, largura_tela, altura_tela):
    """Mantém o retângulo da entidade dentro dos limites da tela."""
    entidade["rect"].x = limitar_valor(
        entidade["rect"].x, 0, largura_tela - entidade["rect"].width
    )
    entidade["rect"].y = limitar_valor(
        entidade["rect"].y, 0, altura_tela - entidade["rect"].height
    )


def reposicionar_apos_colisao(entidade, largura_tela, altura_tela):
    """Move a entidade para uma nova posição após uma colisão com o jogador."""
    entidade["rect"].x += SALTO_REPOSICIONAR_X
    entidade["rect"].y += SALTO_REPOSICIONAR_Y

    if entidade["rect"].x > largura_tela - entidade["rect"].width:
        entidade["rect"].x = MARGEM_REPOSICIONAR
    if entidade["rect"].y > altura_tela - entidade["rect"].height:
        entidade["rect"].y = MARGEM_REPOSICIONAR
