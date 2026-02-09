import pandas as pd

# Simulação: Automação para conferência de pagamentos e prevenção de perdas
# Cenário: Recebemos uma planilha de pagamentos e precisamos evitar pagar a mesma nota duas vezes.

def verificar_duplicidade(arquivo_pagamentos):
    try:
        # Lendo os dados (simulando um arquivo Excel ou CSV)
        # Em um cenário real: df = pd.read_excel(arquivo_pagamentos)
        
        # Criando dados fictícios para demonstração
        dados = {
            'ID_Transacao': [101, 102, 103, 104, 105],
            'Fornecedor': ['Empresa A', 'Empresa B', 'Empresa A', 'Empresa C', 'Empresa B'],
            'Valor': [1500.00, 3000.00, 1500.00, 500.00, 3000.00],
            'Nota_Fiscal': ['NF-001', 'NF-002', 'NF-001', 'NF-003', 'NF-002'] # Note que NF-001 e NF-002 estão duplicadas
        }
        
        df = pd.DataFrame(dados)
        
        print("--- Analisando Base de Dados ---")
        print(df)
        print("\n--------------------------------")

        # Lógica para encontrar duplicatas baseada em 'Fornecedor', 'Valor' e 'Nota_Fiscal'
        duplicadas = df[df.duplicated(subset=['Fornecedor', 'Valor', 'Nota_Fiscal'], keep=False)]

        if not duplicadas.empty:
            print(f"ALERTA: Foram encontradas {len(duplicadas)} transações suspeitas de duplicidade!")
            print("Relatório de Risco Gerado:")
            print(duplicadas)
            # Aqui poderia entrar uma automação para enviar e-mail para o gestor
        else:
            print("Sucesso: Nenhuma duplicidade encontrada. Pagamentos liberados.")

    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

# Execução do script
if __name__ == "__main__":
    verificar_duplicidade("pagamentos_fevereiro.xlsx")
