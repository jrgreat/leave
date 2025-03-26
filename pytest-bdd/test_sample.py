import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import requests

class ApiCaller:
    def __init__(self):
        self.api = None
        self.methods = None
        self.types = None
        self.params = None

    def call_api(self):
        print(self.api)
        result = requests.request(method,'http://' + self.api)
        return result

scenarios('sample.feature')

@pytest.fixture
@given('我是测试接口')
def api_caller():
    return ApiCaller()


@when(parsers.parse('调用 "{api}" 接口'))
def api(api_caller, api):
    api_caller.api = api


@when(parsers.parse('使用 "{methods}" 请求'))
def method(api_caller, methods):
    api_caller.methods = methods


@then('调用成功')
def asserts(api_caller):
    result = api_caller.call_api()
    assert result.status_code == 200