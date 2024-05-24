from selenium.webdriver.common.by import By


class LoginPageLocators:

    INPUT_MAIL = (By.XPATH, ".//label[text()='Email']/../input[@value]")
    INPUT_PASSWORD = (By.XPATH, ".//label[text()='Пароль']/../input[@value]")
    ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    PERSONAL_AREA_LINK = (By.XPATH, ".//a[@href='/account']")
    PROFILE = (By.XPATH, ".//a[@href='/account/profile']")
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[@href='/account/order-history']")
    ORDER_HISTORY = (By.XPATH, ".//div[contains(@class,'OrderHistory')]")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
