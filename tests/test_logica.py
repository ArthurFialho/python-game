import os
import tempfile

from src.dados import (
    carregar_ranking,
    carregar_recorde,
    inserir_no_ranking,
    salvar_ranking,
    salvar_recorde,
)
from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    tomar_dano,
)


# --- Funcoes de logica do jogo -------------------------------------------------


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_calcular_pontos_com_zero():
    """Somar zero pontos nao deve alterar a pontuacao atual."""
    assert calcular_pontos(42, 0) == 42


def test_tomar_dano_reduz_vidas():
    """Deve reduzir o total de vidas pelo dano informado."""
    assert tomar_dano(3, 1) == 2


def test_tomar_dano_pode_zerar_vidas():
    """Deve permitir que as vidas cheguem a zero."""
    assert tomar_dano(1, 1) == 0


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_perdeu_com_vidas_negativas():
    """Vidas negativas tambem devem indicar derrota."""
    assert jogador_perdeu(-1) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_limitar_valor_no_limite_minimo():
    """Deve manter o valor quando ele for exatamente o limite minimo."""
    assert limitar_valor(0, 0, 100) == 0


def test_limitar_valor_no_limite_maximo():
    """Deve manter o valor quando ele for exatamente o limite maximo."""
    assert limitar_valor(100, 0, 100) == 100


# --- Ranking -------------------------------------------------------------------


def test_inserir_no_ranking_ordena_em_ordem_decrescente():
    """Pontuacoes devem ficar ordenadas da maior para a menor."""
    assert inserir_no_ranking([10, 30, 20], 25) == [30, 25, 20, 10]


def test_inserir_no_ranking_respeita_tamanho_maximo():
    """O ranking nao deve ultrapassar o tamanho maximo informado."""
    resultado = inserir_no_ranking([50, 40, 30, 20, 10], 25, tamanho_maximo=5)
    assert resultado == [50, 40, 30, 25, 20]


def test_inserir_no_ranking_em_lista_vazia():
    """Deve permitir inserir a primeira pontuacao em um ranking vazio."""
    assert inserir_no_ranking([], 10) == [10]


# --- Persistencia em arquivo ---------------------------------------------------


def test_carregar_recorde_inexistente_retorna_zero():
    """Carregar um arquivo de recorde inexistente deve retornar 0."""
    caminho = os.path.join(tempfile.gettempdir(), "recorde_inexistente_xyz.txt")
    if os.path.exists(caminho):
        os.remove(caminho)
    assert carregar_recorde(caminho) == 0


def test_salvar_e_carregar_recorde():
    """O recorde salvo deve ser recuperado igual ao gravado."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as arquivo:
        caminho = arquivo.name
    try:
        salvar_recorde(caminho, 123)
        assert carregar_recorde(caminho) == 123
    finally:
        os.remove(caminho)


def test_carregar_ranking_inexistente_retorna_lista_vazia():
    """Carregar um arquivo de ranking inexistente deve retornar lista vazia."""
    caminho = os.path.join(tempfile.gettempdir(), "ranking_inexistente_xyz.txt")
    if os.path.exists(caminho):
        os.remove(caminho)
    assert carregar_ranking(caminho) == []


def test_salvar_e_carregar_ranking():
    """O ranking salvo deve ser recuperado na mesma ordem."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as arquivo:
        caminho = arquivo.name
    try:
        salvar_ranking(caminho, [100, 80, 60])
        assert carregar_ranking(caminho) == [100, 80, 60]
    finally:
        os.remove(caminho)


def test_carregar_ranking_ignora_linhas_invalidas():
    """Linhas em branco ou invalidas devem ser ignoradas ao carregar o ranking."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as arquivo:
        arquivo.write("50\n\nlixo\n30\n")
        caminho = arquivo.name
    try:
        assert carregar_ranking(caminho) == [50, 30]
    finally:
        os.remove(caminho)
