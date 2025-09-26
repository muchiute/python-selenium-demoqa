from selenium.webdriver.common.by import By
from .base_page import BasePage
import time
import re

class ProgressBarPage(BasePage):
    START_STOP_BUTTON = (By.ID, "startStopButton")
    RESET_BUTTON = (By.ID, "resetButton")
    PROGRESS_BAR = (By.CSS_SELECTOR, ".progress-bar")

    def start(self):
        self.click(self.START_STOP_BUTTON)

    def stop(self):
        self.click(self.START_STOP_BUTTON)

    def reset(self):
        self.click(self.RESET_BUTTON)

    def get_progress_value(self):
        """
        Retorna o valor numérico atual da progress bar (0..100) como int.
        Lê aria-valuenow, style (width) ou texto como fallback.
        """
        el = self.find(self.PROGRESS_BAR)
        val = el.get_attribute("aria-valuenow")
        if not val:
            style = el.get_attribute("style") or ""
            # tenta extrair 'width: 25%'
            m = re.search(r"(\d+)", style)
            if m:
                return int(m.group(1))
            text = el.text or ""
            m = re.search(r"(\d+)", text)
            return int(m.group(1)) if m else 0
        try:
            return int(val)
        except Exception:
            m = re.search(r"(\d+)", val)
            return int(m.group(1)) if m else 0

    def wait_until_at_least(self, target, timeout=60):
        """
        Espera até que a progress bar alcance >= target (em %).
        Retorna o valor atual (pode ser >= target) ou último valor lido se timeout.
        """
        end = time.time() + timeout
        while time.time() < end:
            v = self.get_progress_value()
            if v >= target:
                return v
            time.sleep(0.08)
        return self.get_progress_value()
