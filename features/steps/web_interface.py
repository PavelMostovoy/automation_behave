import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.env import Env

use_step_matcher("re")


@when("I open (?P<link>.+) using (?P<browser>.+)")
def step_impl(context, link, browser):
    """
    :type context: behave.runner.Context
    :type link: str
    :type browser: str
    """
    _logger = context.logger
    _logger.info('Opening {} in {}'.format(link, browser))
    client = getattr(context, browser)
    client.get(link)
    time.sleep(Env.vars['wait_time'])
    attach(
        client.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )


@step("I choose (?P<reply_form>.+) and fill (?P<user>.+) contact details in (?P<field>.+) using (?P<browser>.+)")
def step_impl(context, reply_form, user, field, browser):
    """
    :type context: behave.runner.Context
    :type reply_form: str
    :type user: str
    :type field: str
    :type browser: str
    """
    user_id = context.model.users[user]
    user_phone = user_id.phone
    user_email = user_id.e_mail
    client = getattr(context, browser)
    element = client.find_element(By.XPATH, reply_form)
    assert element, "Element not found"
    element.click()
    print("Element {} found and reply form successfully changed".format(reply_form))
    element = client.find_element(By.XPATH, field)
    assert element, "Element not found"
    print("Element {} found".format(field))
    if reply_form == '//*[@id="field-reply"]/div/button[2]':
        element.send_keys(user_email)
        print("Data {} successfully filled up".format(user_email))
    else:
        element.send_keys(user_phone)
        print("Data {} successfully filled up".format(user_phone))
    time.sleep(Env.vars['wait_time'])


@step("I leave (?P<user>.+) comment in (?P<comments_field>.+) using (?P<browser>.+)")
def step_impl(context, user, comments_field, browser):
    """
    :type context: behave.runner.Context
    :type user: str
    :type comments_field: str
    :type browser: str
    """
    user_id = context.model.users[user]
    user_comment = user_id.comments
    client = getattr(context, browser)
    element = client.find_element(By.XPATH, comments_field)
    assert element, "Element not found"
    element.send_keys(user_comment)
    print("Comment {} successfully left".format(user_comment))
    time.sleep(Env.vars['wait_time'])


@step("I press the (?P<button>.+) using (?P<browser>.+)")
def step_impl(context, button, browser):
    """
    :type context: behave.runner.Context
    :type button: str
    :type browser: str
    """
    client = getattr(context, browser)
    element = client.find_element(By.XPATH, button)
    assert element, "Element not found"
    element.click()
    print("Button click successful ")
    time.sleep(Env.vars['wait_time'])


@then("I verify (?P<message>.+) in (?P<element>.+) using (?P<browser>.+)")
def step_impl(context, message, element, browser):
    """
    :type context: behave.runner.Context
    :type message: str
    :type element: str
    :type browser: str
    """
    client = getattr(context, browser)
    WebDriverWait(client, Env.vars['driver_wait']).until(
        EC.text_to_be_present_in_element((By.XPATH, element), '{}'.format(message))
    )
    element = client.find_element(By.XPATH, element)
    attach(
        client.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )
    actual_message = element.text
    assert actual_message == message, \
        "Message is '{}' but expected should be '{}' ".format(actual_message,
                                                              message)
    print("Message '{}' successfully verified".format(actual_message))
    time.sleep(Env.vars['wait_time'])
