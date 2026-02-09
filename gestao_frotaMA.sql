-- BANCO DE DADOS: GESTÃO DE FROTA
-- Simulação da estrutura de dados usada em grandes locadoras

-- 1. Tabela de Veículos (Cadastro da Frota)
CREATE TABLE Veiculos (
    ID_Carro INT PRIMARY KEY AUTO_INCREMENT,
    Modelo VARCHAR(50),
    Placa VARCHAR(10) UNIQUE,
    Grupo_Categoria VARCHAR(1) CHECK (Grupo_Categoria IN ('A', 'B', 'C', 'SUV')),
    Status_Atual VARCHAR(20) DEFAULT 'Disponivel', -- Disponivel, Alugado, Manutencao
    Km_Atual INT,
    Ultima_Revisao DATE
);

-- 2. Tabela de Histórico de Locações
CREATE TABLE Locacoes (
    ID_Locacao INT PRIMARY KEY AUTO_INCREMENT,
    ID_Carro INT,
    Data_Retirada DATETIME,
    Data_Devolucao DATETIME,
    Valor_Total DECIMAL(10,2),
    FOREIGN KEY (ID_Carro) REFERENCES Veiculos(ID_Carro)
);

-- 3. INSERINDO DADOS DE TESTE (CENÁRIO REAL)
INSERT INTO Veiculos (Modelo, Placa, Grupo_Categoria, Status_Atual, Km_Atual) VALUES 
('Fiat Mobi', 'BRA-2E19', 'A', 'Alugado', 12000),
('HB20 Sedan', 'GOL-4040', 'B', 'Disponivel', 45000),
('Jeep Renegade', 'SUV-9090', 'SUV', 'Manutencao', 80000);

-- 4. QUERY DE OPERAÇÃO: "Quais carros posso alugar AGORA do grupo B?"
-- O atendente precisa dessa info em segundos.
SELECT * FROM Veiculos 
WHERE Grupo_Categoria = 'B' 
AND Status_Atual = 'Disponivel';

-- 5. QUERY GERENCIAL: Taxa de Ocupação da Frota
-- Qual % da minha frota está gerando dinheiro agora?
SELECT 
    Status_Atual,
    COUNT(*) as Quantidade,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Veiculos)) as Porcentagem
FROM Veiculos
GROUP BY Status_Atual;
