from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from project.locators.faq_page_locators import FAQPageLocators


class FAQPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = FAQPageLocators()

    def scroll_to_faq(self):
        try:
            faq_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.FAQ_SECTION)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
                faq_section,
            )
        except TimeoutException:
            raise Exception("Не удалось найти раздел FAQ на странице")

    def get_question_text(self, index):
        try:
            question = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.QUESTION(index))
            )
            return question.text
        except TimeoutException:
            raise Exception(f"Не удалось найти вопрос с индексом {index}")

    def click_question(self, index):
        try:
            question = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.QUESTION(index))
            )
            question.click()
        except TimeoutException:
            raise Exception(f"Не удалось кликнуть на вопрос с индексом {index}")

    def get_answer_text(self, index):
        try:
            answer = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.ANSWER(index))
            )
            return answer.text
        except TimeoutException:
            raise Exception(f"Не удалось найти ответ для вопроса с индексом {index}")
