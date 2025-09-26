Feature: Listar livros disponíveis

  @listarLivros @api
  Scenario: Obter todos os livros disponíveis
    Given que existem livros cadastrados
    When eu solicito a lista de livros
    Then devo receber a lista de livros disponíveis
