# Relatório de Vendas (relatorio-vendas)

Descrição
---------
Script simples em Python para gerar um relatório de receita por vendedor a partir de um banco MariaDB e exibir um gráfico de barras.

Arquivos
--------
- [main.py](main.py) — Script principal que conecta ao banco, executa a consulta e plota o gráfico.

Requisitos
---------
- Python 3.8+
- pacotes:
  ```sh
  pip install mariadb pandas matplotlib
  ```

Configuração do banco
---------------------
O script usa a base `techinfo` e as tabelas: `vendedores`, `produtos`, `vendas`. Utilize o arquivo [banco.sql](banco.sql) para criar as tabelas e os dados fictícios no seu banco.

Configuração do script
----------------------
Edite as credenciais de conexão em [main.py](main.py) na seção de conexão:
- host, port, user, password, database

Como rodar
---------
No terminal do projeto, rode o seguinte comando:
```sh
python main.py
```

O que esperar
-------------
- Saída no console com a tabela de receita por vendedor.
- Exibição de um gráfico de barras com a receita total por vendedor.