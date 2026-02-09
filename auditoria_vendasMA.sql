-- CENÁRIO: Auditoria de Vendas e Rankeamento de Vendedores
-- OBJETIVO: Não apenas somar vendas, mas comparar o vendedor com o colega logo abaixo dele.

-- 1. Criação da Tabela para Exemplo
CREATE TABLE Vendas_Mensais (
    Mes INT,
    Vendedor VARCHAR(50),
    Total_Vendido DECIMAL(10,2)
);

-- 2. Inserção de Dados Simulados
INSERT INTO Vendas_Mensais VALUES 
(1, 'Marcos', 15000), (1, 'Ana', 22000), (1, 'João', 12000),
(2, 'Marcos', 18000), (2, 'Ana', 21000), (2, 'João', 19000);

-- 3. QUERY AVANÇADA (O "Pulo do Gato")
-- Uso de RANK() para classificar e LAG() para comparar com o mês anterior
SELECT 
    Mes,
    Vendedor,
    Total_Vendido,
    
    -- Cria um ranking (1º, 2º, 3º) dentro de cada mês
    RANK() OVER (PARTITION BY Mes ORDER BY Total_Vendido DESC) as Ranking_Mes,
    
    -- Pega o valor que esse mesmo vendedor vendeu na linha anterior (mês passado)
    LAG(Total_Vendido, 1, 0) OVER (PARTITION BY Vendedor ORDER BY Mes) as Venda_Mes_Anterior,
    
    -- Calcula o crescimento % em relação ao mês anterior (Cálculo direto no SQL)
    (Total_Vendido - LAG(Total_Vendido, 1, 0) OVER (PARTITION BY Vendedor ORDER BY Mes)) as Crescimento_Real
    
FROM 
    Vendas_Mensais
ORDER BY 
    Mes, Ranking_Mes;
