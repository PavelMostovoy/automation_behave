from behave import *
import selenium

use_step_matcher("re")


@given("we have behave installed")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have behave installed')