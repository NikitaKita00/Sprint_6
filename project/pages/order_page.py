import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from project.locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = OrderPageLocators()

    @allure.step("Заполнить поле Имя: {name}")
    def fill_name(self, name: str):
        time.sleep(2)
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.INPUT_NAME)
        )
        elem.clear()
        elem.send_keys(name)

    @allure.step("Заполнить поле Фамилия: {surname}")
    def fill_surname(self, surname: str):
        time.sleep(2)
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.INPUT_SURNAME)
        )
        elem.clear()
        elem.send_keys(surname)

    @allure.step("Заполнить поле Адрес: {address}")
    def fill_address(self, address: str):
        time.sleep(2)
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.INPUT_ADDRESS)
        )
        elem.clear()
        elem.send_keys(address)

    @allure.step("Выбрать станцию метро: {metro_name}")
    def select_metro_station(self, metro_name: str):
        time.sleep(2)
        input_metro = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.INPUT_METRO)
        )
        input_metro.click()
        input_metro.clear()
        input_metro.send_keys(metro_name)

        option_xpath = f"//*[normalize-space(text())='{metro_name}']"
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option.click()

    @allure.step("Заполнить поле Телефон: {phone}")
    def fill_phone(self, phone: str):
        time.sleep(2)
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.INPUT_PHONE)
        )
        elem.clear()
        elem.send_keys(phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        elem = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.NEXT_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", elem
        )

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
                time.sleep(2)
                return
            except Exception:
                continue
        raise Exception("Не удалось кликнуть кнопку 'Далее'")

    @allure.step("Заполнить дату доставки: {date_str}")
    def fill_delivery_date(self, date_str: str):
        time.sleep(2)
        elem = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.DELIVERY_DATE_INPUT)
        )
        elem.click()
        elem.clear()
        elem.send_keys(date_str)

    @allure.step("Выбрать срок аренды: {period_text}")
    def select_rental_period(self, period_text: str):
        time.sleep(2)
        self.driver.execute_script(
            """
            const datepicker = document.querySelector('.react-datepicker');
            if (datepicker) { datepicker.style.display = 'none'; }
            """
        )
        self.driver.find_element(By.TAG_NAME, "body").click()

        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.RENTAL_PERIOD_DROPDOWN)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", dropdown
        )

        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )

        dropdown.click()

        menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Dropdown-menu"))
        )

        option_xpath = f".//div[contains(@class,'Dropdown-option') and normalize-space(text())='{period_text}']"
        option = WebDriverWait(menu, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(option).click().perform()

    @allure.step("Принять cookie")
    def accept_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.locators.COOKIE_ACCEPT_BUTTON)
            )
            cookie_button.click()
        except Exception:
            pass

    @allure.step("Нажать финальную кнопку 'Заказать'")
    def click_order_final_button(self):
        self.accept_cookies()
        elem = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.ORDER_FINAL_BUTTON)
        )
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", elem
        )
        time.sleep(0.3)

        for method in [
            elem.click,
            lambda: self.driver.execute_script("arguments[0].click();", elem),
            lambda: ActionChains(self.driver).move_to_element(elem).click().perform(),
        ]:
            try:
                method()
                time.sleep(2)
                return
            except Exception:
                continue

        raise Exception("Не удалось нажать кнопку 'Заказать'")

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        elem = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.MODAL_CONFIRM_BUTTON_YES)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", elem
        )
        try:
            elem.click()
            time.sleep(2)
        except Exception:
            try:
                self.driver.execute_script("arguments[0].click();", elem)
                time.sleep(2)
            except Exception:
                actions = ActionChains(self.driver)
                actions.move_to_element(elem).click().perform()
                time.sleep(2)

    @allure.step("Нажать кнопку 'Посмотреть статус' в модальном окне")
    def click_view_status_on_modal(self):
        elem = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.MODAL_VIEW_STATUS_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", elem
        )
        try:
            elem.click()
            time.sleep(2)
        except Exception:
            try:
                self.driver.execute_script("arguments[0].click();", elem)
                time.sleep(2)
            except Exception:
                actions = ActionChains(self.driver)
                actions.move_to_element(elem).click().perform()
                time.sleep(2)

    @allure.step("Нажать логотип Самокат")
    def click_scooter_logo(self):
        logo = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.LOGO_SCOOTER)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", logo
        )
        time.sleep(0.5)

        for method in [
            logo.click,
            lambda: self.driver.execute_script("arguments[0].click();", logo),
            lambda: ActionChains(self.driver).move_to_element(logo).click().perform(),
        ]:
            try:
                method()
                time.sleep(2)
                return
            except Exception:
                continue

        raise Exception("Не удалось нажать логотип 'Самокат'")

    @allure.step("Проверить, что текущий URL — главная страница")
    def is_main_page(
        self, expected_url="https://qa-scooter.praktikum-services.ru/"
    ) -> bool:
        WebDriverWait(self.driver, 15).until(lambda d: d.current_url == expected_url)
        return self.driver.current_url == expected_url

    @allure.step("Нажать логотип Яндекс")
    def click_yandex_logo(self):
        logo = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.LOGO_YANDEX)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", logo
        )
        time.sleep(0.3)

        for method in [
            logo.click,
            lambda: self.driver.execute_script("arguments[0].click();", logo),
            lambda: ActionChains(self.driver).move_to_element(logo).click().perform(),
        ]:
            try:
                method()
                time.sleep(2)
                return
            except Exception:
                continue

        raise Exception("Не удалось нажать логотип 'Яндекс'")

    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

    def is_success_popup_visible(self) -> bool:
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.locators.SUCCESS_POPUP)
            )
            return True
        except Exception:
            return False

    def get_success_popup_text(self) -> str:
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.SUCCESS_POPUP_TEXT)
        )
        return elem.text
