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
    imagem VARCHAR(256)
);

CREATE TABLE livro(
	titulo VARCHAR(256),
    id INT PRIMARY KEY NOT NULL,
    autor VARCHAR(256),
    capa VARCHAR(256)
);