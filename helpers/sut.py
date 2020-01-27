# -----------------------------------------------------------------------------
# SYSTEM UNDER TEST:
# -----------------------------------------------------------------------------

from selenium import webdriver


class Sut:

    def __init__(self, client, options=None):
        self.client = client
        self.options = options
        self.diemsions = (720, 1280)
        self.desired_capabilities = {
            "browserName": "chrome",
            "version": "",
            "platform": "ANY",
        }

    def get_web_driver(self):
        if self.options and self.client == 'chrome':
            chrome_options = webdriver.ChromeOptions()

            chrome_options.add_argument("--disable-notifications")

            chrome_options.add_argument("--start-maximized")
            self.desired_capabilities.update(chrome_options.to_capabilities())

        driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor="http://localhost:4444/wd/hub")

        return driver
