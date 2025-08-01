from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Кнопки «Заказать» на главной странице (2 варианта)
    ORDER_BUTTON_1 = (
        By.XPATH,
        "(//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')])[1]",
    )
    ORDER_BUTTON_2 = (
        By.XPATH,
        "(//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать')])[2]",
    )

    # Поля формы заказа
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']",
    )

    # Поле "Когда привезти самокат"
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # Дропдаун "Срок аренды"
    RENTAL_PERIOD_DROPDOWN = (
        By.CSS_SELECTOR,
        "div.Dropdown-control[aria-haspopup='listbox']",
    )

    @staticmethod
    def rental_period_option(text):
        return (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-menu')]//div[contains(@class, 'Dropdown-option') and normalize-space(text())='{text}']",
        )

    # Кнопка "Далее"
    NEXT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Далее')]",
    )

    # Финальная кнопка "Заказать"
    ORDER_FINAL_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[contains(text(), 'Заказать') and contains(@class, 'Button_Button__ra12g')]",
    )

    # Кнопка согласия с cookie
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # Модальное окно успешного заказа и связанные элементы
    SUCCESS_POPUP = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_POPUP_TEXT = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    MODAL_CONFIRM_BUTTON_YES = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal__YZ-d3')]//button[contains(text(), 'Да')]",
    )
    MODAL_VIEW_STATUS_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal__YZ-d3')]//button[contains(text(), 'Посмотреть статус')]",
    )

    # Логотипы
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
