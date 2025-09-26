Feature: Alugar livros

  @alugarLivros @api
  Scenario: Alugar dois livros de livre escolha
    Given que eu possuo dois livros disponíveis
    When eu envio a requisição para alugar os livros
    Then os livros devem ser adicionados ao meu usuário
