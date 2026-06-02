<div align="center">

```
██████╗ ███████╗██████╗ ██████╗ ██╗██████╗  ██████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔═══██╗
██████╔╝█████╗  ██████╔╝██║  ██║██║██║  ██║██║   ██║
██╔═══╝ ██╔══╝  ██╔══██╗██║  ██║██║██║  ██║██║   ██║
██║     ███████╗██║  ██║██████╔╝██║██████╔╝╚██████╔╝
╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝  ╚═════╝

███╗   ██╗ ██████╗      █████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗████████╗███╗   ███╗ ██████╗
████╗  ██║██╔═══██╗    ██╔══██╗██║     ██╔════╝ ██╔═══██╗██╔══██╗██║╚══██╔══╝████╗ ████║██╔═══██╗
██╔██╗ ██║██║   ██║    ███████║██║     ██║  ███╗██║   ██║██████╔╝██║   ██║   ██╔████╔██║██║   ██║
██║╚██╗██║██║   ██║    ██╔══██║██║     ██║   ██║██║   ██║██╔══██╗██║   ██║   ██║╚██╔╝██║██║   ██║
██║ ╚████║╚██████╔╝    ██║  ██║███████╗╚██████╔╝╚██████╔╝██║  ██║██║   ██║   ██║ ╚═╝ ██║╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝
```

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-00B140?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-F4A01A?style=for-the-badge)

<br/>

> *"Num mundo onde tudo é controlado por algoritmos, apenas quem sabe programar encontra o caminho."*

<br/>
</div>

<div align="center">
  
| Integrantes |
|-----------|
| Arthur Fernandes Fialho e Silva |
| Arthur Rodrigues de Macedo |
| Miguel Xavier dos Santos |
| Pamela Fernandes Nilo |
| Túlio Marcus de Oliveira Gonçalves |
</div>


---

## 📋 Índice

