import pandas as pd

# SISTEMA DE MANUTENÇÃO PREVENTIVA
# Objetivo: Identificar veículos que atingiram o limite de KM para revisão.
# Baseado na regra real: Revisão a cada 10.000km.

def verificar_frota():
    # Simulando dados vindos do banco de dados
    frota = [
        {'Placa': 'ABC-1234', 'Modelo': 'Onix', 'Km_Atual': 10500, 'Ultima_Revisao_Km': 0},     # Precisa (passou 500km)
        {'Placa': 'XYZ-9876', 'Modelo': 'Mobi', 'Km_Atual': 5200,  'Ultima_Revisao_Km': 0},     # Não precisa
        {'Placa': 'DEF-5555', 'Modelo': 'Jeep', 'Km_Atual': 21000, 'Ultima_Revisao_Km': 10000}, # Precisa (passou 1000km da última)
    ]
    
    # Transformando em DataFrame (Tabela)
    df = pd.DataFrame(frota)
    
    print("--- RELATÓRIO DE MANUTENÇÃO ---")
    
    # Criando coluna de Próxima Revisão (Lógica Matemática)
    # A revisão é feita na última revisão + 10.000km
    df['Proxima_Revisao'] = df['Ultima_Revisao_Km'] + 10000
    
    # Verificando quem estourou o limite
    df['Status'] = df.apply(
        lambda x: 'ALERTA: REVISÃO' if x['Km_Atual'] >= x['Proxima_Revisao'] else 'OK', 
        axis=1
    )
    
    # Exibindo apenas os carros críticos
    carros_criticos = df[df['Status'] == 'ALERTA: REVISÃO']
    
    if not carros_criticos.empty:
        print(f"ATENÇÃO: {len(carros_criticos)} veículos precisam parar imediatamente.")
        print(carros_criticos[['Placa', 'Modelo', 'Km_Atual', 'Status']])
    else:
        print("Toda a frota está em dia.")

if __name__ == "__main__":
    verificar_frota()
