CREATE TABLE Cursos (
    cursoID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Materia (
    materiaID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cursoID INT,
    CONSTRAINT fk_materia_curso
        FOREIGN KEY (cursoID)
        REFERENCES Cursos(cursoID)
);

CREATE TABLE Turma (
    turmaID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    ano VARCHAR(10) NOT NULL,
    cursoID INT NOT NULL,
    CONSTRAINT fk_turma_curso
        FOREIGN KEY (cursoID)
        REFERENCES Cursos(cursoID)
);

CREATE TABLE Matricula (
    matriculaID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    numero_matricula INT GENERATED ALWAYS AS IDENTITY UNIQUE,
    data_matricula DATE NOT NULL,
    turmaID INT NOT NULL,
    CONSTRAINT fk_matricula_turma
        FOREIGN KEY (turmaID)
        REFERENCES Turma(turmaID)
);

CREATE TABLE alunos (
    alunoID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    endereco VARCHAR(255),
    data_nascimento DATE,
    matriculaID INT NOT NULL,
    CONSTRAINT fk_aluno_matricula
        FOREIGN KEY (matriculaID)
        REFERENCES Matricula(matriculaID)
);

CREATE INDEX idx_alunos_name ON alunos(name);

CREATE TABLE Nota (
    notaID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nota NUMERIC(4,2) NOT NULL,
    materiaID INT NOT NULL,
    alunoID INT NOT NULL,
    CONSTRAINT fk_nota_materia
        FOREIGN KEY (materiaID)
        REFERENCES Materia(materiaID),
    CONSTRAINT fk_nota_aluno
        FOREIGN KEY (alunoID)
        REFERENCES alunos(alunoID)
);

