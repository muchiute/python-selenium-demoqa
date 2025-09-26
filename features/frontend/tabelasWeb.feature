Feature: CRUD em Web Tables no DemoQA

  @webTables @ui
  Scenario: Criar, editar e deletar um registro em Web Tables
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Elements e o submenu Web Tables
    And eu crio um novo registro
    And eu edito o registro criado
    And eu deleto o registro criado
    Then o registro não deve mais existir na tabela
