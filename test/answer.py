import pytest
import allure
from page.home_page import YaScooterHomePage
from data import YaScooterHomePageFAQ
from conftest import *
from page.base_page import *
from page.home_page import *
from web_locators.locators import YaScooterHomePageLocator


@allure.epic('Upgrade Main page / ui usability')
@allure.parent_suite('Parent_suite_Домашняя страница')
@allure.suite('Suite_FAQ')
class TestYaScooterFAQPage:
    @allure.feature('Аккордион с вопрос/ответ на Домашней страницы')
    @allure.story('При нажатии на вопрос в разделе "Вопросы о важном" раскрывается ответ.')
    @allure.title('При нажатии на вопрос раскрывается ответ ')
    @allure.description('Проверка что при нажатии на поле вопроса в блоке "Вопросы о важном", '
                        'данный вопрос раскрывается и текст в нем соответствует ТЗ')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, YaScooterHomePageFAQ.answer1),
            (1, 1, YaScooterHomePageFAQ.answer2),
            (2, 2, YaScooterHomePageFAQ.answer3),
            (3, 3, YaScooterHomePageFAQ.answer4),
            (4, 4, YaScooterHomePageFAQ.answer5),
            (5, 5, YaScooterHomePageFAQ.answer6),
            (6, 6, YaScooterHomePageFAQ.answer7),
            (7, 7, YaScooterHomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.test_go_to_site()
        ya_scooter_home_page.test_click_cookie_accept()
        ya_scooter_home_page.test_click_faq_question(question_number=question)
        answer = ya_scooter_home_page.test_answer_number(answer_number=answer)

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым значением '