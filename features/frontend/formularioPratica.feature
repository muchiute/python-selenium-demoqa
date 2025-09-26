Feature: Preencher formulário de prática no DemoQA

  @practiceForm @ui
  Scenario: Preencher e submeter o formulário de prática
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Forms e o submenu Practice Form
    And eu preencho o formulário com dados aleatórios e envio um arquivo
    And eu submeto o formulário
    Then deve abrir um popup com os dados enviados
    And eu fecho o popup
