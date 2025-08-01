import pytest
import allure


@pytest.fixture(scope="function")
def driver(request):
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    if request.node.rep_call.failed:
        with allure.step("Attach screenshot on failure"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
