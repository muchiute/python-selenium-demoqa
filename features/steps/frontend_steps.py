from behave import given, when, then
from pages.practice_form_page import PracticeFormPage
from pages.browser_windows_page import BrowserWindowsPage
from pages.web_tables_page import WebTablesPage
from pages.progress_bar_page import ProgressBarPage
from pages.sortable_page import SortablePage
from selenium.webdriver.common.by import By
import os, random, time

# ---------- CONTEXTO GERAL ----------

@given("que estou na página inicial do DemoQA")
def step_impl(context):
    context.driver.get("https://demoqa.com/")
    time.sleep(1)

# ---------- PRACTICE FORM ----------

@when("eu acesso o menu Forms e o submenu Practice Form")
def step_impl(context):
    context.driver.find_element("xpath", "//h5[text()='Forms']").click()
    time.sleep(0.5)
    context.driver.find_element("xpath", "//span[text()='Practice Form']").click()
    context.page = PracticeFormPage(context.driver)
    time.sleep(0.5)

@when("eu preencho o formulário com dados aleatórios e envio um arquivo")
def step_impl(context):
    email = f"teste{random.randint(1000,9999)}@mail.com"
    file_path = os.path.abspath("utils/so_para_automacao.txt")
    context.page.fill_form("Teste", "Web", email, "9999999999", "Rua Teste 123", file_path)

@when("eu submeto o formulário")
def step_impl(context):
    context.page.submit()
    time.sleep(1)

@then("deve abrir um popup com os dados enviados")
def step_impl(context):
    assert context.page.wait_for_modal(timeout=10), "Popup não abriu!"
    assert context.page.is_popup_opened(), "Popup não abriu!"

@then("eu fecho o popup")
def step_impl(context):
    context.page.close_popup()
    if context.driver:
        context.driver.quit()

# ---------- BROWSER WINDOWS ----------

@when("eu acesso o menu Alerts, Frame & Windows e o submenu Browser Windows")
def step_impl(context):
    context.driver.find_element("xpath", "//h5[text()='Alerts, Frame & Windows']").click()
    time.sleep(0.5)
    context.driver.find_element("xpath", "//span[text()='Browser Windows']").click()
    context.page = BrowserWindowsPage(context.driver)

@when("eu clico no botão new window")
def step_impl(context):
    context.page.open_new_window()
    time.sleep(0.5)

@then('uma nova janela deve ser exibida com a mensagem "This is a sample page"')
def step_impl(context):
    text = context.page.validate_new_window()
    assert text == "This is a sample page"

@then("eu fecho a nova janela")
def step_impl(context):
    context.driver.close()
    handles = context.driver.window_handles
    context.driver.switch_to.window(handles[0])
    context.driver.quit()

# ---------- WEB TABLES ----------

@when("eu acesso o menu Elements e o submenu Web Tables")
def step_impl(context):
    context.driver.find_element("xpath", "//h5[text()='Elements']").click()
    time.sleep(0.5)
    context.driver.find_element("xpath", "//span[text()='Web Tables']").click()
    context.page = WebTablesPage(context.driver)
    time.sleep(0.5)

@when("eu crio um novo registro")
def step_impl(context):
    context.page.add_record("Joao", "Teste", "joao@mail.com", "30", "5000", "QA")

@when("eu edito o registro criado")
def step_impl(context):
    context.page.edit_record(0, new_fname="Jose")

@when("eu deleto o registro criado")
def step_impl(context):
    context.page.delete_record(0)

@then("o registro não deve mais existir na tabela")
def step_impl(context):
    assert context.page.all_records_deleted() or all("Jose" not in r.text for r in context.page.get_rows())
    context.driver.quit()

@when("eu crio dinamicamente 12 registros")
def step_impl(context):
    for i in range(12):
        context.page.add_record(
            f"User{i}", "Auto", f"user{i}@mail.com", str(20+i), str(1000+i), "IT"
        )
        time.sleep(0.1)

@when("eu deleto todos os registros criados")
def step_impl(context):
    while not context.page.all_records_deleted():
        context.page.delete_record(0)

@then("nenhum dos registros deve estar presente na tabela")
def step_impl(context):
    assert context.page.all_records_deleted(), "Ainda existem registros na tabela!"
    context.driver.quit()

# ---------- PROGRESS BAR ----------

@when("eu acesso o menu Widgets e o submenu Progress Bar")
def step_impl(context):
    try:
        context.driver.execute_script("document.getElementById('fixedban').style.display='none';")
        iframes = context.driver.find_elements(By.TAG_NAME, "iframe")
        for iframe in iframes:
            context.driver.execute_script("arguments[0].style.display='none';", iframe)
    except Exception:
        pass
    context.driver.find_element("xpath", "//h5[text()='Widgets']").click()
    time.sleep(0.5)
    context.driver.find_element("xpath", "//span[text()='Progress Bar']").click()
    context.page = ProgressBarPage(context.driver)

@when("eu inicio a progress bar")
def step_impl(context):
    context.page.start()
    time.sleep(0.2)

@when("eu paro antes dos 25 porcento")
def step_impl(context):
    target_stop = 24
    while context.page.get_progress_value() < target_stop:
        time.sleep(0.05)
    context.page.stop()
    time.sleep(2)

@then("o valor da progress bar deve ser menor ou igual a 25 porcento")
def step_impl(context):
    value = context.page.get_progress_value()
    assert value <= 25, f"Progress bar está em {value}% (esperado <= 25%)"
    print(f"Progress bar parou em {value}%")

@when("eu inicio novamente a progress bar até 100 porcento")
def step_impl(context):
    context.page.start()
    context.page.wait_until_at_least(100, timeout=60)
    time.sleep(1)

@then("devo resetar a progress bar")
def step_impl(context):
    context.page.reset()
    time.sleep(1)
    assert context.page.get_progress_value() == 0, "Progress bar não resetou para 0%"
    context.driver.quit()

# ---------- SORTABLE ----------

@when("eu acesso o menu Interactions e o submenu Sortable")
def step_impl(context):
    context.driver.find_element("xpath", "//h5[text()='Interactions']").click()
    time.sleep(0.5)
    context.driver.find_element("xpath", "//span[text()='Sortable']").click()
    context.page = SortablePage(context.driver)

@when("eu organizo os elementos em ordem crescente")
def step_impl(context):
    context.page.sort_elements()
    time.sleep(0.5)

@then("os elementos devem estar em ordem de One até Six")
def step_impl(context):
    expected_order = ["One", "Two", "Three", "Four", "Five", "Six"]
    actual_order = context.page._get_texts()
    assert actual_order == expected_order, f"A lista não está na ordem correta: {actual_order}"
    print("Lista validada:", actual_order)
    context.driver.quit()
