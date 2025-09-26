# Python + Selenium Testes Automatizados

Este projeto contém testes automatizados utilizando Python, Selenium e Behave para testar funcionalidades de API e interfaces Web/UI.

## 🧪 Funcionalidades

### API

CT001 – Criar Usuário
- Criação de um novo usuário (usado como massa de dados para cenários Web/UI).

CT002 – Gerar Token
- Geração de token de acesso válido para o usuário.

CT003 – Autorização de Usuário
- Validação de que o usuário possui autorização.

CT004 – Listar Livros
- Consulta de todos os livros disponíveis.

CT005 – Alugar Livros
- Aluguel de livros selecionados pelo usuário.

CT006 – Detalhes do Usuário
- Consulta de detalhes do usuário incluindo livros alugados.

### Web/UI

CT001 – Preencher Practice Form
- Preenchimento de formulário com dados aleatórios e envio de arquivo no site DemoQA.

CT002 – Abertura de Nova Janela
- Validação de abertura de nova janela e fechamento após verificação.

CT003 – Web Tables
- Criação, edição e exclusão de registros em Web Tables.

CT004 – Web Tables (Mutiples)
- Criação e deleção de múltiplos registros em Web Tables.

CT005 – Progress Bar
- Validação do funcionamento da barra de progresso (início, parada e reset).

CT006 – Sortable
- Ordenação de elementos de forma crescente na interface DemoQA.

## ⚙️ Tecnologias Utilizadas
- **Python**: Linguagem de programação utilizada para automação e scripts.
- **SeleniumLibrary**: Automação de navegadores.
- **Behave**: Framework BDD para testes automatizados.
- **Allure**: Geração de relatórios detalhados.
- **VSCode**: Editor de código recomendado para desenvolvimento.

## 🛠️ Pré-requisitos
Antes de começar, você precisará ter instalado em sua máquina as seguintes ferramentas:

- [Python 3.13.6](https://www.python.org/downloads/) (para gerenciamento de dependências)
- [VSCode](https://code.visualstudio.com/) (opcional, mas recomendado)
- [Driver do Navegador - ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br)

## 📦 Instalação

- `pip install -r requirements.txt` (dentro da pasta do projeto na raiz)

## 🏷️ Tags utilizadas + Descrição

- @api - Cenários de API (usuário, token, livros)
- @ui - Cenários de Web/UI (DemoQA, formulários, janelas, Web Tables, progress bar, sortable)
- @criarUsuario - Criar usuário
- @gerarToken - Gerar token de acesso
- @autorizarUsuario - Autorização de usuário
- @listarLivros - Listagem de livros
- @alugarLivros - Aluguel de livros
- @detalhesUsuario - Detalhes do usuário com livros alugados
- @practiceForm - Preenchimento de formulário DemoQA
- @browserWindows - Testes de novas janelas
- @webTables - CRUD em Web Tables
- @webTablesBonus - CRUD de múltiplos registros
- @progressBar - Testes de progress bar
- @sortable - Ordenação de elementos

## Comandos para execução dos testes

Para execução normal dos testes (dentro da pasta do projeto na raiz) - SEM TAG
- [Exemplo:]; behave

Para executar apenas testes de API:
- [Exemplo:]: behave --tags=@api

Para executar apenas testes de Web/UI:
- [Exemplo:]: behave --tags=@ui

Para executar um cenário específico e gerar o relatório na pasta reports/allure-results
- [Exemplo]: behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results