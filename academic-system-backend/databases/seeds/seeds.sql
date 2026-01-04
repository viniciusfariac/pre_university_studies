INSERT INTO Cursos (name) VALUES
('Análise e Desenvolvimento de Sistemas'),
('Ciência da Computação');

INSERT INTO Materia (name, cursoID) VALUES
('Banco de Dados', 1),
('Algoritmos', 1),
('Arquitetura Computacional', 1),
('Linguagens de Programação', 1),
('Cálculo Computacional', 1),
('Estatística', 1);

INSERT INTO Turma (name, ano, cursoID) VALUES
('ADS-1A', '2025', 1),
('ADS-1B', '2025', 1);

INSERT INTO Matricula (data_matricula, turmaID) VALUES
('2025-01-10', 1),
('2025-01-10', 1),
('2025-01-10', 2);

INSERT INTO alunos (name, endereco, data_nascimento, matriculaID) VALUES
('Vinícius Faria', 'Rua A, 123', '2006-05-12', 1),
('Ana Souza', 'Rua B, 456', '2005-09-22', 2),
('Carlos Lima', 'Rua C, 789', '2006-01-30', 3);

INSERT INTO Nota (nota, materiaID, alunoID) VALUES
(8.5, 1, 1),
(9.0, 2, 1),
(8.0, 3, 1),
(7.5, 1, 2),
(8.0, 2, 2),
(7.0, 3, 2),
(6.5, 1, 3),
(7.0, 2, 3),
(6.0, 3, 3);
