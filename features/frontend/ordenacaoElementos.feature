Feature: Ordenação de elementos no DemoQA

  @sortable @ui
  Scenario: Ordenar elementos de forma crescente
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Interactions e o submenu Sortable
    And eu organizo os elementos em ordem crescente
    Then os elementos devem estar em ordem de One até Six
