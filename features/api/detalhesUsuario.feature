Feature: Consultar detalhes do usuário

  @detalhesUsuario @api
  Scenario: Obter detalhes do usuário com os livros alugados
    Given que eu possuo um usuário com livros alugados
    When eu consulto os detalhes do usuário
    Then devo ver os dados do usuário e os livros alugados
