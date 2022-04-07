from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _acessar(self, url):
        self.driver.get(url)

    def _encontrar(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _clicar(self, locator):
        self._encontrar(locator).click()

    def _escrever(self, locator, text):
        self._encontrar(locator).send_keys(text)

    def _apagar(self, locator, text):
        self._encontrar(locator).clear(text)

    def _ler(self, locator):
        self._encontrar(locator).text()

    def _rolar_abaixo(self):
        self.driver.execute_script("window.scrollTo(0,450)")

    def _rolar_acima(self):
        self.driver.execute_script("window.scrollTo(0,-450)")



    def _aparecer(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    expected_conditions.visibility_of_element_located(
                        (locator['by'], locator['value'])
                    )
                )
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._encontrar(locator).is_displayed()
            except NoSuchElementException:
                return False
