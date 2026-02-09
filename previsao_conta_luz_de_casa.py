# PROJETO: Simulador de Conta de Luz
# OBJETIVO: Ler o medidor hoje e prever quanto vou pagar no fim do mês.

def calcular_previsao_conta(leitura_anterior, leitura_atual, dias_decorridos):
    # Tarifas fictícias de Brasília (CEB/Neoenergia)
    TARIFA_KWH = 0.75 
    BANDEIRA_AMARELA_EXTRA = 0.02 # Extra por kWh
    
    consumo_atual = leitura_atual - leitura_anterior
    media_diaria = consumo_atual / dias_decorridos
    
    # Projetando para 30 dias
    previsao_mensal_kwh = media_diaria * 30
    valor_base = previsao_mensal_kwh * TARIFA_KWH
    
    # Lógica da Bandeira Tarifária (Se gastar muito, paga extra)
    adicional_bandeira = 0
    cor_bandeira = "VERDE"
    
    if previsao_mensal_kwh > 200: # Se gastar mais que 200kWh
        cor_bandeira = "AMARELA"
        adicional_bandeira = previsao_mensal_kwh * BANDEIRA_AMARELA_EXTRA

    valor_total = valor_base + adicional_bandeira

    print(f"--- RELATÓRIO DE CONSUMO ---")
    print(f"Consumo em {dias_decorridos} dias: {consumo_atual} kWh")
    print(f"Média diária: {media_diaria:.2f} kWh")
    print(f"----------------------------")
    print(f"PREVISÃO P/ FIM DO MÊS (30 dias): {previsao_mensal_kwh:.0f} kWh")
    print(f"Bandeira Prevista: {cor_bandeira}")
    print(f"Valor Estimado da Conta: R$ {valor_total:.2f}")

    if cor_bandeira == "AMARELA":
        print("DICA: Tente reduzir o banho quente para voltar à bandeira Verde!")

if __name__ == "__main__":
    # Exemplo: Medidor marcava 1000 no dia 1. Hoje é dia 15 e marca 1120.
    calcular_previsao_conta(leitura_anterior=1000, leitura_atual=1120, dias_decorridos=15)
