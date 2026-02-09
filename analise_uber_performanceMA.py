import pandas as pd
import random
from datetime import datetime, timedelta

# PROJETO: Otimização de Ganhos para Motoristas de App
# OBJETIVO: Analisar histórico de corridas para descobrir quais horários pagam mais por km rodado.
# CURIOSIDADE: "Como autodidata, usei Python para responder: vale a pena trabalhar de madrugada?"

def gerar_dados_ficticios():
    # Simulando um CSV exportado do aplicativo
    dados = []
    data_inicial = datetime(2024, 1, 1)
    
    for _ in range(100): # 100 corridas
        hora = random.randint(0, 23)
        distancia = round(random.uniform(2.0, 25.0), 1)
        # Lógica: De madrugada e horário de pico é mais caro
        tarifa_base = 1.5
        if 6 <= hora <= 9 or 17 <= hora <= 19: multiplicador = 2.0
        elif 0 <= hora <= 5: multiplicador = 1.8
        else: multiplicador = 1.2
        
        valor = round(distancia * tarifa_base * multiplicador, 2)
        tempo = round(distancia * 2.5, 0) # minutos
        
        dados.append({
            "Data": data_inicial + timedelta(hours=hora),
            "Hora_Dia": hora,
            "Distancia_KM": distancia,
            "Valor_Recebido": valor,
            "Tempo_Min": tempo
        })
    return pd.DataFrame(dados)

def analisar_performance():
    df = gerar_dados_ficticios()
    
    # Criando métrica nova: Valor por KM (Eficiência)
    df['Valor_por_KM'] = df['Valor_Recebido'] / df['Distancia_KM']
    
    print("--- AMOSTRA DOS DADOS ---")
    print(df.head())
    
    print("\n--- MÉDIA DE GANHO POR FAIXA DE HORÁRIO ---")
    # Agrupando por hora para ver qual horário rende mais
    analise_hora = df.groupby('Hora_Dia')[['Valor_Recebido', 'Valor_por_KM']].mean()
    
    # Ordenando para pegar os TOP 5 melhores horários
    melhores_horarios = analise_hora.sort_values(by='Valor_por_KM', ascending=False).head(5)
    
    print(melhores_horarios)
    
    print(f"\nCONCLUSÃO: O horário mais lucrativo paga em média R$ {melhores_horarios.iloc[0]['Valor_por_KM']:.2f} por KM.")

if __name__ == "__main__":
    analisar_performance()
