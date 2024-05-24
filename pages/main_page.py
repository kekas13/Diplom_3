import allure
from pages.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):

    @allure.step('Нажимаем на кнопку конструктора')
    def click_on_constructor(self):
        return self.find_element(MainLocators.CONSTRUCT_LINK).click()

    @allure.step('Находим элемент конструкторв "Соберите бургер"')
    def find_constructor(self):
        return self.find_element(MainLocators.CONSTRUCTOR)

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_order_line_button(self):
        return self.find_element(MainLocators.ORDER_LINE_BUTTON).click()

    @allure.step('Находим элемент "Лента заказов"')
    def find_order_line(self):
        return self.find_element(MainLocators.ORDER_LINE)

    @allure.step('Нажимаем кнопку ингредиента')
    def click_order_element(self):
        return self.find_element(MainLocators.ORDER_LINE_ELEMENT_BUN).click()

    @allure.step('Находим элемент "Детали ингредиента"')
    def find_pop_up_details(self):
        return self.find_element(MainLocators.ORDER_ELEMENT_DETAILS_POP_UP)

    @allure.step('Ожидаем отсутствие элемента "Детали ингредиента"')
    def not_find_pop_up_details(self):
        return self.not_find_element(MainLocators.ORDER_ELEMENT_DETAILS_POP_UP)

    @allure.step('Нажимаем кнопку закрытия окна с деталями ингредиента')
    def click_close_details_button(self):
        return self.find_element(MainLocators.CLOSE_DETAILS_BUTTON, 300).click()

    @allure.step('Нажимаем на заказ в ленте заказов')
    def click_order_in_order_line(self):
        return self.find_element(MainLocators.ORDER_IN_ORDER_LINE).click()

    @allure.step('Находим элемент "Детали заказа"')
    def find_order_details(self):
        return self.find_element(MainLocators.ORDER_DETAILS_POP_UP)

    @allure.step('Перетаскиваем ингредиент "булка" в заказ')
    def drag_ingredient_bun_to_order(self):
        drag = self.find_element(MainLocators.ORDER_LINE_ELEMENT_BUN)
        drop = self.find_element(MainLocators.ORDER)
        self.drag_and_drop(drag, drop)

    @allure.step('Перетаскиваем ингредиент "соус" в заказ')
    def drag_ingredient_sauce_to_order(self):
        drag = self.find_element(MainLocators.ORDER_LINE_ELEMENT_SAUCE)
        drop = self.find_element(MainLocators.ORDER)
        self.drag_and_drop(drag, drop)

    @allure.step('Возвращаем текст счетчика элемента')
    def get_ingredient_counter(self, element):
        return self.find_element(element).text

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def click_make_order_button(self):
        return self.find_element(MainLocators.MAKE_ORDER_BUTTON).click()

    @allure.step('Находим элемент оформленного заказа')
    def find_made_order_pop_up(self):
        return self.find_element(MainLocators.MADE_ORDER_POP_UP)

    @allure.step('Находим номер оформленного заказа')
    def get_made_order_pop_up_number(self):
        return self.find_element(MainLocators.MADE_ORDER_POP_UP_NUMBER).text

    @allure.step('Находим номер оформленного заказа')
    def get_made_order_number_in_order_line(self):
        return self.find_element(MainLocators.MADE_ORDER_IN_ORDER_LINE).text

    @allure.step('Находим номер оформленного заказа')
    def get_alltime_order_count(self):
        return self.find_element(MainLocators.ALLTIME_ORDER_COUNTER).text

    @allure.step('Находим номер оформленного заказа')
    def get_daily_order_count(self):
        return self.find_element(MainLocators.DAILY_ORDER_COUNTER).text

    @allure.step('Находим номер заказа в работе')
    def get_order_in_work_number(self):
        return self.find_element(MainLocators.ORDER_IN_WORK).text
