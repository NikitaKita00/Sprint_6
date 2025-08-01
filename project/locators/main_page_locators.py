from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    FOOTER_ORDER_BUTTON = (
        By.XPATH,
        "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']",
    )
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    MAIN_PAGE_CONTENT = (
        By.XPATH,
        "//div[contains(text(), 'Привезём его прямо к вашей двери')]",
    )
