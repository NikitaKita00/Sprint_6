from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator) -> WebElement:
        """Ожидает появление элемента."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_visible_element(self, locator) -> WebElement:
        """Ожидает видимость элемента."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Ожидает, что элемент кликабелен и кликает."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def input_text(self, locator, text, clear_first=True):
        """Записывает текст в поле, предварительно очищая, если нужно."""
        element = self.find_visible_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def open_url(self, url):
        self.driver.get(url)

    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: len(d.window_handles) > 1
        )
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

    def scroll_into_view(self, element: WebElement):
        """Прокрутка к веб-элементу"""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def is_element_present(self, locator) -> bool:
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False
