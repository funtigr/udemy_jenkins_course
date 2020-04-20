import pytest
from selenium.webdriver import Chrome

# similar to beforetest and aftertest pytest can be set by fixture syntax
#@pytest.fixture(scope="module") # before and after the whole suite
@pytest.fixture() # before and after every test-case
def setPath():
    global driver  # declares a global variable for the module
    driver = Chrome()
    yield
    driver.close()  # that's executed after every testcase

def test_registration_valid_data(setPath):  # put the fixture function name in parentheses
    driver.get("http://www.testingworld.com/testing/")

# skipping particular tests
@pytest.mark.skip("Don't want to execute at current build.")
def test_registration_valid_data_new(setPath):
    driver.get("http://www.testingworld.com/testing/")

# skipping on condition
a = 105
@pytest.mark.skipif(a<100, reason="Don't want to execute at current build.")
def test_registration_valid_data_new_new(setPath):
    driver.get("http://www.thetestingworld.com/testing/")

# to execute specific cases from terminal: pytest -k test_case_name
# to execute specific cases from terminal with word someword in the test-case name: pytest -k test_someword /no "" needed


# grouping testcases
# in terminal: pytest -m Smoke  /any word may be there
@pytest.mark.Smoke
def some_smoke_test():
    driver.get("http://www.testingworld.com/testing/")

@pytest.mark.Sanity
def some_sanity_test():
    driver.get("http://www.testingworld.com/testing/")

@pytest.mark.Smoke
def some_smoke_test_one():
    driver.get("http://www.testingworld.com/testing/")