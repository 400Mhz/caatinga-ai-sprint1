import random
import math

def get_free_plots(grid):
    """Retorna todos os talhões que não estão bloqueados (#)."""
    free = []
    n = len(grid)
    for r in range(n):
        for c in range(n):
            if grid[r][c] != "#":
                free.append((r, c))
    return free

def objective_function(selected_plots, grid):
    """
    Função Objetivo: Maximiza o valor dos talhões inspecionados.
    Talhões encharcados (~) têm maior prioridade de inspeção (peso 4)
    que os carreadores (.), por acumularem mais humidade.
    """
    weights = {".": 1, "~": 4}
    return sum(weights[grid[r][c]] for r, c in selected_plots)

def get_neighbor_solution(current_solution, all_free_plots):
    """Gera uma solução vizinha trocando 1 talhão da solução por um fora dela."""
    neighbor = list(current_solution)
    idx_to_remove = random.randint(0, len(neighbor) - 1)
    
    available = list(set(all_free_plots) - set(neighbor))
    if not available:
        return neighbor
        
    new_plot = random.choice(available)
    neighbor[idx_to_remove] = new_plot
    return neighbor

def hill_climbing(grid, K=15, max_iter=500):
    """Subida de Encosta (Hill-Climbing)."""
    all_free = get_free_plots(grid)
    current_sol = random.sample(all_free, K)
    current_val = objective_function(current_sol, grid)

    for _ in range(max_iter):
        neighbor = get_neighbor_solution(current_sol, all_free)
        neighbor_val = objective_function(neighbor, grid)

        if neighbor_val > current_val:
            current_sol = neighbor
            current_val = neighbor_val

    return current_sol, current_val

def simulated_annealing(grid, K=15, initial_temp=100.0, cooling_rate=0.95, max_iter=500):
    """Têmpera Simulada (Simulated Annealing) - Aceita pioras temporárias para escapar de ótimos locais."""
    all_free = get_free_plots(grid)
    current_sol = random.sample(all_free, K)
    current_val = objective_function(current_sol, grid)

    best_sol = current_sol
    best_val = current_val

    temp = initial_temp

    for _ in range(max_iter):
        neighbor = get_neighbor_solution(current_sol, all_free)
        neighbor_val = objective_function(neighbor, grid)
        
        delta = neighbor_val - current_val

        # Aceita se for melhor ou se passar no teste de probabilidade de Boltzmann
        if delta > 0 or random.random() < math.exp(delta / temp):
            current_sol = neighbor
            current_val = neighbor_val

            if current_val > best_val:
                best_sol = current_sol
                best_val = current_val

        temp *= cooling_rate
        if temp < 1e-3:
            break

    return best_sol, best_val

def run_local_searches(grid, runs=30):
    """Executa os algoritmos 30 vezes e retorna métricas (média, desvio, melhor)."""
    hc_results = []
    sa_results = []

    for _ in range(runs):
        _, val_hc = hill_climbing(grid)
        _, val_sa = simulated_annealing(grid)
        hc_results.append(val_hc)
        sa_results.append(val_sa)

    def stats(data):
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = math.sqrt(variance)
        return round(mean, 2), round(std_dev, 2), max(data)

    hc_mean, hc_std, hc_best = stats(hc_results)
    sa_mean, sa_std, sa_best = stats(sa_results)

    return {
        "hill_climbing": {"media": hc_mean, "desvio": hc_std, "melhor": hc_best},
        "simulated_annealing": {"media": sa_mean, "desvio": sa_std, "melhor": sa_best}
    }