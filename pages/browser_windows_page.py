from selenium.webdriver.common.by import By
from .base_page import BasePage

class BrowserWindowsPage(BasePage):
    NEW_WINDOW_BUTTON = (By.ID, "windowButton")
    SAMPLE_HEADING = (By.ID, "sampleHeading")

    def open_new_window(self):
        self.click(self.NEW_WINDOW_BUTTON)

    def validate_new_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        text = self.get_text(self.SAMPLE_HEADING)
        return text
