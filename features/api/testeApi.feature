Feature: Fluxo completo de criação de usuário e manipulação de livros

  @criarUsuario @api
  Scenario: Criar um novo usuário com sucesso
    Given que eu possuo dados válidos de usuário
    When eu envio a requisição para criar o usuário
    Then o usuário deve ser criado com sucesso

  @gerarToken @api
  Scenario: Gerar um token válido
    Given que eu possuo credenciais válidas
    When eu envio a requisição para gerar o token
    Then devo receber um token válido

  @autorizarUsuario @api
  Scenario: Confirmar que o usuário está autorizado
    Given que eu possuo um token de acesso válido
    When eu verifico a autorização do usuário
    Then o usuário deve estar autorizado

  @listarLivros @api
  Scenario: Obter todos os livros disponíveis
    Given que existem livros cadastrados
    When eu solicito a lista de livros
    Then devo receber a lista de livros disponíveis

  @alugarLivros @api
  Scenario: Alugar dois livros de livre escolha
    Given que eu possuo dois livros disponíveis
    When eu envio a requisição para alugar os livros
    Then os livros devem ser adicionados ao meu usuário

  @detalhesUsuario @api
  Scenario: Obter detalhes do usuário com os livros alugados
    Given que eu possuo um usuário com livros alugados
    When eu consulto os detalhes do usuário
    Then devo ver os dados do usuário e os livros alugados