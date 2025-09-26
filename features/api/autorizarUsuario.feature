Feature: Autorizar usuário

  @autorizarUsuario @api
  Scenario: Confirmar que o usuário está autorizado
    Given que eu possuo um token de acesso válido
    When eu verifico a autorização do usuário
    Then o usuário deve estar autorizado
