-- CENÁRIO: Controle Financeiro Doméstico
-- PERGUNTA: "Por que minha compra do mês ficou mais cara se comprei as mesmas coisas?"

-- 1. Tabela de Compras (Histórico)
CREATE TABLE Compras_Mercado (
    ID INT,
    Mes_Referencia VARCHAR(10), -- Ex: 'Jan/24', 'Fev/24'
    Produto VARCHAR(50),
    Preco_Unitario DECIMAL(10,2),
    Quantidade INT
);

-- 2. Inserindo dados (Janeiro vs Fevereiro)
INSERT INTO Compras_Mercado VALUES 
(1, 'Jan/24', 'Arroz 5kg', 25.00, 2),
(2, 'Jan/24', 'Azeite', 30.00, 1),
(3, 'Jan/24', 'Carne 1kg', 40.00, 3),
(4, 'Fev/24', 'Arroz 5kg', 28.00, 2), -- Aumentou
(5, 'Fev/24', 'Azeite', 35.00, 1), -- Aumentou muito
(6, 'Fev/24', 'Carne 1kg', 38.00, 3); -- Baixou

-- 3. QUERY: Relatório de Inflação Pessoal
-- Compara o mesmo produto em meses diferentes para ver quanto aumentou (%)

SELECT 
    A.Produto,
    A.Preco_Unitario AS Preco_Janeiro,
    B.Preco_Unitario AS Preco_Fevereiro,
    
    -- Cálculo da Diferença em Reais
    (B.Preco_Unitario - A.Preco_Unitario) AS Aumento_Reais,
    
    -- Cálculo da Porcentagem de Aumento
    CAST(((B.Preco_Unitario - A.Preco_Unitario) / A.Preco_Unitario * 100) AS DECIMAL(10,1)) AS Inflacao_Pct
    
FROM 
    Compras_Mercado A
INNER JOIN 
    Compras_Mercado B ON A.Produto = B.Produto
WHERE 
    A.Mes_Referencia = 'Jan/24' 
    AND B.Mes_Referencia = 'Fev/24'
ORDER BY 
    Inflacao_Pct DESC; -- Mostra os "vilões" da inflação primeiro
