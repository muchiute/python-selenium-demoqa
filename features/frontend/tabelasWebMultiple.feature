Feature: Criar e deletar múltiplos registros em Web Tables no DemoQA

  @webTablesBonus @ui
  Scenario: Criar e deletar múltiplos registros em Web Tables
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Elements e o submenu Web Tables
    And eu crio dinamicamente 12 registros
    And eu deleto todos os registros criados
    Then nenhum dos registros deve estar presente na tabela
