DROP DATABASE cafe;
CREATE DATABASE cafe;
USE cafe;

CREATE TABLE usuario(
	usuario VARCHAR(256) PRIMARY KEY NOT NULL,
    senha VARCHAR(256)
);

CREATE TABLE produto(
	nome VARCHAR(50),
    id INT PRIMARY KEY NOT NULL,
    preco DOUBLE,
    categoria INT
);

CREATE TABLE livro(
	titulo VARCHAR(256),
    id INT PRIMARY KEY NOT NULL,
    autor VARCHAR(256),
    edicao VARCHAR(256)
);

CREATE TABLE doacao(
	titulo VARCHAR(256),
    id INT PRIMARY KEY NOT NULL,
    autor VARCHAR(256),
    edicao VARCHAR(256)
);

INSERT INTO usuario (usuario, senha) VALUES ("bea", "bea");