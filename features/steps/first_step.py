from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers.sut import Sut


@given('website')
def step_impl(context):
    context.browser = Sut("chrome", options=True).get_web_driver()
    context.browser.get('https://stackoverflow.com/')
    context.browser.implicitly_wait(5)


@then('looking for title')
def step_impl(context):
    assert 'We build products that empower developers and connect them' \
           ' to solutions that' \
           ' enable productivity, growth,' \
           ' and discovery.' \
           == context.browser.find_element(By.CLASS_NAME,
                                           'fs-title.ta-center').text
    context.browser.quit()


@step("my first step")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And my first step')
