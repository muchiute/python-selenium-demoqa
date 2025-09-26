Feature: Criar um novo usuário

  @criarUsuario @api
  Scenario: Criar um novo usuário com sucesso
    Given que eu possuo dados válidos de usuário
    When eu envio a requisição para criar o usuário
    Then o usuário deve ser criado com sucesso