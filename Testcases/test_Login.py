import pytest
from Config.LoginInfo import UserData
from Pages.Login import LoginPage
from Testcases.test_base import BaseTest





class Test_Loginclass(BaseTest):


    @pytest.mark.sanity
    def test_launch_demo_qa(self):
        self.obj2 = LoginPage(self.driver)
        elements_card = self.obj2.launch_demo_qa()
        assert elements_card == True

    def test_assertheader(self):
        self.obj1 = LoginPage(self.driver)
        header = self.obj1.assertheader()
        assert header.text == "Elements"

    # @pytest.mark.skip(reason="Already checked through` conftest")
    # def test_resetpwd(self):
    #     self.reset = LoginPage(self.driver)
    #     self.reset.ResetPassword(UserData.USERNAME)
    #
    # #@pytest.mark.skip(reason="Already checked through` conftest")
    # def test_subscribe(self):
    #     self.sub = LoginPage(self.driver)
    #     self.sub.Subscribe()
    #
    # @pytest.mark.skip(reason="Already checked through` conftest")
    # def test_register(self):
    #     self.register_obj = LoginPage(self.driver)
    #     self.register_obj.Register()
    #
    # @pytest.mark.parametrize("Username , Password",
    #                          get_cel_data_rows())
    # def test_validate(self, Username, Password):
    #     self.valid_obj = LoginPage(self.driver)
    #     self.valid_obj.validCredentials(Username,Password)
