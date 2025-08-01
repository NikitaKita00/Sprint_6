from selenium.webdriver.common.by import By


class FAQPageLocators:
    FAQ_SECTION = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")
    QUESTION = lambda self, index: (
        By.XPATH,
        f"//div[@data-accordion-component='AccordionItem'][{index}]//div[@data-accordion-component='AccordionItemHeading']",
    )
    ANSWER = lambda self, index: (
        By.XPATH,
        f"//div[@data-accordion-component='AccordionItem'][{index}]//div[@data-accordion-component='AccordionItemPanel']",
    )
