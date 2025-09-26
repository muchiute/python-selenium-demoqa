Feature: Gerar token de acesso

  @gerarToken @api
  Scenario: Gerar um token válido
    Given que eu possuo credenciais válidas
    When eu envio a requisição para gerar o token
    Then devo receber um token válido
