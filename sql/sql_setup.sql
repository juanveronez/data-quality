CREATE OR REPLACE TABLE produtos_bronze (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    preco FLOAT NOT NULL,
    categoria VARCHAR(255) NOT NULL
);

CREATE OR REPLACE TABLE produtos_bronze_email (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    preco FLOAT NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

INSERT INTO produtos_bronze_email (nome, quantidade, preco, categoria, email) VALUES
('Produto A', 100, 10.0, 'eletronicos','produtoA@example.com' ),
('Produto B', 150, 20.0, 'mobilia', 'produtoA@example.com'),
('Produto C', 200, 15.0, 'informatica', 'produtoA@example.com'),
('Produto D', 50, 5.0, 'decoracao', 'produtoA@example.com'),
('Produto E', 120, 22.0, 'eletronicos', 'produtoA@example.com'),
('Produto F', 80, 45.0, 'mobilia', 'produtoA@example.com'),
('Produto G', 60, 120.0, 'informatica', 'produtoA@example.com'),
('Produto H', 30, 85.0, 'decoracao', 'produtoA@example.com'),
('Produto I', 90, 55.0, 'eletronicos', 'produtoA@example.com'),
('Produto J', 20, 100.0, 'mobilia', 'produtoA@example.com');

INSERT INTO produtos_bronze (nome, quantidade, preco, categoria) VALUES
('Produto A', 100, 10.0, 'eletronicos'),
('Produto B', 150, 20.0, 'mobilia'),
('Produto C', 200, 15.0, 'informatica'),
('Produto D', 50, 5.0, 'decoracao'),
('Produto E', 120, 22.0, 'eletronicos'),
('Produto F', 80, 45.0, 'mobilia'),
('Produto G', 60, 120.0, 'informatica'),
('Produto H', 30, 85.0, 'decoracao'),
('Produto I', 90, 55.0, 'eletronicos'),
('Produto J', 20, 100.0, 'mobilia');

INSERT INTO produtos_bronze (nome, quantidade, preco, categoria) VALUES
('Produto A', 100, 10.0, 'eletronicos'),
('Produto B', -150, 20.0, 'mobilia'),
('Produto C', 200, 15.0, 'informatica'),
('Produto D', 50, 5.0, 'decoracao'),
('Produto E', 120, 22.0, 'eletronicos'),
('Produto F', 80, 45.0, 'mobilia'),
('Produto G', 60, 120.0, 'informatica'),
('Produto H', 30, 85.0, 'decoracao'),
('Produto I', 90, 55.0, 'eletronicos'),
('Produto J', 20, 100.0, 'mobilia');