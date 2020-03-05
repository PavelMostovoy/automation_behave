from behave import *
from helpers.data_model import DataModel
use_step_matcher("re")


@given("the user(?:s?)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    model = getattr(context, "model", None)
    if not model:
        context.model = DataModel()
    for row in context.table:
        context.model.add_user(name=row['name'],
                               phone=row['phone'],
                               e_mail=row['e_mail'],
                               comments=row['comments']
                               )
