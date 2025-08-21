from selenium.webdriver.common.by import By


class Locators:
    
    # кнопка "Войти в аккаунт" на главной странице
    log_in_to_account_button = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
    # поле "Email"
    email_field = (By.XPATH, "//label[contains(text(), 'Email')]/following::input[1]")

    # поле "Пароль"
    password_field = (By.XPATH, "//label[contains(text(), 'Пароль')]/following::input[1]")

    # надпись "Вход"
    entrance_label = (By.XPATH, "//h2[text()='Вход']")

    # кнопка "Войти" на странице авторизации
    entrance_button = (By.XPATH, "//button[text()='Войти']")

    # кнопка "Зарегистрироваться" на странице авторизации
    registration_button = (By.CSS_SELECTOR, "a[href='/register']")

    # кнопка "Восстановить пароль"
    password_recovery_button = (By.CSS_SELECTOR, "a[href='/forgot-password']")

    # кнопка "Войти" на странице восстановления пароля
    entrance_button_on_recovery_page = (By.CSS_SELECTOR, "a[href='/login']")

    # поле "Имя" на странице регистрации
    name_field = (By.XPATH, "//label[contains(text(), 'Имя')]/following::input[1]")

    # кнопка "Зарегистрироваться" на странице регистрации
    complete_registration_button = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

    # надпись "Некорректный пароль" на странице регистрации
    incorrect_password_label = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

    # надпись "Соберите бургер" на главной странице
    create_burger_title = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

    # кнопка "Личный кабинет" на главной странице
    personal_account_button = (By.CSS_SELECTOR, "a[href='/account']")

    # кнопка "Выход" в личном кабинете
    exit_button = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # надпись "Конструктор" в шапке сайта
    constructor_label = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    # лого Stellar Burgers в шапке сайта
    stellar_burgers_logo = (By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2 a')



