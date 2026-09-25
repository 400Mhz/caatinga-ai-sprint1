class Rule:
    def __init__(self, rule_id, conditions, conclusion):
        self.rule_id = rule_id
        self.conditions = conditions  # Lista de tuplas (fato, valor)
        self.conclusion = conclusion  # Tupla (fato, valor)

class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules
        self.execution_trace = []

    def backward_chaining(self, goal, facts):
        """
        Encadeamento para trás: Tenta provar se o objetivo (goal) é verdadeiro com base nos fatos e regras.
        """
        goal_fact, goal_val = goal

        # Se o fato já é conhecido na base de conhecimento
        if facts.get(goal_fact) == goal_val:
            return True, [f"Fato conhecido: {goal_fact} = {goal_val}"]

        # Procura regras que resultam no objetivo desejado
        for rule in self.rules:
            if rule.conclusion == goal:
                self.execution_trace.append(f"Avaliando Regra {rule.rule_id} para provar {goal_fact} = {goal_val}")
                all_conditions_met = True
                sub_traces = []

                for cond_fact, cond_val in rule.conditions:
                    satisfied, trace = self.backward_chaining((cond_fact, cond_val), facts)
                    sub_traces.extend(trace)
                    if not satisfied:
                        all_conditions_met = False
                        break

                if all_conditions_met:
                    msg = f"Regra {rule.rule_id} APLICADA -> {rule.conclusion[0]} = {rule.conclusion[1]}"
                    self.execution_trace.append(msg)
                    facts[goal_fact] = goal_val
                    return True, self.execution_trace

        return False, [f"Não foi possível provar {goal_fact} = {goal_val}"]

def get_expert_rules():
    """Define as 6 regras SE-ENTÃO para maneio do talhão."""
    rules = [
        Rule("R1", [("sensor_positivo", True), ("umidade_alta", True)], ("prioridade_inspecao", "ALTA")),
        Rule("R2", [("dias_sem_inspecao", 15), ("prioridade_inspecao", "ALTA")], ("acao_recomendada", "PULVERIZAR_URGENTE")),
        Rule("R3", [("sensor_positivo", False), ("historico_pragas", False)], ("prioridade_inspecao", "BAIXA")),
        Rule("R4", [("prioridade_inspecao", "BAIXA")], ("acao_recomendada", "MONITORAR")),
        Rule("R5", [("tipo_terreno", "~"), ("temperatura_alta", True)], ("umidade_alta", True)),
        Rule("R6", [("sensor_positivo", True), ("umidade_alta", False)], ("prioridade_inspecao", "MEDIA")),
    ]
    return rules

def test_expert_system():
    rules = get_expert_rules()
    engine = InferenceEngine(rules)

    # Exemplo de fatos do talhão
    facts = {
        "sensor_positivo": True,
        "tipo_terreno": "~",
        "temperatura_alta": True,
        "dias_sem_inspecao": 15,
        "historico_pragas": False
    }

    goal = ("acao_recomendada", "PULVERIZAR_URGENTE")
    success, trace = engine.backward_chaining(goal, facts)
    return success, trace