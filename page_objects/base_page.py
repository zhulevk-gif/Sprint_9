from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver, base_url: str, timeout: int = 10):
        self._driver = driver
        self._base_url = base_url.rstrip("/")
        self._wait = WebDriverWait(driver, timeout, ignored_exceptions=(StaleElementReferenceException,))

    @property
    def driver(self):
        return self._driver

    @property
    def base_url(self):
        return self._base_url

    def open(self, path: str = ""):
        self._driver.get(f"{self._base_url}{path}")

    def current_url_contains(self, text: str) -> bool:
        self._wait.until(ec.url_contains(text))
        return text in self._driver.current_url

    def click_create_account(self):
        self._click(BaseLocators.CREATE_ACCOUNT_LINK)

    def click_login(self):
        self._click(BaseLocators.LOGIN_LINK)

    def click_create_recipe(self):
        self._click(BaseLocators.CREATE_RECIPE_LINK)

    def is_logout_button_visible(self) -> bool:
        return self._is_visible(BaseLocators.LOGOUT_LINK)

    def _find_visible(self, locator):
        return self._wait.until(ec.visibility_of_element_located(locator))

    def _find_clickable(self, locator):
        return self._wait.until(ec.element_to_be_clickable(locator))

    def _find_present(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))

    def _click(self, locator):
        def click_when_ready(driver):
            element = ec.element_to_be_clickable(locator)(driver)
            if not element:
                return False
            element.click()
            return True

        self._wait.until(click_when_ready)

    def _js_click_present(self, locator):
        element = self._find_present(locator)
        self._driver.execute_script("arguments[0].click();", element)


    def _click_text(self, text: str):
        script = """
            const expected = arguments[0];
            const element = Array.from(document.querySelectorAll('button, a, div, span, li'))
                .find((node) => node.textContent.trim() === expected);
            if (!element) {
                return false;
            }
            element.click();
            return true;
        """
        self._wait.until(lambda driver: driver.execute_script(script, text))

    def _type(self, locator, value: str):
        element = self._find_visible(locator)
        element.clear()
        element.send_keys(value)

    def _is_visible(self, locator) -> bool:
        return self._find_visible(locator).is_displayed()
