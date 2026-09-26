# Caatinga.AI — Sprint 1

Sistema desenvolvido para a disciplina de **Inteligência Artificial** do **Centro Universitário do Rio São Francisco (UniRios)**.

O **Caatinga.AI** é um projeto acadêmico que simula a navegação autônoma e o diagnóstico preventivo de pragas em um pomar localizado na região da Caatinga. O sistema integra diferentes técnicas de Inteligência Artificial para realizar a navegação pelo ambiente, analisar informações de sensores e auxiliar na tomada de decisões.

As principais técnicas utilizadas são:

- **Busca em Grafos:** navegação pelo terreno e otimização de rotas.
- **Inferência Bayesiana:** análise probabilística da presença de pragas.
- **Sistema Especialista:** aplicação de regras para tomada de decisão e recomendações de manejo.

---

## Integrantes

| Integrante | Matrícula |
|---|---|
| Antônio M. Oliveira | `24114073` |
| Tony Carlos | `24114047` |

---

## Visão Geral

O sistema é dividido em três componentes principais:

### 1. Geração do Terreno e Sensores

**Arquivo:** `src/gerador_pomar.py`

Responsável pela criação do ambiente utilizado nas simulações.

O módulo:

- Utiliza a matrícula do estudante como `seed`, garantindo a reprodução do mesmo ambiente a partir da mesma entrada.
- Gera uma grade de **12 × 12 posições**, representando o terreno do pomar.
- Define diferentes tipos de terreno e seus respectivos custos de movimentação:
  - **Solo livre / Carreador:** custo `1`;
  - **Solo encharcado:** custo `4`;
  - **Obstáculo:** posição inacessível.
- Gera os parâmetros estocásticos utilizados pelo sensor de detecção de pragas.

### 2. Algoritmos de Busca e Navegação

**Arquivos:** `src/buscas.py` e `src/busca_local.py`

Responsáveis pela navegação do agente pelo terreno e pela avaliação dos caminhos disponíveis.

O ambiente possui como:

- **Posição inicial:** `(0, 0)`
- **Destino:** `(11, 11)`

O projeto utiliza diferentes estratégias de busca para encontrar caminhos e comparar seus resultados, incluindo:

- Busca A*;
- Busca Gulosa;
- Busca Local;
- Subida de Encosta (*Hill Climbing*).

Os algoritmos consideram os custos de movimentação e as posições classificadas como obstáculos.

### 3. Diagnóstico Inteligente

**Arquivos:** `src/bayes.py` e `src/especialista.py`

Responsáveis pela análise probabilística e pela tomada de decisão relacionada à presença de pragas.

#### Inferência Bayesiana

O módulo `bayes.py` calcula a **probabilidade a posteriori** da presença de uma praga com base nas informações fornecidas pelo sensor.

Entre os parâmetros considerados estão:

- Probabilidade inicial da presença da praga;
- Sensibilidade do sensor;
- Especificidade do sensor;
- Resultado da leitura realizada.

#### Sistema Especialista

O módulo `especialista.py` utiliza um conjunto de **regras de inferência** para interpretar os resultados obtidos e recomendar ações de manejo agrícola.

---

## Estrutura do Repositório

```text
caatinga-ai-sprint1/
│
├── src/
│   ├── gerador_pomar.py    # Geração determinística do terreno e sensores
│   ├── buscas.py           # Algoritmos de busca informada e não informada
│   ├── busca_local.py      # Algoritmos de busca local
│   ├── bayes.py            # Módulo de inferência Bayesiana
│   ├── especialista.py     # Sistema especialista baseado em regras
│   └── main.py             # Ponto de entrada da aplicação
│
├── resultados/             # Mapas, gráficos e resultados das simulações
│
├── .gitignore              # Arquivos e diretórios ignorados pelo Git
│
└── README.md               # Documentação do projeto
```

---

## Requisitos

Para executar o projeto, é necessário possuir:

- **Python 3.10 ou superior**
- **Matplotlib**
- **Seaborn**

As dependências podem ser instaladas com:

```bash
pip install matplotlib seaborn
```

---

## Execução

### Gerador de Pomar

O gerador pode ser executado individualmente para gerar o terreno e os parâmetros do sensor a partir de uma matrícula.

```bash
python src/gerador_pomar.py 24114047
```

A matrícula utilizada como argumento funciona como `seed` para a geração determinística do ambiente.

### Sistema Completo

Para executar todas as etapas do sistema:

```bash
python src/main.py 24114047
```

O comando executa a geração do ambiente, os algoritmos de busca, a inferência Bayesiana e o sistema especialista.

Para utilizar outra matrícula, basta substituir o valor utilizado como argumento:

```bash
python src/main.py <matricula>
```

Os mapas, gráficos e demais resultados visuais gerados durante a execução são armazenados automaticamente no diretório:

```text
resultados/
```

---

## Resultados

A execução do sistema permite analisar os resultados obtidos nas diferentes etapas do projeto.

### Navegação

Os algoritmos de busca determinam caminhos entre a posição inicial `(0, 0)` e o destino `(11, 11)`, considerando os custos de movimentação e os obstáculos presentes no terreno.

### Diagnóstico

A inferência Bayesiana utiliza os resultados dos sensores para calcular a probabilidade a posteriori da presença de uma praga.

### Tomada de Decisão

O sistema especialista utiliza regras previamente definidas para interpretar o diagnóstico e determinar recomendações de manejo.

### Visualização

Os mapas do terreno, as rotas encontradas e os demais gráficos produzidos pela aplicação ficam disponíveis no diretório:

```text
resultados/
```

---

## Objetivo

O **Caatinga.AI** tem como objetivo demonstrar a aplicação integrada de diferentes técnicas de Inteligência Artificial em um cenário de agricultura.

O fluxo geral do sistema pode ser representado da seguinte forma:

```text
Geração do Ambiente
        ↓
Navegação e Busca
        ↓
Coleta de Informações
        ↓
Inferência Bayesiana
        ↓
Sistema Especialista
        ↓
Tomada de Decisão
```

O projeto reúne conceitos de **busca em espaços de estados, busca local, probabilidade Bayesiana e sistemas especialistas** em uma única aplicação.

> Versão 1.0 - Projeto Sprint 1