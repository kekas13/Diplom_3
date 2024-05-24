from selenium.webdriver.common.by import By


class MainLocators:

    CONSTRUCT_LINK = (By.XPATH, ".//p[text()='Конструктор']")
    CONSTRUCTOR = (By.XPATH, ".//h1[text()='Соберите бургер']")

    ORDER_LINE_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    ORDER_LINE = (By.XPATH, ".//div[contains(@class,'OrderFeed_contentBox')]")
    ORDER_LINE_ELEMENT_BUN = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    ORDER_BUN_COUNTER = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[starts-with(@class,'counter')]")
    ORDER_ELEMENT_DETAILS_POP_UP = (By.XPATH, ".//div[contains(@class,'modal__container')]")
    ORDER_LINE_ELEMENT_SAUCE = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")
    ORDER_SAUCE_COUNTER = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//p[starts-with(@class,'counter')]")
    ORDER = (By.XPATH, ".//section[contains(@class,'BurgerConstructor')]")
    ORDER_IN_ORDER_LINE = (By.XPATH, ".//ul[contains(@class,'OrderFeed_list')]//li")
    ORDER_DETAILS_POP_UP = (By.XPATH, ".//div[contains(@class,'Modal_orderBox')]")
    ORDER_IN_WORK = (By.XPATH, ".//ul[contains(@class,'OrderFeed')]/li[contains(@class,'text')]")

    CLOSE_DETAILS_BUTTON = (By.XPATH, ".//button[contains(@class,'close')]")
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    MADE_ORDER_POP_UP = (By.XPATH, ".//div[contains(@class,'modal__contentBox')]")
    MADE_ORDER_POP_UP_NUMBER = (By.XPATH, ".//div[contains(@class,'modal__contentBox')]/h2")
    MADE_ORDER_IN_ORDER_LINE = (By.XPATH, ".//div[contains(@class,'OrderHistory')]/p[contains(@class,'text')]")

    ALLTIME_ORDER_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/../p[contains(@class,'OrderFeed_number')]")
    DAILY_ORDER_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/../p[contains(@class,'OrderFeed_number')]")
