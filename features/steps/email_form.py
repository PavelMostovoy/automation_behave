import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from utilites.env import Env


use_step_matcher("re")


@when("I open website (?P<link>.+) using (?P<browser>.+)")
def step_impl(context, link, browser):
    """
    :type context: behave.runner.Context
    :type link: str
    :type browser: str
    """
    print(f"Opening {link} in {browser}")
    client = getattr(context, browser)
    client.get(link)
    time.sleep(Env.vars['wait_time'])
    attach(
        client.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )


@when("I change (?P<reply_form>.+) and fill up (?P<data>.+) in (?P<field>.+) using (?P<browser>.+)")
def step_impl(context, reply_form, data, field, browser):
    """
    :type context: behave.runner.Context
    :type reply_form: str
    :type data: str
    :type field: str
    :type browser: str
    """
    client = getattr(context, browser)
    element = client.find_element(By.XPATH, reply_form)
    assert element, "Element not found"
    element.click()
    print(f"Element {reply_form} found and reply form successfully changed")
    element = client.find_element(By.XPATH, field)
    assert element, "Element not found"
    print(f"Element {field} found")
    element.send_keys(data)
    print(f"Data {data} successfully filled up")
    time.sleep(Env.vars['wait_time'])


@when("I press the submit (?P<button>.+) using (?P<browser>.+)")
def step_impl(context, button, browser):
    """
    :type context: behave.runner.Context
    :type button: str
    :type browser: str
    """
    client = getattr(context, browser)
    element = client.find_element(By.XPATH, button)
    assert element, "Element not found"
    print(f"Element {button} found")
    element.click()
    print("Button click successful")
    time.sleep(Env.vars['wait_time'])


@then("I check (?P<message>.+) in (?P<element>.+) using (?P<browser>.+)")
def step_impl(context, message, element, browser):
    """
    :type context: behave.runner.Context
    :type message: str
    :type element: str
    :type browser: str
    """
    client = getattr(context, browser)
    find_message = client.find_element(By.XPATH, element)
    attach(
        client.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )
    actual_message = find_message.text
    assert actual_message == message,\
        f"Message is '{actual_message}' but expected should be '{message}'"
    print(f"Message '{actual_message}' successfully verified")
    time.sleep(Env.vars['wait_time'])
