Feature: Validação de abertura de novas janelas no DemoQA

  @browserWindows @ui
  Scenario: Validar abertura de nova janela
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Alerts, Frame & Windows e o submenu Browser Windows
    And eu clico no botão new window
    Then uma nova janela deve ser exibida com a mensagem "This is a sample page"
    And eu fecho a nova janela
