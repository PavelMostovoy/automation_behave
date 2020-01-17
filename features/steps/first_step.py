from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By



@given('website')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://stackoverflow.com/')
    context.browser.implicitly_wait(5)
@then('looking for title')
def step_impl(context):
    assert 'We build products that empower developers and connect them to solutions that enable productivity, growth, and discovery.' \
           == context.browser.find_element(By.CLASS_NAME, 'fs-title.ta-center').text
    context.browser.quit()

