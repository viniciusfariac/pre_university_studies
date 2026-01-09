# 🎓 Academic System Backend

Sistema acadêmico backend desenvolvido em **Python**, com integração a **banco de dados relacional**, simulando um ambiente real de faculdade.
O projeto foi criado com foco em **arquitetura backend, regras de negócio e persistência de dados**, indo além de um simples CRUD.

---

## 🎯 Objetivo do Projeto

- Simular o funcionamento básico de um sistema acadêmico
- Aplicar conceitos de backend em um cenário real
- Praticar modelagem e validação de dados
- Trabalhar lógica de negócio diretamente no backend
- Consolidar conhecimentos em Python e SQL

---

## ⚙️ Funcionalidades

- Cadastro de alunos
- Validação de curso e turma no banco de dados
- Matrícula vinculada a curso e turma
- Lançamento de notas por matéria
- Cálculo de média diretamente via SQL (`AVG`)
- Relatórios estatísticos
- Geração de gráficos a partir dos dados
- Menu interativo via terminal (CLI)

---

## 🛠 Tecnologias Utilizadas

- Python
- PostgreSQL
- MariaDB
- SQL (JOINs, agregações, chaves primárias e estrangeiras)
- Matplotlib
- Git & GitHub

---

## 🧱 Conceitos Aplicados

- Modelagem de banco de dados relacional
- Chaves primárias e estrangeiras
- Validação de dados antes da persistência
- Separação de responsabilidades
- Arquitetura modular em Python
- Tratamento de erros
- Regras de negócio no backend
- Uso consciente do banco (consultas e cálculos via SQL)

---

## 📂 Estrutura do Projeto

## 📂 Estrutura do Projeto

```text
src/
 ├── menu.py          # Menu principal do sistema
 ├── alunos.py        # Cadastro e validação de alunos
 ├── notas.py         # Lançamento de notas 
 ├── notas_calculos.py # Médias e gráficos
 ├── db.py  # Configuração e conexão com o banco
 
databases/
 ├── schema.sql       # Criação das tabelas
 └── seeds.sql        # Dados iniciais para testes

```
*(nomes podem variar conforme evolução do projeto)*
---

## 📊 Relatórios e Estatísticas

Os relatórios são gerados a partir de consultas SQL e visualizados através de gráficos, permitindo uma análise clara do desempenho acadêmico.

---

## 🚀 Motivação

Este projeto foi desenvolvido como parte da minha preparação acadêmica, com foco em **pensar como desenvolvedor backend**, entendendo não apenas o código, mas também a lógica e a estrutura por trás de sistemas reais.

---

## 📌 Observações

Projeto em evolução contínua.  
Novas funcionalidades e melhorias estruturais serão adicionadas conforme o avanço dos estudos.

