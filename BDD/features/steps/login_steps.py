from behave import given, when, then
from selenium import webdriver

@given('the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://example.com/login")

@when('the user enters valid username and password')
def step_impl(context):
    username_input = context.driver.find_element_by_id("username")
    password_input = context.driver.find_element_by_id("password")
    username_input.send_keys("valid_user")
    password_input.send_keys("valid_password")
    context.driver.find_element_by_id("login_button").click()

@then('the user should be redirected to the home page')
def step_impl(context):
    assert "Home Page" in context.driver.title
    context.driver.quit()