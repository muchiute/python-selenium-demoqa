# pages/practice_form_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
from .base_page import BasePage
import os

class PracticeFormPage(BasePage):
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[text()='Male']")
    PHONE = (By.ID, "userNumber")
    DATE_INPUT = (By.ID, "dateOfBirthInput")
    DATE_DAY_15 = (By.CSS_SELECTOR, ".react-datepicker__day--015")
    SUBJECT = (By.ID, "subjectsInput")
    HOBBY_SPORTS = (By.XPATH, "//label[text()='Sports']")
    HOBBY_READING = (By.XPATH, "//label[text()='Reading']")
    ADDRESS = (By.ID, "currentAddress")
    UPLOAD = (By.ID, "uploadPicture")
    SUBMIT = (By.ID, "submit")
    MODAL = (By.CLASS_NAME, "modal-content")
    CLOSE_MODAL = (By.ID, "closeLargeModal")

    def __init__(self, driver, timeout=10):
        super().__init__(driver)
        # garante um wait local; se BasePage já possuir, ok também
        self.wait = WebDriverWait(driver, timeout)

    def _safe_click(self, locator):
        """
        Tenta clicar normalmente; se houver intercept (ad, iframe), usa JS click como fallback.
        Também rola para o elemento antes de clicar.
        """
        el = self.wait.until(EC.presence_of_element_located(locator))
        try:
            # tenta clique normal (clicável)
            self.wait.until(EC.element_to_be_clickable(locator))
            el = self.find(locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
            el.click()
            return
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            # fallback por JS
            try:
                el = self.find(locator)
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                self.driver.execute_script("arguments[0].click();", el)
                return
            except Exception:
                raise

    def fill_form(self, fname, lname, email, phone, address, file_path=None):
        # inputs com clear() via BasePage.type (garanta que BasePage.type chame el.clear())
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)

        # sanitiza email (remove espaços/quebras)
        email = (email or "").strip().replace("\n", "").replace("\r", "")
        self.type(self.EMAIL, email)

        # gênero
        try:
            self._safe_click(self.GENDER_MALE)
        except Exception:
            # se falhar, não interrompe o fluxo (mas pode afetar validações específicas)
            pass

        # telefone
        self.type(self.PHONE, phone)

        # data: abrir e selecionar dia 15 (fazer try porque pode variar)
        try:
            self._safe_click(self.DATE_INPUT)
            self._safe_click(self.DATE_DAY_15)
        except Exception:
            pass

        # subject: digita e confirma com ENTER para o autocomplete
        try:
            subj_el = self.find(self.SUBJECT)
            subj_el.clear()
            subj_el.send_keys("Maths")
            subj_el.send_keys("\n")
        except Exception:
            pass

        # hobbies (safe clicks)
        try:
            self._safe_click(self.HOBBY_SPORTS)
        except Exception:
            pass
        try:
            self._safe_click(self.HOBBY_READING)
        except Exception:
            pass

        # endereço
        self.type(self.ADDRESS, address)

        # upload: envia o path diretamente para o input type=file
        if file_path:
            if not os.path.isabs(file_path):
                file_path = os.path.abspath(file_path)
            if os.path.exists(file_path):
                input_el = self.find(self.UPLOAD)
                input_el.send_keys(file_path)
            else:
                # opcional: raise para aviso claro
                raise FileNotFoundError(f"Arquivo de upload não encontrado: {file_path}")

    def submit(self):
        # usa safe click no botão submit (pode haver overlay)
        self._safe_click(self.SUBMIT)

    def wait_for_modal(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.MODAL)
            )
            return True
        except TimeoutException:
            return False

    def is_popup_opened(self):
        return self.wait_for_modal(5)

    def close_popup(self):
        # fecha com clique seguro e espera invisibilidade
        self._safe_click(self.CLOSE_MODAL)
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.MODAL))
        except TimeoutException:
            pass
