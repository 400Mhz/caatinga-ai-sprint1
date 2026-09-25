```markdown
# caatinga-ai-sprint1


Projeto desenvolvido para a disciplina de Inteligência Artificial do Centro Universitário Rio Salgado (UniRios). O sistema simula a navegação autônoma e o diagnóstico preventivo de pragas em um pomar na região da Caatinga, utilizando técnicas de Busca em Grafos, Inferência Bayesiana e Sistemas Especialistas.

```

---

## 👥 Integrantes da Equipe

* **Antônio Oliveira** — Matrícula: `24114073`
* **Tony Carlos** — Matrícula: `24114047`

---

## 📌 Visão Geral do Projeto

O **Caatinga.AI** é dividido em três pilares principais:

1. **Geração do Terreno e Sensores (`gerador_pomar.py`):**
* Utiliza a matrícula do estudante como semente determinística (`seed`) para gerar uma grelha $12 \times 12$ representando o terreno do pomar.
* Modela custos de movimentação: Solo Livre/Carreador (Custo 1), Solo Encharcado (Custo 4) e Obstáculos (Inacessível).
* Fornece os parâmetros estocásticos do sensor para análise de pragas.


2. **Algoritmos de Busca e Navegação (`buscas.py` & `busca_local.py`):**
* Determina a melhor rota entre a entrada `(0,0)` e o ponto de coleta `(11,11)`.
* Avalia a eficiência de algoritmos de busca (ex.: Busca A*, Gulosa, Subida de Encosta / Hill Climbing).


3. **Diagnóstico Inteligente (`bayes.py` & `especialista.py`):**
* **Rede Bayesiana:** Calcula a probabilidade *a posteriori* de presença de praga com base na sensibilidade e especificidade do sensor.
* **Sistema Especialista:** Aplica regras de inferência para recomendar ações de manejo agrícola sustentável.



---

## 📁 Estrutura do Repositório

```text
caatinga-ai-sprint1/
├── src/
│   ├── gerador_pomar.py   # Gerador determinístico da grelha e sensores
│   ├── buscas.py          # Algoritmos de busca informada e não informada
│   ├── busca_local.py    # Algoritmos de busca local
│   ├── bayes.py          # Módulo de inferência bayesiana
│   ├── especialista.py   # Sistema especialista baseado em regras
│   └── main.py           # Script principal de execução
├── resultados/            # Gráficos e mapas gerados das rotas
├── .gitignore             # Arquivos ignorados pelo Git (__pycache__, etc.)
└── README.md              # Documentação do projeto

```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

* Python 3.10 ou superior instalado.
* Dependências necessárias (instalar via terminal):

```bash
pip install matplotlib seaborn

```

### 1. Testar o Gerador de Pomar (Execução Independente)

Para testar a geração da grelha $12 \times 12$ e os parâmetros do sensor para uma matrícula específica:

```bash
python src/gerador_pomar.py 24114047

```

### 2. Executar o Sistema Completo

Para rodar a busca de caminhos, cálculo bayesiano e regras do sistema especialista com geração dos resultados gráficos:

```bash
python src/main.py 24114047

```

*Os mapas de rotas e gráficos gerados serão salvos automaticamente na pasta `resultados/`.*

---

## 📊 Principais Resultados

* **Caminho Otimizado:** A busca encontrou o trajeto de menor custo evitando zonas encharcadas e obstáculos.
* **Diagnóstico da Praga:** A probabilidade *a posteriori* foi calculada com precisão com base nas leituras estocásticas do sensor.
* **Saídas Visuais:** Os mapas do terreno e as rotas encontradas estão disponíveis na pasta `resultados/`.

```

```