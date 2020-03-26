import time
from behave import *
from selenium.webdriver.common.by import By
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from utilites.env import Env

use_step_matcher("re")


@when("I go to (?P<link>.+) using (?P<browser>.+)")
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


@step("I pass to (?P<next_page>.+) and verify (?P<url>.+) and (?P<title_name>.+) using (?P<browser>.+)")
def step_impl(context, next_page, url, title_name, browser):
    """
    :type context: behave.runner.Context
    :type next_page: str
    :type url: str
    :type title_name: str
    :type browser: str
    """
    _logger = context.logger
    client = getattr(context, browser)
    element = client.find_element(By.CSS_SELECTOR, next_page)
    assert element, _logger.error(f'Element "{next_page}" not found')
    element.click()
    _logger.info(f'Element "{next_page}" successfully found and redirected to another page')
    time.sleep(Env.vars['page_wait'])
    element = client.find_element(By.CSS_SELECTOR, title_name)
    current_title = element.text
    assert url in client.current_url, _logger.error(f'"{url}" link is not presented')
    _logger.info(f'"{current_title}" page successfully loaded')


@step("I press intro video play (?P<button>.+) using (?P<browser>.+)")
def step_impl(context, button, browser):
    """
    :type context: behave.runner.Context
    :type button: str
    :type browser: str
    """
    _logger = context.logger
    client = getattr(context, browser)
    element = client.find_element(By.CSS_SELECTOR, button)
    assert element, _logger.error(f'Element "{button}" not found')
    _logger.info(f'Element "{button}" successfully found and pressed')
    element.click()
    time.sleep(Env.vars['page_wait'])


@then("I check (?P<video_player>.+) and verify duration and current time using (?P<browser>.+)")
def step_impl(context, video_player, browser):
    """
    :type context: behave.runner.Context
    :type video_player: str
    :type browser: str
    """
    _logger = context.logger
    client = getattr(context, browser)
    element = client.find_element(By.CSS_SELECTOR, video_player)
    # Scroll page to video player
    client.execute_script("return arguments[0].scrollIntoView(true);", element)
    assert element, _logger.error(f'Element "{video_player}" not found')
    _logger.info(f'Element "{video_player}" successfully found')
    time.sleep(Env.vars['wait_time'])
    attach(
        client.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=AttachmentType.PNG
    )
    # From str to float
    duration_time = round(float(element.get_attribute('duration')))
    assert duration_time > 0, _logger.error('Video not found')
    _logger.info(f'Full video duration time is "{duration_time}" seconds')
    current_time = round(float(element.get_attribute('currentTime')))
    assert current_time > 0, _logger.error('Video not played')
    _logger.info(f'Video current time before completing the test is "{current_time}" seconds')
