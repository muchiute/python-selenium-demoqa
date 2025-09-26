from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class WebTablesPage(BasePage):
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    AGE = (By.ID, "age")
    SALARY = (By.ID, "salary")
    DEPARTMENT = (By.ID, "department")
    SUBMIT = (By.ID, "submit")
    TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")

    # ---------------- CRUD ----------------
    def add_record(self, fname, lname, email, age, salary, department):
        self.click(self.ADD_BUTTON)
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)
        self.type(self.EMAIL, email)
        self.type(self.AGE, age)
        self.type(self.SALARY, salary)
        self.type(self.DEPARTMENT, department)
        self.click(self.SUBMIT)
        time.sleep(0.2)  # espera DOM atualizar

    def get_rows(self):
        rows = self.find_all(self.TABLE_ROWS)
        return [r for r in rows if r.text.strip()]

    def edit_record(self, row_index, new_fname=None, new_lname=None):
        rows = self.get_rows()
        if row_index < len(rows):
            edit_button = rows[row_index].find_element(By.CSS_SELECTOR, "span[title='Edit']")
            edit_button.click()
            time.sleep(0.2)
            if new_fname:
                self.type(self.FIRST_NAME, new_fname)
            if new_lname:
                self.type(self.LAST_NAME, new_lname)
            self.click(self.SUBMIT)
            time.sleep(0.2)

    def delete_record(self, row_index=0):
        rows = self.get_rows()
        if rows:
            delete_button = rows[row_index].find_element(By.CSS_SELECTOR, "span[title='Delete']")
            delete_button.click()
            time.sleep(0.2)

    def all_records_deleted(self):
        """Retorna True se a grid estiver vazia (nenhuma linha com texto)."""
        return len(self.get_rows()) == 0
