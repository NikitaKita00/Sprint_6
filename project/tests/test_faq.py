import pytest
import allure
import time
from project.pages.main_page import MainPage
from project.pages.faq_page import FAQPage


FAQ_DATA = [
    (
        1,
        "Сколько это стоит? И как оплатить?",
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
    ),
    (
        2,
        "Хочу сразу несколько самокатов! Так можно?",
        "Пока что у нас так: один заказ — один самокат.",
    ),
    (
        3,
        "Как рассчитывается время аренды?",
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру.",
    ),
    (
        4,
        "Можно ли заказать самокат прямо на сегодня?",
        "Только начиная с завтрашнего дня.",
    ),
    (
        5,
        "Можно ли продлить заказ или вернуть самокат раньше?",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
    ),
    (
        6,
        "Вы привозите зарядку вместе с самокатом?",
        "Самокат приезжает к вам с полной зарядкой.",
    ),
    (7, "Можно ли отменить заказ?", "Да, пока самокат не привезли."),
    (
        8,
        "Я жизу за МКАДом, привезёте?",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
    ),
]


@allure.feature("Тесты раздела FAQ")
@pytest.mark.parametrize("index,question,answer", FAQ_DATA)
def test_faq_questions(driver, index, question, answer):
    main_page = MainPage(driver)
    faq_page = FAQPage(driver)

    with allure.step("Открыть главную страницу"):
        main_page.open()
        main_page.wait_for_load()

    with allure.step("Прокрутить до раздела FAQ"):
        faq_page.scroll_to_faq()
        time.sleep(1)  # Даём время для завершения анимации

    with allure.step(f'Проверить вопрос: "{question}"'):
        question_text = faq_page.get_question_text(index)
        assert (
            question in question_text
        ), f"Ожидался вопрос: '{question}', получен: '{question_text}'"

    with allure.step("Кликнуть на вопрос и проверить ответ"):
        faq_page.click_question(index)
        time.sleep(0.5)  # Даём время для раскрытия ответа
        answer_text = faq_page.get_answer_text(index)
        assert (
            answer in answer_text
        ), f"Ожидался ответ: '{answer}', получен: '{answer_text}'"
