import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")


@when("I open (?P<link>.+) using (?P<browser>.+)")
def step_impl(context, link, browser):
    """
    :type context: behave.runner.Context
    :type link: str
    :type browser: str
    """
    print('Opening {} in {}'.format(link, browser))
    client = getattr(context, browser)
    client.get(link)
    time.sleep(1)
    attach(
        client.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )


@when("I find (?P<field>.+) using (?P<browser>.+)")
def step_impl(context, field, browser):
    """
    :type context: behave.runner.Context
    :type field: str
    :type browser: str
    """
    client = getattr(context, browser)
    element = client.find_element(By.XPATH, field)
    # wrong way
    assert element, "Element not found"
    print("Element {} found".format(field))
    context.element = element
    time.sleep(1)


@when("I fill (?P<data>.+) in (?P<field>.+) using (?P<browser>.+)")
def step_impl(context, data, field, browser):
    """
    :type context: behave.runner.Context
    :type data: str
    :type field: str
    :type browser: str
    """
    client = getattr(context, browser)
    # still wrong way
    element = context.element
    element.send_keys(data)
    # element = client.find_element(By.XPATH, field)
    print("Data {} successfully filled".format(data))
    time.sleep(1)


@when("I press the (?P<button>.+) using (?P<browser>.+)")
def step_impl(context, button, browser):
    """
    :type context: behave.runner.Context
    :type button: str
    :type browser: str
    """
    client = getattr(context, browser)
    element = client.find_element(By.XPATH, button)
    element.click()
    print("Button click successful ")
    time.sleep(1)


@then("I verify (?P<message>.+) in (?P<element>.+) using (?P<browser>.+)")
def step_impl(context, message, element, browser):
    """
    :type context: behave.runner.Context
    :type message: str
    :type element: str
    :type browser: str
    """
    client = getattr(context, browser)
    element = client.find_element(By.XPATH, element)
    attach(
        client.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )
    actual_message = element.text
    assert actual_message == message, "Message is '{}' but expected should be '{}' ".format(actual_message, message)
    print("Message '{}' successfully verified")
    time.sleep(1)
