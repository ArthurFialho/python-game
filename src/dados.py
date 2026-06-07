def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0


def carregar_ranking(caminho_arquivo):
    """Carrega o ranking salvo (uma pontuação por linha); retorna lista vazia se não existir."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        return []

    ranking = []
    for linha in linhas:
        valor = linha.strip()
        if valor == "":
            continue
        try:
            ranking.append(int(valor))
        except ValueError:
            continue
    return ranking


def salvar_ranking(caminho_arquivo, ranking):
    """Salva o ranking em arquivo, uma pontuação por linha."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for pontuacao in ranking:
            arquivo.write(f"{pontuacao}\n")


def inserir_no_ranking(ranking, pontuacao, tamanho_maximo=5):
    """Insere uma pontuação no ranking mantendo apenas as melhores em ordem decrescente."""
    novo_ranking = list(ranking) + [pontuacao]
    novo_ranking.sort(reverse=True)
    return novo_ranking[:tamanho_maximo]
