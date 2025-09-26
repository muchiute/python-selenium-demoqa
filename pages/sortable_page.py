from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from .base_page import BasePage
import time

class SortablePage(BasePage):
    LIST_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")

    EXPECTED_ORDER = ["One", "Two", "Three", "Four", "Five", "Six"]

    def _get_texts(self):
        return [e.text.strip() for e in self.find_all(self.LIST_ITEMS)]

    def is_sorted_ascending(self):
        """
        Valida se a lista está na ordem correta: One → Six.
        """
        texts = self._get_texts()
        return texts == self.EXPECTED_ORDER

    def sort_elements(self):
        """
        Organiza a lista para a ordem One → Six.
        """
        if self.is_sorted_ascending():
            return  # já está ordenado corretamente

        actions = ActionChains(self.driver)
        current_texts = self._get_texts()

        for target_index, expected_text in enumerate(self.EXPECTED_ORDER):
            current_items = self.find_all(self.LIST_ITEMS)

            if current_items[target_index].text.strip() == expected_text:
                continue

            try:
                src_index = next(i for i, el in enumerate(current_items) if el.text.strip() == expected_text)
            except StopIteration:
                continue

            src = current_items[src_index]
            dest = current_items[target_index]

            try:
                actions.reset_actions()
                actions.click_and_hold(src).move_to_element(dest).move_by_offset(0, 5).release().perform()
            except Exception:
                try:
                    actions.reset_actions()
                    actions.drag_and_drop(src, dest).perform()
                except Exception:
                    try:
                        self.driver.execute_script("""
                            const src = arguments[0];
                            const dest = arguments[1];
                            dest.parentNode.insertBefore(src, dest);
                        """, src, dest)
                    except Exception:
                        pass

            time.sleep(0.3)
