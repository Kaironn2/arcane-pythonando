# 🤖 My DRF API – CRUD + Statistics + JWT

## English

---

### 📟 Short Description

A robust API built with Django Rest Framework, offering comprehensive CRUD operations, advanced statistical insights (averages, totals), and secure access via JWT authentication. Includes Django commands for CSV processing and database seeding using the Rest Countries API.

### 📄 Long Description

This repository hosts a powerful API developed with **Django Rest Framework (DRF)**. It's designed to go beyond basic data management, providing valuable statistical analysis alongside standard CRUD functionalities.

The system incorporates several key features:

* **JWT Authentication**: Ensures secure API access by leveraging JSON Web Tokens (JWT) for user authentication.
* **Django Commands for Data Processing**: Custom Django management commands facilitate the efficient processing of `.csv` files and seamless data insertion into the database.
* **Database Seeding with Rest Countries API**: Includes specialized commands to automatically populate database tables, such as nationalities, by fetching up-to-date data from the [Rest Countries API](https://restcountries.com/).
* **Serializers**: Utilizes DRF's powerful serializers for effective data serialization and deserialization, streamlining data handling.
* **RESTful API Endpoints**: Provides a well-structured set of RESTful API endpoints for interacting with various data resources.
* **Signals**: Employs Django signals to trigger specific actions or logic in response to various database events, enhancing data integrity and automation.
* **Advanced Statistical Insights**: Offers more than just basic data retrieval; the API calculates and provides statistical information, including averages, totals, and other aggregated metrics to support data analysis.

### 🔄 Process Flow

1.  **Data Ingestion**: Data can be inserted via API endpoints, or through Django commands by processing `.csv` files.
2.  **Database Seeding**: Specific commands can be run to fetch external data (e.g., nationalities from Rest Countries API) and populate the database.
3.  **Data Processing**: Incoming data can trigger Django signals for validation, cleaning, or additional processing before being saved.
4.  **API Requests**: Users send authenticated requests to various RESTful endpoints.
5.  **Response Generation**: The API processes requests, interacts with the database (for CRUD), and performs calculations for statistical endpoints.
6.  **Data Serialization**: DRF serializers transform database objects into structured API responses (JSON).
7.  **Authentication**: Every request is validated against JWT tokens to ensure authorized access.

### 🧰 Tech Stack

* Python
* Django
* Django Rest Framework (DRF)
* Django REST Simple JWT
* `requests` (for external API calls like Rest Countries)
* PostgreSQL (or your chosen database)

---

## Português

---

### 📟 Descrição Curta

Uma API robusta construída com Django Rest Framework, oferecendo operações CRUD completas, insights estatísticos avançados (médias, totais) e acesso seguro via autenticação JWT. Inclui comandos Django para processamento de CSV e preenchimento de banco de dados usando a API Rest Countries.

### 📄 Descrição Longa

Este repositório hospeda uma poderosa API desenvolvida com **Django Rest Framework (DRF)**. Ela foi projetada para ir além do gerenciamento básico de dados, fornecendo análises estatísticas valiosas juntamente com as funcionalidades CRUD padrão.

O sistema incorpora várias características-chave:

* **Autenticação JWT**: Garante acesso seguro à API utilizando JSON Web Tokens (JWT) para autenticação de usuários.
* **Django Commands para Processamento de Dados**: Comandos de gerenciamento Django personalizados facilitam o processamento eficiente de arquivos `.csv` e a inserção contínua de dados no banco de dados.
* **Preenchimento do Banco de Dados com a Rest Countries API**: Inclui comandos especializados para popular automaticamente tabelas do banco de dados, como nacionalidades, buscando dados atualizados da [Rest Countries API](https://restcountries.com/).
* **Serializers**: Utiliza os poderosos serializers do DRF para serialização e desserialização eficazes de dados, otimizando o manuseio das informações.
* **Endpoints de API RESTful**: Fornece um conjunto bem estruturado de endpoints de API RESTful para interagir com vários recursos de dados.
* **Signals**: Emprega sinais do Django para disparar ações ou lógicas específicas em resposta a vários eventos do banco de dados, aprimorando a integridade e a automação dos dados.
* **Insights Estatísticos Avançados**: Oferece mais do que apenas a recuperação básica de dados; a API calcula e fornece informações estatísticas, incluindo médias, totais e outras métricas agregadas para apoiar a análise de dados.

### 🔄 Fluxo do Processo

1.  **Ingestão de Dados**: Os dados podem ser inseridos via endpoints da API, ou através de comandos Django processando arquivos `.csv`.
2.  **Preenchimento do Banco de Dados**: Comandos específicos podem ser executados para buscar dados externos (ex: nacionalidades da Rest Countries API) e popular o banco de dados.
3.  **Processamento de Dados**: Dados recebidos podem disparar sinais do Django para validação, limpeza ou processamento adicional antes de serem salvos.
4.  **Requisições da API**: Usuários enviam requisições autenticadas para vários endpoints RESTful.
5.  **Geração de Resposta**: A API processa as requisições, interage com o banco de dados (para CRUD) e realiza cálculos para os endpoints estatísticos.
6.  **Serialização de Dados**: Serializers do DRF transformam objetos do banco de dados em respostas estruturadas da API (JSON).
7.  **Autenticação**: Cada requisição é validada contra tokens JWT para garantir acesso autorizado.

### 🧰 Tech Stack

* Python
* Django
* Django Rest Framework (DRF)
* Django REST Simple JWT
* `requests` (para chamadas a APIs externas como Rest Countries)
* PostgreSQL (ou seu banco de dados de escolha)
