from behave import *
from selenium import webdriver

use_step_matcher("re")


@given("we have behave installed")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have behave installed')


@given("Browser name Chrome")
def step_impl(context):
    context.driver = webdriver.Chrome()
