from behave import given, when, then
from src.number_checker import check_number
# TODO: Importáld a number_checker modult a src mappából


# TODO: Implementáld a Given step-et
# @given('the number is {number}')
# def step_given_number(context, number):
    

@given('the number is 4')
def step_given_number(context):
    context.number = 4

@given('the number is 3')
def step_given_number(context):
    context.number = 3


# TODO: Implementáld a When step-et
# Használd a check_number függvényt a src/number_checker.py fájlból!
@when('I check the number')
def step_when_check_number(context):
    context.result = check_number(context.number)

# TODO: Implementáld a Then step-et
@then('I should be told "{expected}"')
def step_then_result(context, expected):
    assert context.result == expected, f'Az elvárt eredmény {expected}, a kapott eredmény {context.result}'
