CREATE DATABASE academic
    DEFAULT CHARACTER SET = 'utf8mb4';

USE academic

CREATE TABLE Cursos (
    cursoID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE Materia (
    materiaID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cursoID INT,
    CONSTRAINT fk_materia_curso
        FOREIGN KEY (cursoID)
        REFERENCES Cursos(cursoID)
        ON UPDATE CASCADE
        ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE Turma (
    turmaID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    ano VARCHAR(10) NOT NULL,
    cursoID INT NOT NULL,
    CONSTRAINT fk_turma_curso
        FOREIGN KEY (cursoID)
        REFERENCES Cursos(cursoID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE Matricula (
    matriculaID INT AUTO_INCREMENT PRIMARY KEY,
    numero_matricula INT UNIQUE,
    data_matricula DATE NOT NULL,
    turmaID INT NOT NULL,
    CONSTRAINT fk_matricula_turma
        FOREIGN KEY (turmaID)
        REFERENCES Turma(turmaID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE alunos (
    alunoID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    endereco VARCHAR(255),
    data_nascimento DATE,
    matriculaID INT NOT NULL,
    CONSTRAINT fk_aluno_matricula
        FOREIGN KEY (matriculaID)
        REFERENCES Matricula(matriculaID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE INDEX idx_alunos_name ON alunos(name);

CREATE TABLE Nota (
    notaID INT AUTO_INCREMENT PRIMARY KEY,
    nota DECIMAL(4,2) NOT NULL,
    materiaID INT NOT NULL,
    alunoID INT NOT NULL,
    CONSTRAINT fk_nota_materia
        FOREIGN KEY (materiaID)
        REFERENCES Materia(materiaID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_nota_aluno
        FOREIGN KEY (alunoID)
        REFERENCES alunos(alunoID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE=InnoDB;


