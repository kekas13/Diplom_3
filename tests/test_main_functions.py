import pytest
import allure
from pages.main_page import MainPage
from locators.main_locators import MainLocators
from urls import Urls


class TestMainFunctions:

    @allure.title('Проверяем переход в конструктор по кнопке "Конструктор"')
    @allure.description('Открываем страницу логина, нажимаем кнопку "конструктор", '
                        'проверяем, что появляется элемент "соберите бургер"')
    def test_transfer_by_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_page(Urls.LOGIN_PAGE)
        main_page.click_on_constructor()
        assert main_page.find_constructor()

    @allure.title('Проверяем переход на ленту заказов по кнопке "Лента заказов"')
    @allure.description('Открываем главную страницу, нажимаем кнопку "лента заказов", '
                        'проверяем, что появляется лента заказов')
    def test_transfer_by_click_order_line(self, driver):
        main_page = MainPage(driver)
        main_page.go_page(Urls.MAIN_PAGE)
        main_page.click_order_line_button()
        assert main_page.find_order_line(), 'не найдена лента заказов'

    @allure.title('Проверяем, что клик по ингредиенту вызывает всплывающее окно с деталями')
    @allure.description('Открываем главную страницу, нажимаем кнопку ингредиента, '
                        'проверяем, что появляется всплывающее окно с деталями')
    def test_show_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.go_page(Urls.MAIN_PAGE)
        main_page.click_order_element()
        assert main_page.find_pop_up_details(), 'не найдено всплывающее окно с деталями'

    @allure.title('Проверяем, что всплывающее окно закрывается кликом по крестику')
    @allure.description('Открываем главную страницу, нажимаем кнопку ингредиента, появляется окно с деталями, '
                        'нажимаем крестик на окне с деталями, ожидаем, что окно с деталями закроется')
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.go_page(Urls.MAIN_PAGE)
        main_page.click_order_element()
        main_page.find_pop_up_details()
        main_page.click_close_details_button()
        assert main_page.not_find_pop_up_details(), 'не закрывается окно с деталями'

    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('Открываем главную страницу, перетаскиваем ингредиент из списка ингредиентов в заказ, '
                        'ожидаем, что счетчик ингредиента увеличится: для булки - на 2, для соуса - на 1')
    @pytest.mark.parametrize('element,element_counter,count', [
        [MainLocators.ORDER_LINE_ELEMENT_BUN, MainLocators.ORDER_BUN_COUNTER, '2'],
        [MainLocators.ORDER_LINE_ELEMENT_SAUCE, MainLocators.ORDER_SAUCE_COUNTER, '1']])
    def test_add_ingredient_counter(self, driver, element, element_counter, count):
        main_page = MainPage(driver)
        main_page.go_page(Urls.MAIN_PAGE)
        main_page.drag_ingredient_to_order(element)
        assert main_page.get_ingredient_counter(element_counter) == count, 'неверно работает счетчик ингредиентов'
