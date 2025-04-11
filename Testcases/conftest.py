import time
from xml.dom.xmlbuilder import Options

import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver

from Config.LoginInfo import UserData
from selenium import webdriver
from Pages.Login import LoginPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        #global web_driver

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        web_driver = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            options=options
        )
        web_driver.maximize_window()


        print("--------------Test Started------------------------")
        web_driver.get(UserData.Base_url)

        # loginPage = LoginPage(web_driver)
        # time.sleep(2)
        # loginPage.validCredentials(UserData.USERNAME, UserData.PASSWORD)
        request.cls.driver = web_driver
        yield
        time.sleep(5)
        #web_driver.close()


# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.h3("Adding prefix message")])
#     summary.extend([html.h3("Adding summary message")])
#     postfix.extend([html.h3("Adding postfix message")])

# def pytest_html_report_title(report):
#      report.title = 'Agreemint'
#
# def pytest_cmdline_preparse(config, args):
#     p = os.getcwd().replace("\\Pages", "")
#     s = p.replace("\\Testcases", "")
#     path = s.__add__("\\Reports\\Agreemint_Report.html")
#
#     config.option.htmlpath = path
#     config.option.self_contained_html = True
#
#
# def pytest_html_results_summary(prefix, summary):
#     prefix.extend([html.h3("This is Sanity Testing Scenarios")])
#     # summary.extend([html.h3("This is Testing Inform")])
#     # postfix.extend([html.h3("Adding postfix message")]
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("https://intelligentcontracts-cls-qa.isg-one.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             screenshot = web_driver.get_screenshot_as_base64()
#             extra.append(pytest_html.extras.image(screenshot, ''))
#         report.extra = extra
#
#


