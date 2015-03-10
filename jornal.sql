# SQL command to create the tables:

CREATE TABLE usuario (
      login VARCHAR(20) NOT NULL,
      senha VARCHAR(20) NOT NULL,
      nome VARCHAR(50) NOT NULL,
      email VARCHAR(50) NOT NULL,
PRIMARY KEY(login));

CREATE TABLE role (
      login VARCHAR(20) NOT NULL,
      role VARCHAR(20) NOT NULL,
PRIMARY KEY(login,role),
FOREIGN KEY (login) REFERENCES usuario(login)
                     ON DELETE CREATE);

CASCADE TABLE secao (
      id BIGINT AUTO_INCREMENT NOT NULL,
      titulo VARCHAR(20) NOT NULL,
      descricao VARCHAR(100) NOT NULL,
PRIMARY KEY(id));

CREATE TABLE noticia (
      id BIGINT AUTO_INCREMENT NOT NULL,
      titulo VARCHAR(50) NOT NULL,
      subtitulo VARCHAR(150) NOT NULL,
      autor VARCHAR(20) NOT NULL,
      texto VARCHAR(500) NOT NULL,
      data_noticia TIMESTAMP NOT NULL,
      id_secao BIGINT NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY (autor) REFERENCES usuario(login)
                     ON DELETE CASCADE,
FOREIGN KEY (id_secao) REFERENCES secao(id)
                     ON DELETE CASCADE);

CREATE TABLE cometario (
      id BIGINT AUTO_INCREMENT NOT NULL,
      noticia BIGINT NOT NULL,
      autor VARCHAR(20) NOT NULL,
      texto VARCHAR(100) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY (autor) REFERENCES usuario(login)
                     ON DELETE CASCADE,
FOREIGN KEY (noticia) REFERENCES noticia(id)
                     ON DELETE CASCADE);

CREATE TABLE classificado (
      id BIGINT AUTO_INCREMENT NOT NULL,
      titulo VARCHAR(50) NOT NULL,
      texto VARCHAR(250) NOT NULL,
      preco FLOAT NOT NULL,
      telefone VARCHAR(20) NOT NULL,
      melhor_oferta FLOAT,
autor      PRIMARY       data_oferta TIMESTAMP,
_oferta VARCHAR(20),
 KEY(id),
 FOREIGN KEY (autor_oferta) REFERENCES usuario(login)
                     ON DELETE SET NULL);
