# Jogo da Velha em Python ❌ ⭕
Um jogo da velha simples e interativo feito em Python para ser jogado direto no terminal. O projeto foi desenvolvido com foco em lógica de programação básica, utilizando matrizes lineares (listas), funções e validação de dados.
## 🚀 Como Funciona o Jogo?
O jogo é jogado em um tabuleiro clássico de 3x3. Dois jogadores alternam seus turnos (Jogador X e Jogador O).
Para realizar uma jogada, você deve digitar a posição desejada no formato linha,coluna (separados por uma vírgula), utilizando os índices de 0 a 2.
## 📌 Mapa do Tabuleiro (Índices)
Para facilitar visualmente, as coordenadas do tabuleiro funcionam da seguinte forma:

 Top-Esquerda: 0,0  |  Top-Centro: 0,1  | Top-Direita: 0,2

 Meio-Esquerda: 1,0 |  Meio-Centro: 1,1 | Meio-Direita: 1,2

Baixo-Esquerda: 2,0 | Baixo-Centro: 2,1 | Baixo-Direita: 2,2

<img width="824" height="107" alt="image" src="https://github.com/user-attachments/assets/0e877214-7f6b-48a5-bf9e-c279f0e6ee8c" />

## 🛠️ Funcionalidades
Validação de Entrada: O programa garante que você só digite coordenadas válidas (entre 0 e 2) e no formato correto.
Verificação de Ocupação: Não é possível jogar em uma casa que já foi preenchida.
Detecção Automática de Vitória/Velha: O jogo valida todas as 8 combinações possíveis de vitória a cada turno e encerra o jogo caso dê empate (velha).
## 📦 Como Executar
### Pré-requisitos
Você só precisa ter o Python 3 instalado na sua máquina.
### Passo a Passo
Clone este repositório ou baixe o arquivo do código.
Abra o terminal na pasta onde o arquivo está salvo.
Execute o comando:
Bash
python jogo_da_velha.py

(Substitua jogo_da_velha.py pelo nome exato do seu arquivo script).
## 🧠 Lógica de Código Destacada
Uma curiosidade sobre a implementação é como o tabuleiro de duas dimensões (3x3) é tratado internamente como uma lista simples de 9 elementos ([0, 1, 2, 3, 4, 5, 6, 7, 8]).
A conversão da coordenada digitada pelo usuário para o índice correto da lista é feita através desta fórmula matemática simples:
Python
posicao = linha * 3 + coluna

