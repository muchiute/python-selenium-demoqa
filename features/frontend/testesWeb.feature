Feature: Fluxo completo de testes Web no DemoQA

  @practiceForm @ui
  Scenario: Preencher e submeter o formulário de prática
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Forms e o submenu Practice Form
    And eu preencho o formulário com dados aleatórios e envio um arquivo
    And eu submeto o formulário
    Then deve abrir um popup com os dados enviados
    And eu fecho o popup

  @browserWindows @ui
  Scenario: Validar abertura de nova janela
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Alerts, Frame & Windows e o submenu Browser Windows
    And eu clico no botão new window
    Then uma nova janela deve ser exibida com a mensagem "This is a sample page"
    And eu fecho a nova janela

  @webTables @ui
  Scenario: Criar, editar e deletar um registro em Web Tables
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Elements e o submenu Web Tables
    And eu crio um novo registro
    And eu edito o registro criado
    And eu deleto o registro criado
    Then o registro não deve mais existir na tabela

  @webTablesBonus @ui
  Scenario: Criar e deletar múltiplos registros em Web Tables
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Elements e o submenu Web Tables
    And eu crio dinamicamente 12 registros
    And eu deleto todos os registros criados
    Then nenhum dos registros deve estar presente na tabela

  @progressBar @ui
  Scenario: Validar funcionamento da progress bar
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Widgets e o submenu Progress Bar
    And eu inicio a progress bar
    And eu paro antes dos 25 porcento
    Then o valor da progress bar deve ser menor ou igual a 25 porcento
    When eu inicio novamente a progress bar até 100 porcento
    Then devo resetar a progress bar

  @sortable @ui
  Scenario: Ordenar elementos de forma crescente
    Given que estou na página inicial do DemoQA
    When eu acesso o menu Interactions e o submenu Sortable
    And eu organizo os elementos em ordem crescente
    Then os elementos devem estar em ordem de One até Six