- [🎮 Sobre o Jogo](#-sobre-o-jogo)
- [👾 Como Jogar](#-como-jogar)
- [🎯 Objetivos](#-objetivos)
- [📏 Regras](#-regras)
- [📦 Elementos do Jogo](#-elementos-do-jogo)
- [⌨️ Controles](#️-controles)
- [🏗️ Organização do Código](#️-organização-do-código)
- [🖼️ Recursos Externos](#️-recursos-externos)
- [🚀 Melhorias Previstas](#-melhorias-previstas)

---

## 🎮 Sobre o Jogo

<div align="center">


</div>

**Perdido no Algoritmo** é um jogo de labirinto simples onde o jogador não controla o personagem diretamente — ele **monta algoritmos** com blocos de programação para mover o personagem pelo cenário.

Na tela aparecem um personagem, diferentes cenários organizados em uma grade, e objetos relacionados aos desafios de cada fase: estrelas para coletar, livros, interruptores, portas, obstáculos e um painel com blocos de comandos. Por meio desse painel, o jogador faz o personagem andar, virar, coletar itens, ativar mecanismos e tomar decisões.

Conforme as fases avançam, torna-se necessário utilizar estruturas condicionais (`IF` e `ELSE`) e laços de repetição (`WHILE` e `FOR`), além de estratégias para contornar obstáculos e resolver problemas de forma eficiente.

---

## 👾 Como Jogar

<div align="center">

![How to play gif](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTZlMHU4NmRrd3VkZWc5ajlvcGhsNmF4MHd4MGF5ZTR4bGloNzA2YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/077i6AULCXc0FKTj9s/giphy.gif)

</div>

<div align="center">

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  1. Analise o labirinto e os objetivos da fase           │
│              ↓                                           │
│  2. Monte sua sequência de blocos no painel              │
│              ↓                                           │
│  3. Pressione ENTER para executar                        │
│              ↓                                           │
│  4. Observe o personagem seguindo seus comandos          │
│              ↓                                           │
│  5. Se não conseguir, perde uma vida e tenta de novo     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```
</div>
---

## 🎯 Objetivos

<div align="center">


</div>

- 🏁 Chegar até o final do labirinto
- 📚 Coletar itens
- ✂️ Coletar os itens no **menor número de linhas de comando possível**
- 🚧 Evitar obstáculos

### Condição de vitória

> Chegar ao final da fase seguindo as regras impostas.

### Condição de derrota

> Usar todos os movimentos disponíveis **ou** perder todas as vidas.

---

## 📏 Regras

<div align="center">


</div>
<div align="center">

| # | Regra |
|---|-------|
| 1 | O jogador começa no ponto **A** e deve chegar ao ponto **B** |
| 2 | Para chegar ao ponto B, ele deve definir a movimentação com **blocos de programação** |
| 3 | Há um **limite de comandos** para executar por fase |
| 4 | Caso não consiga completar a fase, perde **uma vida** |
| 5 | O jogador começa com **3 vidas** (tentativas) |
| 6 | Caso as vidas acabem, retorna ao **começo do game** |
</div>

---

## 📦 Elementos do Jogo

<div align="center">


</div>

### 🤖 Personagem principal

Um personagem controlado pelos blocos de comando selecionados pelo jogador.

### 🧱 Obstáculos

Barreiras que impedem a passagem do personagem: estantes, móveis, portas, etc.

### 📚 Itens de interação

Livros aparecem na tela e aumentam a pontuação quando coletados.

### ❤️ Pontuação, Vidas e Progresso

```
♥ ♥ ♥  →  3 vidas iniciais

📚 Coletar um livro    → +10 pontos
💀 Perder todas vidas  → volta ao início
```

O jogador começa com uma quantidade limitada de ações por fase, 3 vidas, e ganha 10 pontos por item coletado.

---

## ⌨️ Controles

<div align="center">

```
╔══════════════════════════════════════════════════╗
║               CONTROLES DO JOGO                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  🖱️  Mouse / Teclado  →  Selecionar bloco        ║
║                                                  ║
║  ↵   ENTER            →  Executar tentativa      ║
║                                                  ║
║  ⎋   ESC              →  Sair do jogo            ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

</div>

---

## 🏗️ Organização do Código

<div align="center">

![Code gif](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWd3am0yY3hoaWhuMGNibW5pbHg2d201NzN0NTR3bzVjdXo5Nmp0eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qgQUggAC3Pfv687qPC/giphy.gif)

</div>

```
main.py          →  inicializa o jogo e chama o loop principal

src/
├── jogo.py      →  loop principal e gerenciamento dos estados do jogo
├── config.py    →  configurações globais (tamanho da tela, cores, constantes)
├── mapa.py      →  representação e renderização dos mapas em matriz
├── personagem.py→  lógica de movimentação e estado do personagem
├── blocos.py    →  definição dos blocos de comando e seu comportamento (dicionários)
├── fase.py      →  carregamento e controle de cada fase/disciplina
├── avaliacao.py →  sistema de notas e verificação de eficiência
├── dados.py     →  leitura e escrita de progresso, ranking e configs em arquivo
└── ui.py        →  elementos de interface (painel de blocos, dicas, HUD de notas)
```

---

## 🖼️ Recursos Externos

- Imagens obtidas de banco gratuito
- Efeitos sonoros obtidos de banco gratuito
- Fonte personalizada

---

## ⚠️ Principais Dificuldades Esperadas

```
→  Movimentação do jogador
→  Organização do código
→  Interface gráfica
→  Modelagem das classes
→  Uso do GitHub
→  Testes
→  Exibição de textos na tela
```

---

## 📦 Escopo Mínimo

A versão mínima contará com **três fases completas e funcionais**, nas quais o jogador utilizará comandos de programação para conduzir o personagem até o objetivo final. Essa versão incluirá:

- Movimentação do personagem
- Obstáculos para desviar
- Validação da sequência de comandos criada pelo jogador

---

## 🚀 Melhorias Previstas

<div align="center">

</div>

Caso haja tempo durante o desenvolvimento:

- [ ] ⭐ Coletar estrelas para pontuação e chaves para abrir portas e avançar fases
- [ ] 🔊 Sons gratuitos
- [ ] 🗺️ Novas fases
- [ ] 🎭 Animações
- [ ] 🧑‍🎨 Diferentes personagens
- [ ] 🧱 Novos tipos de obstáculos
- [ ] 📈 Aumento de dificuldade

---

## 👨‍💻 Time de Desenvolvimento

<div align="center">

![Team gif](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXc5YXo3MHgwMmo2Z3Z0OXB5NHBwbXU0Y2w5dWViMzlhemhoZWlsNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LaVp0AyqR5bGsC5Cbm/giphy.gif)

</div>


---

<div align="center">

```
> Feito com ☕, 🧠 e muito  print("debug")
```

**Perdido no Algoritmo** — Projeto Acadêmico · 2025

</div>
