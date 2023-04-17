# Desafio CRUD

# Contexto
A criação de um CRUD (Create, Read, Update, Delete) é uma tarefa comum no desenvolvimento de aplicações web para gerenciar informações em um banco de dados. Uma das formas populares de criar um CRUD é usando o Flask, que é um framework de desenvolvimento web em Python.

A criação de um CRUD usando Flask para gerenciar um banco de dados de funcionários em uma empresa envolve configurar o ambiente, criar um modelo de dados, definir rotas para as operações de CRUD, a implementação das operações de banco de dados foi feita usando SQLAlchemy, além disso foram criados templates para exibir as páginas da aplicação web. Com a aplicação desenvolvida, os funcionários podem adicionar, visualizar, atualizar e excluir informações de funcionários de forma fácil e rápida, melhorando a gestão de funcionários na empresa.

## Técnologias usadas

Python3, Flask, SQLACHEMY


## Instalando Dependências

> Criação e ativação do ambiente virtual
```bash
python3 -m venv .venv && source .venv/bin/activate
``` 
> Instalação das libs
```bash
pip install -r requirements.txt
``` 
## Executando aplicação

  ```
  python3 app.py
  ```
## Rotas Implementadas

Tela inicial
```
rota("/")
```

Visualização do banco de dados
```
rota("/data")
```

Criação de um novo registro
```
rota("/data/create")
```

Visualização detalhada de um registro
```
rota("/data/<int:id>")
```

Atualização de um registro
```
rota("/data/<int:id>/update"
```

Exclusão de um registro
```
rota("/data/<int:id>/delete")
```
## Executando Testes

Em breve