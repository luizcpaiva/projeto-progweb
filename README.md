# Projeto Django - GAC116 - Sistema de Vendas de Produtos de beleza

Este é o projeto de implementação da disciplina de Programação Web (GAC116).
O tema é um sistema de e-commerce para venda de produtos de beleza.

## Requisitos Atendidos (Checkpoint 1)

* [cite_start][x] Modelagem Completa (Produtos, Categorias, Pedidos) 
* [cite_start][x] Ambiente Administrativo funcional (via Django Admin) [cite: 5, 15]
* [cite_start][x] Uso de Git e GitHub com documentação 
* [cite_start][x] Banco de dados relacional (Django ORM / SQLite) 

## Requisitos Atendidos (Checkpoint 2)

* [cite_start][x] Framework CSS (Bootstrap) para interface responsiva 
* [cite_start][x] Ambiente para o usuário protegido com login/senha 

## Como Rodar (Localmente)

1.  Clone o repositório.
2.  Crie e ative um ambiente virtual (`python -m venv venv` e `.\venv\Scripts\activate`).
3.  Instale as dependências: `pip install django Pillow`
4.  Aplique as migrações: `python manage.py migrate`
5.  Crie um superusuário: `python manage.py createsuperuser`
6.  Rode o servidor: `python manage.py runserver`
7.  Acesse o site em: `http://127.0.0.1:8000/`
8.  Acesse o admin em: `http://127.0.0.1:8000/admin/`

## Integrantes do Grupo
* Kaique Inácio Salvador
* Luiz Carlos de Paiva Silva
* Sandy Karolina Maciel