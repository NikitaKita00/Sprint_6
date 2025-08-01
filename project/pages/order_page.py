import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from project.locators.order_page_locators import OrderPageLocators
from project.pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.open_url(url)

    @allure.step("Заполнить поле Имя: {name}")
    def fill_name(self, name: str):
        self.input_text(self.locators.INPUT_NAME, name)

    @allure.step("Заполнить поле Фамилия: {surname}")
    def fill_surname(self, surname: str):
        self.input_text(self.locators.INPUT_SURNAME, surname)

    @allure.step("Заполнить поле Адрес: {address}")
    def fill_address(self, address: str):
        self.input_text(self.locators.INPUT_ADDRESS, address)

    @allure.step("Выбрать станцию метро: {metro_name}")
    def select_metro_station(self, metro_name: str):
        self.click(self.locators.INPUT_METRO)
        self.input_text(self.locators.INPUT_METRO, metro_name, clear_first=True)
        option_xpath = f"//*[normalize-space(text())='{metro_name}']"
        self.click((By.XPATH, option_xpath))

    @allure.step("Заполнить поле Телефон: {phone}")
    def fill_phone(self, phone: str):
        self.input_text(self.locators.INPUT_PHONE, phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        elem = self.find_element(self.locators.NEXT_BUTTON)
        self.scroll_into_view(elem)
        for method in [
            elem.click,
            lambda: self.driver.execute_script("arguments[0].click();", elem),
            lambda: ActionChains(self.driver).move_to_element(elem).click().perform(),
            lambda: ActionChains(self.driver)
            .move_to_element_with_offset(elem, 5, 5)
            .click()
            .perform(),
        ]:
            try:
                method()
                return
            except Exception:
                continue
        raise Exception("Не удалось кликнуть кнопку 'Далее'")

    @allure.step("Заполнить дату доставки: {date_str}")
    def fill_delivery_date(self, date_str: str):
        elem = self.find_element(self.locators.DELIVERY_DATE_INPUT)
        self.scroll_into_view(elem)
        elem.click()
        elem.clear()
        elem.send_keys(date_str)

    @allure.step("Выбрать срок аренды: {period_text}")
    def select_rental_period(self, period_text: str):
        self.driver.execute_script(
            """
            const datepicker = document.querySelector('.react-datepicker');
            if (datepicker) { datepicker.style.display = 'none'; }
        """
        )
        self.driver.find_element(By.TAG_NAME, "body").click()

        dropdown = self.find_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        self.scroll_into_view(dropdown)
        dropdown.click()

        menu = self.find_element((By.CLASS_NAME, "Dropdown-menu"))
        option_xpath = f".//div[contains(@class,'Dropdown-option') and normalize-space(text())='{period_text}']"
        option = menu.find_element(By.XPATH, option_xpath)

        actions = ActionChains(self.driver)
        actions.move_to_element(option).click().perform()

    @allure.step("Принять cookie")
    def accept_cookies(self):
        if self.is_element_present(self.locators.COOKIE_ACCEPT_BUTTON):
            self.click(self.locators.COOKIE_ACCEPT_BUTTON)

    @allure.step("Нажать финальную кнопку 'Заказать'")
    def click_order_final_button(self):
        self.accept_cookies()
        elem = self.find_element(self.locators.ORDER_FINAL_BUTTON)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.scroll_into_view(elem)
        for method in [
            elem.click,
            lambda: self.driver.execute_script("arguments[0].click();", elem),
            lambda: ActionChains(self.driver).move_to_element(elem).click().perform(),
        ]:
            try:
                method()
                return
            except Exception:
                continue
        raise Exception("Не удалось нажать кнопку 'Заказать'")

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        elem = self.find_element(self.locators.MODAL_CONFIRM_BUTTON_YES)
        self.scroll_into_view(elem)
        for method in [
            elem.click,
            lambda: self.driver.execute_script("arguments[0].click();", elem),
            lambda: ActionChains(self.driver).move_to_element(elem).click().perform(),
        ]:
            try:
                method()
                return
            except Exception:
                continue
        raise Exception("Не удалось подтвердить заказ")

    @allure.step("Нажать кнопку 'Посмотреть статус' в модальном окне")
    def click_view_status_on_modal(self):
        elem = self.find_element(self.locators.MODAL_VIEW_STATUS_BUTTON)
        self.scroll_into_view(elem)
        for method in [
            elem.click,
            lambda: self.driver.execute_script("arguments[0].click();", elem),
            lambda: ActionChains(self.driver).move_to_element(elem).click().perform(),
        ]:
            try:
                method()
                return
            except Exception:
                continue
        raise Exception("Не удалось нажать кнопку 'Посмотреть статус'")

    @allure.step("Нажать логотип Самокат")
    def click_scooter_logo(self):
        logo = self.find_element(self.locators.LOGO_SCOOTER)
        self.scroll_into_view(logo)
        for method in [
            logo.click,
            lambda: self.driver.execute_script("arguments[0].click();", logo),
            lambda: ActionChains(self.driver).move_to_element(logo).click().perform(),
        ]:
            try:
                method()
                return
            except Exception:
                continue
        raise Exception("Не удалось нажать логотип 'Самокат'")

    @allure.step("Проверить, что текущий URL — главная страница")
    def wait_for_main_page(
        self, expected_url="https://qa-scooter.praktikum-services.ru/", timeout=15
    ):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url == expected_url
        )

    @allure.step("Нажать логотип Яндекс")
    def click_yandex_logo(self):
        logo = self.find_element(self.locators.LOGO_YANDEX)
        self.scroll_into_view(logo)
        for method in [
            logo.click,
            lambda: self.driver.execute_script("arguments[0].click();", logo),
            lambda: ActionChains(self.driver).move_to_element(logo).click().perform(),
        ]:
            try:
                method()
                return
            except Exception:
                continue
        raise Exception("Не удалось нажать логотип 'Яндекс'")

    def switch_to_new_window(self):
        super().switch_to_new_window()

    def wait_for_order_status_page(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: "status" in d.current_url or "track" in d.current_url
        )

    def wait_for_dzen_page(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: "dzen.ru" in d.current_url or "yandex.ru" in d.current_url
        )

    def is_success_popup_visible(self) -> bool:
        try:
            WebDriverWait(self.driver, self.timeout).until(
                lambda d: d.find_element(*self.locators.SUCCESS_POPUP).is_displayed()
            )
            return True
        except Exception:
            return False

    def get_success_popup_text(self) -> str:
        elem = self.find_visible_element(self.locators.SUCCESS_POPUP_TEXT)
        return elem.text
