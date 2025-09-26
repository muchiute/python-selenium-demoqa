Feature: Validação da progress bar no DemoQA

  @progressBar @ui
  Scenario: Validar funcionamento da progress bar
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Widgets e o submenu Progress Bar
    And eu inicio a progress bar
    And eu paro antes dos 25 porcento
    Then o valor da progress bar deve ser menor ou igual a 25 porcento
    When eu inicio novamente a progress bar até 100 porcento
    Then devo resetar a progress bar
