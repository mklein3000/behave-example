from behave import given, when, then
from calculator import Calculator

@given(u'Calculator app is run')
def step_impl(context):
    context.calculator = Calculator()
    print(u'Step: Given Calculator app is run')

@when(u'I input "{a}" to calculator')
def step_impl(context, a):
    context.calculator.set(a)

@when(u'I input plus "{a}" to calculator')
def step_impl(context, a):
    context.calculator.add(a)

@then(u'I get result "{out}"')
def step_impl(context, out):
    assert context.calculator.result == int(out), "Invalid result is returned. got %d" % context.calculator.result
    
@when(u'multiplicate with "{a}"')
def step_impl(context, a):
    context.calculator.mul(a)