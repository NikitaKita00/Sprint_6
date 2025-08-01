import pytest
import allure
from project.pages.main_page import MainPage
from project.pages.order_page import OrderPage

ORDER_DATA = [
    {
        "name": "Иван",
        "surname": "Иванов",
        "address": "ул. Пушкина, д.10",
        "metro": "Бульвар Рокоссовского",
        "phone": "+79991112233",
    },
    {
        "name": "Мария",
        "surname": "Смирнова",
        "address": "пр. Ленина, д.45",
        "metro": "Таганская",
        "phone": "+79123334455",
    },
]


@pytest.mark.parametrize("order_data", ORDER_DATA)
@allure.feature("Оформление заказа")
@allure.story("Позитивный сценарий оформления заказа")
def test_positive_order_scenario(driver, order_data):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    with allure.step("Открыть главную страницу"):
        main_page.open()
        main_page.wait_for_load()

    with allure.step("Нажать кнопку 'Заказать' на главной странице"):
        main_page.click_order_button(index=0)

    with allure.step("Заполнить данные для заказа"):
        order_page.fill_name(order_data["name"])
        order_page.fill_surname(order_data["surname"])
        order_page.fill_address(order_data["address"])
        order_page.select_metro_station(order_data["metro"])
        order_page.fill_phone(order_data["phone"])

    with allure.step("Нажать кнопку 'Далее'"):
        order_page.click_next_button()

    with allure.step("Заполнить дату доставки самоката"):
        order_page.fill_delivery_date("24.07.2025")

    with allure.step("Выбрать срок аренды 'двое суток'"):
        order_page.select_rental_period("двое суток")

    with allure.step("Нажать финальную кнопку 'Заказать'"):
        order_page.click_order_final_button()

    with allure.step("Подтвердить заказ в модальном окне"):
        order_page.confirm_order()
        assert (
            order_page.is_success_popup_visible()
        ), "Модальное окно подтверждения не появилось"

    with allure.step("Нажать кнопку 'Посмотреть статус' в модальном окне"):
        order_page.click_view_status_on_modal()

    with allure.step("Проверить переход на страницу статуса заказа"):
        order_page.wait_for_order_status_page()
        assert (
            "status" in order_page.driver.current_url
            or "track" in order_page.driver.current_url
        ), "Переход на страницу статуса не произошёл"

    with allure.step(
        "Проверить переход на главную страницу Самоката по клику на логотип"
    ):
        order_page.click_scooter_logo()
        order_page.wait_for_main_page()
        assert (
            order_page.driver.current_url == "https://qa-scooter.praktikum-services.ru/"
        ), "Не произошёл переход на главную страницу Самоката"

    with allure.step("Проверить переход на страницу Дзена по логотипу Яндекса"):
        order_page.click_yandex_logo()
        order_page.switch_to_new_window()
        order_page.wait_for_dzen_page()
        current_url = order_page.driver.current_url
        assert (
            "dzen.ru" in current_url or "yandex.ru" in current_url
        ), f"Ожидался редирект на Дзен, открыт: {current_url}"
