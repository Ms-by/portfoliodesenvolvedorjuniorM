-- Script de criação e consulta para Relatórios Gerenciais

-- 1. Criação da Tabela de Vendas
CREATE TABLE Vendas (
    ID_Venda INT PRIMARY KEY,
    Data_Venda DATE,
    Vendedor VARCHAR(100),
    Valor_Total DECIMAL(10,2),
    Status_Pagamento VARCHAR(20)
);

-- 2. Query para Relatório de Performance (Total vendido por Vendedor)
-- Objetivo: Identificar quem bateu a meta no mês
SELECT 
    Vendedor,
    COUNT(ID_Venda) AS Total_Vendas,
    SUM(Valor_Total) AS Faturamento_Total
FROM 
    Vendas
WHERE 
    Status_Pagamento = 'Aprovado'
    AND Data_Venda BETWEEN '2025-01-01' AND '2025-01-31'
GROUP BY 
    Vendedor
ORDER BY 
    Faturamento_Total DESC;

-- 3. Query para Auditoria (Identificar vendas canceladas acima de R$ 1000)
SELECT * FROM Vendas
WHERE Status_Pagamento = 'Cancelado' 
AND Valor_Total > 1000.00;
