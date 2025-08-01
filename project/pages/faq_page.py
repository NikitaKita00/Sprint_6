from selenium.common.exceptions import TimeoutException
from project.locators.faq_page_locators import FAQPageLocators
from project.pages.base_page import BasePage


class FAQPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FAQPageLocators()

    def scroll_to_faq(self):
        try:
            faq_section_element = self.find_element(
                self.locators.FAQ_SECTION
            )  # Ищем элемент
            self.scroll_into_view(faq_section_element)  # Передаём элемент, а не локатор
        except TimeoutException:
            raise Exception("Не удалось найти раздел FAQ на странице")

    def get_question_text(self, index):
        try:
            question = self.find_visible_element(self.locators.QUESTION(index))
            return question.text
        except TimeoutException:
            raise Exception(f"Не удалось найти вопрос с индексом {index}")

    def click_question(self, index):
        try:
            self.click(self.locators.QUESTION(index))
        except TimeoutException:
            raise Exception(f"Не удалось кликнуть на вопрос с индексом {index}")

    def get_answer_text(self, index):
        try:
            answer = self.find_visible_element(self.locators.ANSWER(index))
            return answer.text
        except TimeoutException:
            raise Exception(f"Не удалось найти ответ для вопроса с индексом {index}")
