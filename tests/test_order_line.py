import allure
from pages.main_page import MainPage
from pages.personal_area_page import PersonalAreaPage
from locators.main_locators import MainLocators
from urls import Urls


class TestOrderLine:

    @allure.title('Проверяем, что клик на заказ в ленте заказов вызывает всплывающее окно с деталями заказа')
    @allure.description('Открываем главную страницу, нажимаем кнопку ленты заказов, в ленте заказов нажимаем на заказ '
                        'проверяем, что появляется всплывающее окно с деталями заказа')
    def test_show_order_details(self, driver):
        main_page = MainPage(driver)
        main_page.go_page(Urls.MAIN_PAGE)
        main_page.click_order_line_button()
        main_page.click_order_in_order_line()
        assert main_page.find_order_details(), 'не найдено всплывающее окно с деталями заказа'

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Открываем страницу логина, логинимся, оформляем заказа, получаем номер заказа, '
                        'закрываем окно с заказом и нажимаем на кнопку "Лента заказов", '
                        'проверяем, что номер нашего заказа есть в ленте заказов')
    def test_show_orders_on_order_line(self, login):
        page = PersonalAreaPage(login)
        page.drag_ingredient_to_order(MainLocators.ORDER_LINE_ELEMENT_BUN)
        page.drag_ingredient_to_order(MainLocators.ORDER_LINE_ELEMENT_SAUCE)
        page.click_make_order_button()
        page.find_made_order_pop_up()
        made_order_number = page.get_made_order_pop_up_number()
        page.click_close_details_button()
        page.click_order_line_button()
        assert page.get_made_order_number_in_order_line()[2:] == made_order_number, 'номер в ленте заказов не равен номеру нашего заказа'

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Открываем страницу логина, логинимся, со страницы ленты заказов фиксируем общий счетчик '
                        'заказов "Выполнено за все время", на главной странице оформляем заказ, '
                        'нажимаем на ленту заказов, проверяем, что счетчик Выполнено за всё время увеличился на 1')
    def test_add_order_alltime_counter_increase(self, login):
        page = PersonalAreaPage(login)
        page.click_order_line_button()
        alltime_counter = page.get_alltime_order_count()
        page.go_page(Urls.MAIN_PAGE)
        page.drag_ingredient_to_order(MainLocators.ORDER_LINE_ELEMENT_BUN)
        page.drag_ingredient_to_order(MainLocators.ORDER_LINE_ELEMENT_SAUCE)
        page.click_make_order_button()
        page.click_close_details_button()
        page.click_order_line_button()
        assert int(page.get_alltime_order_count()) == int(alltime_counter) + 1, 'счетчик "Выполнено за все время" не равен ожидаемому значению'

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Открываем страницу логина, логинимся, со страницы ленты заказов фиксируем счетчик заказов '
                        'за сегодня "Выполнено за сегодня", на главной странице оформляем заказ, '
                        'нажимаем на ленту заказов, проверяем, что счетчик "Выполнено за сегодня" увеличился на 1')
    def test_add_order_day_counter_increase(self, login):
        page = PersonalAreaPage(login)
        page.click_order_line_button()
        daily_counter = page.get_daily_order_count()
        page.go_page(Urls.MAIN_PAGE)
        page.drag_ingredient_to_order(MainLocators.ORDER_LINE_ELEMENT_BUN)
        page.drag_ingredient_to_order(MainLocators.ORDER_LINE_ELEMENT_SAUCE)
        page.click_make_order_button()
        page.click_close_details_button()
        page.click_order_line_button()
        assert int(page.get_daily_order_count()) == int(daily_counter), 'счетчик "Выполнено за сегодня" не равен ожидаемому значению'

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    @allure.description('Открываем страницу логина, логинимся, оформляем заказ, переходим в ленту заказов,'
                        'проверяем, что его номер заказа, появляется в разделе "В работе"')
    def test_add_order_show_in_work(self, login):
        page = PersonalAreaPage(login)
        page.drag_ingredient_to_order(MainLocators.ORDER_LINE_ELEMENT_BUN)
        page.drag_ingredient_to_order(MainLocators.ORDER_LINE_ELEMENT_SAUCE)
        page.click_make_order_button()
        page.find_made_order_pop_up()
        page.click_close_details_button()
        page.click_order_line_button()
        assert page.get_order_in_work_number()[1:] == '38679', 'номер заказа не появился в разделе "В работе"'
