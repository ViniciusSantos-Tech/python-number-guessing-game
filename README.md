#  Jogo de Adivinhação - Meu Primeiro Projeto Python

## 📋 Sobre o Projeto
Este foi meu **primeiro projeto** em Python - um simples jogo de adivinhação onde o jogador tenta descobrir um número aleatório entre 1 e 5. Desenvolvido durante meus primeiros passos na programação.

## 🎮 Como Jogar
- O sistema gera um **número aleatório entre 1 e 5**
- Você tenta adivinhar o número
- Recebe feedback se acertou ou errou
- Pode jogar quantas vezes quiser

##  Funcionalidades
- ✅ Geração de números aleatórios
- ✅ Sistema de tentativas ilimitadas
- ✅ Feedback imediato (acerto/erro)
- ✅ Opção de jogar novamente
- ✅ Interface simples e intuitiva

## 🛠️ Tecnologias Utilizadas
```python
# Módulos Python
- random (geração de números aleatórios)

# Conceitos Aplicados
- Variáveis e input do usuário
- Estruturas condicionais (if/else)
- Loops while para repetição
- Comparação de valores
- Controle de fluxo do programa
```

## 💡 Aprendizados
Este projeto me ensinou os **fundamentos da programação**:
- Como usar a biblioteca `random`
- Estruturas de controle (`if`, `else`)
- Loops com `while`
- Interação com o usuário via `input()`
- Lógica booleana para controle do jogo

## Código Principal
```python
import random
jogar_novamente = True

while jogar_novamente:
    numero_aleatorio = random.randint(1,5)
    numero = int(input("Digite um numero: "))
    
    if numero == numero_aleatorio:
        print("Voce acertou")
    else:
        print("Voce nao acertou")
        print(f"O numero era: {numero_aleatorio}")
    
    resposta = input("Deseja tentar novamente? (sim/nao) ")
    if resposta.lower() != "sim":
        jogar_novamente = False
        print("Obrigado por jogar!")
```

##  Desafios Superados
- Entender como funcionam os loops infinitos
- Aprender a usar condições para controlar o fluxo
- Manipular entrada e saída de dados
- Trabalhar com valores aleatórios

## 👨‍💻 Autor
**Vinicius Santos**  
*Desenvolvedor Python Iniciante*

[![GitHub](https://img.shields.io/badge/GitHub-ViniciusSantos--Tech-blue?style=for-the-badge&logo=github)](https://github.com/ViniciusSantos-Tech)

---

> **"O projeto que iniciou minha jornada na programação - simples, mas cheio de aprendizado!"** 💖
