import os
import sys
import time
import pandas as pd
import matplotlib.pyplot as plt

from gerador_pomar import gerar_pomar, parametros_sensor
from buscas import bfs, dfs, ucs, a_star
from busca_local import run_local_searches
from especialista import test_expert_system
from bayes import calcular_bayes

def main():
    matricula = int(sys.argv[1]) if len(sys.argv) > 1 else 24114047
    print(f"=== CAATINGA.AI - Executando para a Matrícula: {matricula} ===")

    grid = gerar_pomar(matricula)
    params = parametros_sensor(matricula)

    os.makedirs("resultados", exist_ok=True)

    # 1. Grava pomar.txt[cite: 1]
    with open("resultados/pomar.txt", "w", encoding="utf-8") as f:
        f.write(f"{matricula}\n")
        for row in grid:
            f.write(" ".join(row) + "\n")

    # 2. Executa Procuras[cite: 1]
    estrategias = [
        ("BFS", lambda g: bfs(g)),
        ("DFS", lambda g: dfs(g)),
        ("UCS", lambda g: ucs(g)),
        ("A* (h1=0)", lambda g: a_star(g, 0.0)),
        ("A* (h2=Manhattan)", lambda g: a_star(g, 1.0)),
        ("A* (h3=4xManhattan)", lambda g: a_star(g, 4.0)),
    ]

    resultados = []
    for nome, func in estrategias:
        t0 = time.perf_counter()
        res = func(grid)
        t1 = time.perf_counter()
        tempo_ms = round((t1 - t0) * 1000, 2)

        resultados.append({
            "estrategia": nome,
            "custo": res["custo"],
            "passos": res["passos"],
            "nos_expandidos": res["nos_expandidos"],
            "fronteira_max": res["fronteira_max"],
            "tempo_ms": tempo_ms
        })

    df = pd.DataFrame(resultados)
    df.to_csv("resultados/resultados.csv", index=False)
    print("\n--- RESULTADOS DAS BUSCAS (Parte 2 e 3) ---")
    print(df.to_string(index=False))

    # 3. Gera grafico.png[cite: 1]
    plt.figure(figsize=(10, 5))
    plt.bar(df["estrategia"], df["nos_expandidos"], color="darkgreen")
    plt.xlabel("Estratégia de Busca")
    plt.ylabel("Nós Expandidos")
    plt.title(f"Nós Expandidos por Estratégia (Semente: {matricula})")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("resultados/grafico.png")
    plt.close()

    # 4. Busca Local (Parte 3.4)[cite: 1]
    print("\n--- BUSCA LOCAL (Parte 3.4) ---")
    local_results = run_local_searches(grid, runs=30)
    print(f"Hill-Climbing: {local_results['hill_climbing']}")
    print(f"Simulated Annealing: {local_results['simulated_annealing']}")

    # 5. Sistema Especialista (Parte 4.1)[cite: 1]
    print("\n--- SISTEMA ESPECIALISTA (Parte 4.1) ---")
    sucesso, traço = test_expert_system()
    print(f"Objetivo provado com sucesso? {sucesso}")
    print("Traço de Execução:")
    for t in traço:
        print("  ->", t)

    # 6. Teorema de Bayes (Parte 4.3)[cite: 1]
    print("\n--- TEOREMA DE BAYES (Parte 4.3) ---")
    res_bayes = calcular_bayes(params)
    print(f"Parâmetros: {params}")
    print(f"P(Infestado | Positivo): {res_bayes['p_infestado_pos']:.4f}")
    print(f"Alertas falsos a cada 100: {res_bayes['falsos_por_100']}")
    print(f"Alertas falsos/semana: {res_bayes['alertas_falsos_semana']}")
    print(f"Horas desperdiçadas/semana: {res_bayes['horas_perdidas']} h")

if __name__ == "__main__":
    main()