import allure
from page.base_page import BasePage
from web_locators.locators import *
from selenium.webdriver.support.wait import WebDriverWait
from web_locators.locators import YaScooterHomePageLocator as Locators


class YaScooterHomePage(BasePage):
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.FAQ_BUTTONS, 10)
        return elems[question_number].click()


    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        return self.find_element(BasePageLocator.YANDEX_SITE_BUTTON).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Сравнение вопроса')
    def test_answer_number(self, answer_number):
        elems2 = self.find_element(YaScooterHomePageLocator.FAQ_ANSWER, 10)
        return elems2[answer_number]
