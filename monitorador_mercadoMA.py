import pandas as pd
# Nota: Em um projeto real, usariamos 'import yfinance as yf' para dados reais da bolsa
# Aqui, simularemos a estrutura para não depender de instalação de pacotes externos no teste

class AnalisadorBolsa:
    def __init__(self):
        self.carteira = {
            'PETR4': [30.50, 31.00, 29.80, 32.10, 33.00], # Histórico de 5 dias
            'VALE3': [68.00, 67.50, 66.00, 69.00, 70.20],
            'ITUB4': [32.00, 32.10, 32.05, 31.90, 31.80]
        }
    
    def calcular_volatilidade(self):
        print("\n--- ANÁLISE DE RISCO (VOLATILIDADE) ---")
        """
        CURIOSIDADE TÉCNICA:
        Aqui calculamos o Desvio Padrão para entender qual ação oscila mais.
        Ativos muito voláteis são mais arriscados.
        """
        resultados = []
        
        for acao, precos in self.carteira.items():
            serie = pd.Series(precos)
            media = serie.mean()
            desvio_padrao = serie.std()
            variacao_pct = ((precos[-1] - precos[0]) / precos[0]) * 100
            
            resultados.append({
                'Acao': acao,
                'Preco_Atual': precos[-1],
                'Variacao_%': round(variacao_pct, 2),
                'Risco_Volatilidade': round(desvio_padrao, 4)
            })
            
        df_resultados = pd.DataFrame(resultados)
        
        # Lógica de Decisão: Recomendação simples baseada em alta do papel
        df_resultados['Recomendacao'] = df_resultados['Variacao_%'].apply(
            lambda x: 'COMPRA FORTE' if x > 5 else ('MANTER' if x > 0 else 'VENDER')
        )
        print(df_resultados)

if __name__ == "__main__":
    bot = AnalisadorBolsa()
    bot.calcular_volatilidade()
