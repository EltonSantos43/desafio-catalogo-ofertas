# Catálogo de Ofertas - Mercado Livre

Este projeto foi desenvolvido para realizar a raspagem de dados no site do **Mercado Livre** e exibir informações sobre o produto "Computador Gamer i7 16GB SSD 1TB". Utilizando o framework **Django** e a biblioteca **Selenium** para realizar a raspagem, o objetivo é fornecer uma lista de produtos com os seguintes campos:

- Imagem do Produto
- Nome do Produto
- Preço do Produto
- Opção de Parcelamento
- Link do Produto
- Preço sem Desconto (se houver)
- Percentual de Desconto (se houver)
- Tipo de Entrega (Full ou Normal)
- Frete Grátis (se houver)

Além disso, a aplicação implementa funcionalidades de filtragem para facilitar a busca do usuário:

- Produtos com Frete Grátis
- Produtos Entregues pelo Full

Também são exibidos os seguintes destaques dos produtos:

- Maior Preço
- Menor Preço
- Maior Desconto Percentual

Os dados dos produtos são armazenados em um banco de dados relacional PostgreSQL para manter a estrutura persistente.

## Requisitos

- Python 3.x
- Django 5.x
- Selenium 4.x
- PostgreSQL

## Instalação

1. **Clone o repositório**:
```
git clone U[RL-do-repositório](https://github.com/EltonSantos43/desafio-catalogo-ofertas)
```

2. **Instale as dependências**:
Se você não tiver um arquivo **requirements.txt**, execute o seguinte comando para instalar as bibliotecas necessárias:
```
pip install django selenium psycopg2-binary webdriver-manager
```

3. **Configuração do Banco de Dados**:
Se você optar por usar o PostgreSQL, configure as variáveis de ambiente para o banco de dados e ajuste no arquivo settings.py do Django.

4. **Configuração do Selenium**:
Certifique-se de que o ChromeDriver está instalado e configurado corretamente. O script usa o webdriver-manager para instalar automaticamente o ChromeDriver.

## Como Usar

1. **Rodando o Servidor**:
Para rodar o servidor de desenvolvimento do Django, execute:
```
python manage.py runserver
```

2. **Raspagem de Dados**:
A função de raspagem será executada automaticamente quando você chamar o comando relacionado à função **scrape()**. 

3. **Acessando a Página de Produtos**:
Após a raspagem dos dados, os produtos estarão disponíveis em uma página no Django onde você pode visualizar as informações de cada produto.
