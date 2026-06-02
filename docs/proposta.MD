# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

Perdido no algoritmo

## 2. Integrantes do grupo

Arthur Fernandes Fialho e Silva 
Arthur Rodrigues de Macedo 
Miguel Xavier dos Santos 
Pamela Fernandes Nilo
Túlio Marcus de Oliveira Gonçalves 

## 3. Tipo de jogo

- Labirinto simples;

## 4. Descrição geral do jogo

- O que aparece na tela? Na tela aparece um personagem que representa o jogador, além de diferentes cenários organizados em uma grade. Também aparecem objetos e elementos relacionados aos desafios de cada fase, como estrelas para coletar, livros, interruptores, portas, obstáculos e um painel com blocos de comandos. Esse painel permite que o jogador monte algoritmos para controlar o personagem. 

- O que o jogador controla?O jogador controla o personagem de forma indireta, utilizando blocos de programação. Por meio desses blocos, é possível fazer o personagem andar, virar, coletar itens, pegar objetos, ativar mecanismos e tomar decisões de acordo com as situações encontradas no cenário. 

- O que o jogador precisa fazer?O jogador precisa analisar cada fase e criar uma sequência lógica de comandos para que o personagem consiga atingir os objetivos propostos. Esses objetivos podem incluir coletar estrelas, transportar objetos, ativar interruptores, abrir portas e chegar a um local específico do mapa. 

- Quais desafios aparecem durante a partida?Durante a partida, o jogador encontra desafios que exigem raciocínio lógico e pensamento computacional. Conforme as fases avançam, torna-se necessário utilizar estruturas condicionais (IF e ELSE) e laços de repetição (WHILE E FOR) , além de estratégias para contornar obstáculos, otimizar comandos e resolver problemas de forma eficiente. 


## 5. Objetivo do jogador

Objetivos:

- coletar os itens no menor número de linhas possíveis
- chegar até o final do labirinto;
- coletar itens.;
- evitar obstáculos;

## 6. Regras principais
Regras do grupo:

- Regra 1: O jogador começa no ponto A e deve chegar ao ponto B
- Regra 2:.Para chegar ao ponto B, ele deve definir a movimentação com blocos de    programação
- Regra 3: Ele tem um limite de comandos para executar por fase.
- Regra 4: Caso não consiga, perderá uma vida.
- Regra 5: O jogador começa com 3 vidas (tentativas)
-Regra 6: Caso as vidas acabem, ele retorna ao começo do game.

## 7. Condição de vitória

Condição de vitória:

- chegar ao final da fase seguindo as regras impostas

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

- usar todos os movimentos;
- perder todas as vidas;

## 9. Elementos previstos no jogo
## Jogador ou elemento principal
- Um personagem controlado pelos blocos de comando selecionados.

## Obstáculos, inimigos ou desafios
-Exemplo: Barreiras que impedem a passagem do personagem (Estantes, móveis, portas, etc)

## Itens, alvos ou objetos de interação
- Livros aparecem na tela e aumentam a pontuação quando coletadas.

## Pontuação, vidas, tempo ou progresso
- O jogador começa com uma quantidade limitada de ações por fase,  3 vidas e ganha 10 pontos por item coletado.

## 10. Controles previstos
Controles do grupo:

- Selecionar com o mouse/teclado o bloco desejado
- Enter: executar tentativa
- ESC: sair do jogo

## 11. Organização inicial do código
Organização planejada:

main.py: inicializa o jogo e chama o loop principal
src/jogo.py: contém o loop principal e gerencia os estados do jogo
src/config.py: configurações globais (tamanho da tela, cores, constantes)
src/mapa.py: representação e renderização dos mapas em matriz
src/personagem.py: lógica de movimentação e estado do personagem
src/blocos.py: definição dos blocos de comando e seu comportamento (dicionários)
src/fase.py: carregamento e controle de cada fase/disciplina
src/avaliacao.py: sistema de notas e verificação de eficiência
src/dados.py: leitura e escrita de progresso, ranking e configurações em arquivo
src/ui.py: elementos de interface (painel de blocos, dicas, HUD de notas)

## 12. Recursos externos previstos
Recursos previstos:

- imagens obtidas de banco gratuito;
- efeitos sonoros obtidos de banco gratuito;
- fonte personalizada.

## 13. Principais dificuldades esperadas
Dificuldades previstas:

- movimentação do jogador;
- organização do código;
- interface gráfica;
- modelagem das classes;
- uso do GitHub;
- testes;
- exibição de textos na tela.


## 14. Escopo mínimo para a entrega final
Escopo mínimo:

A versão mínima do jogo contará com três fases completas e funcionais, na qual o jogador deverá utilizar comandos de programação para conduzir o personagem até o objetivo final. Essa versão incluirá movimentação do personagem, obstáculos para desviar e validação da sequência de comandos criada pelo jogador. 

## 15. Possíveis melhorias, caso haja tempo:
Melhorias possíveis:

- Melhoria 1: O jogador terá que coletar estrelas para aumentar a pontuação e chave para abrir portas e passar para as próximas fases.
- Melhoria 2: Sons gratuitos;
- Melhoria 3: fases;
- Melhoria 4: animações;
- Melhoria 5: diferentes personagens;
- Melhoria 6: novos tipos de obstáculos;
- Melhoria 7: aumento de dificuldade;





