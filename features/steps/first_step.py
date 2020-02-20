from behave import *
from selenium.webdriver.common.by import By

from helpers.sut import Sut

@given('website')
def step_impl(context):
    context.browser = Sut("chrome", options=True).get_web_driver()
    context.browser.get('https://dev.svetlitsky.photography/')
    context.browser.implicitly_wait(5)


@then('looking for title')
def step_impl(context):
    assert 'Newborn Photography In Toronto & GTA\n' \
           'In the comfort of Your Home' \
           == context.browser.find_element(By.XPATH, '/html[1]' \
            '/body[1]/div[1]/section[1]/div[1]/h1[1]').text
    context.browser.quit()


@step("my first step")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    return True


@then("Open New Window")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Open New Window')
