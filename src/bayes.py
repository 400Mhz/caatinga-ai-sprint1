def calcular_bayes(params):
    # Obtém os parâmetros necessários para o cálculo
    prev = params["prevalencia"]
    sens = params["sensibilidade"]
    fp = params["taxa_falso_positivo"]
    talhoes_semana = params["talhoes_por_semana"]

    # Calcula a probabilidade de o sensor apresentar resultado positivo
    p_positivo = (sens * prev) + (fp * (1 - prev))

    # Calcula a probabilidade de existir infestação dado um resultado positivo
    p_infestado_pos = (sens * prev) / p_positivo

    # Calcula a taxa de resultados positivos que são falsos alertas
    taxa_falsos_alertas = 1 - p_infestado_pos
    
    # Calcula quantos falsos alertas são gerados por semana
    alertas_falsos_semana = (talhoes_semana * p_positivo) * taxa_falsos_alertas

    # Converte o número de falsos alertas em horas perdidas
    horas_perdidas = (alertas_falsos_semana * 12) / 60

    # Retorna os resultados calculados e arredondados
    return {
        "p_infestado_pos": p_infestado_pos,
        "falsos_por_100": round(taxa_falsos_alertas * 100, 2),
        "alertas_falsos_semana": round(alertas_falsos_semana, 2),
        "horas_perdidas": round(horas_perdidas, 2)
    }