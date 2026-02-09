import pandas as pd
from datetime import datetime

# PROJETO: Gestão de Prazos Advocatícios / Pessoais
# CENÁRIO: Tenho uma lista de processos e preciso filtrar o que vence em Fevereiro de 2024 (ano bissexto).
# OBJETIVO: Nunca perder um prazo judicial.

def analisar_prazos():
    # Base de dados simulada (Ex: Exportação do sistema do tribunal ou planilha pessoal)
    dados = {
        'Numero_Processo': ['001-23.TJDF', '002-21.TJSP', '003-24.TRT', '004-23.TJDF', '005-22.STJ'],
        'Cliente': ['João Silva', 'Padaria Central', 'Maria Souza', 'Condomínio X', 'Pedro Rocha'],
        'Tipo_Prazo': ['Audiência', 'Recurso', 'Pagamento', 'Réplica', 'Sentença'],
        'Data_Vencimento': [
            '2024-02-15', # Dentro de Fev/24
            '2024-03-01', # Fora
            '2024-02-05', # Dentro e Urgente
            '2024-01-30', # Já passou (Atrasado!)
            '2024-02-29'  # Ano bissexto (data válida)
        ],
        'Status': ['Pendente', 'Pendente', 'Pendente', 'Concluido', 'Pendente']
    }

    df = pd.DataFrame(dados)
    
    # Convertendo a coluna de texto para formato de DATA real
    df['Data_Vencimento'] = pd.to_datetime(df['Data_Vencimento'])
    
    # Definindo o período de análise: Fevereiro de 2024
    inicio_mes = pd.Timestamp('2024-02-01')
    fim_mes = pd.Timestamp('2024-02-29')

    print("--- RELATÓRIO DE PRAZOS: FEVEREIRO 2024 ---")
    
    # FILTRO 1: Apenas o que vence em Fevereiro E está pendente
    prazos_fevereiro = df[
        (df['Data_Vencimento'] >= inicio_mes) & 
        (df['Data_Vencimento'] <= fim_mes) &
        (df['Status'] == 'Pendente')
    ].copy()

    # Calculando quantos dias faltam (simulando que hoje é 01/02/2024)
    hoje_simulado = pd.Timestamp('2024-02-01')
    prazos_fevereiro['Dias_Restantes'] = (prazos_fevereiro['Data_Vencimento'] - hoje_simulado).dt.days

    # Ordenando do mais urgente para o menos urgente
    prazos_fevereiro = prazos_fevereiro.sort_values(by='Data_Vencimento')

    # Exibindo resultado
    if not prazos_fevereiro.empty:
        for index, row in prazos_fevereiro.iterrows():
            print(f"URGÊNCIA: Faltam {row['Dias_Restantes']} dias")
            print(f"Processo: {row['Numero_Processo']} | Cliente: {row['Cliente']}")
            print(f"Ação: {row['Tipo_Prazo']} | Data: {row['Data_Vencimento'].strftime('%d/%m/%Y')}")
            print("-" * 30)
    else:
        print("Nenhum prazo pendente para este mês.")

if __name__ == "__main__":
    analisar_prazos()
