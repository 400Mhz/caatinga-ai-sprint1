def calcular_bayes(params):
    prev = params["prevalencia"]
    sens = params["sensibilidade"]
    fp = params["taxa_falso_positivo"]
    talhoes_semana = params["talhoes_por_semana"]

    p_positivo = (sens * prev) + (fp * (1 - prev))
    p_infestado_pos = (sens * prev) / p_positivo
    taxa_falsos_alertas = 1 - p_infestado_pos
    
    alertas_falsos_semana = (talhoes_semana * p_positivo) * taxa_falsos_alertas
    horas_perdidas = (alertas_falsos_semana * 12) / 60

    return {
        "p_infestado_pos": p_infestado_pos,
        "falsos_por_100": round(taxa_falsos_alertas * 100, 2),
        "alertas_falsos_semana": round(alertas_falsos_semana, 2),
        "horas_perdidas": round(horas_perdidas, 2)
    }