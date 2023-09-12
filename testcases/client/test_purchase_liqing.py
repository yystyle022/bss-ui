import allure
from page.LoginPage import LoginPage
from page.ClientLiQingDetailPage import ClientLiQingDetailPage


@allure.feature('客户端购买厘清账号')
class TestPurchaseLiqing():
    @allure.story('首页购买厘清账号，验证账号是否购买成功')
    @allure.description('首页购买厘清账号')
    def test_purchase_liqing_for_homepage(self, driver, url, username, password, active=1, bind=1, duration=1, sum=1):
        '''
        首页购买差分账号
        @param driver:
        @param url:
        @param username:
        @param password:
        @param active:激活方法 1：自动激活、2：手动激活
        @param bind:绑定方法 1：自动绑定、2：手动绑定
        @param duration:购买时长 1：天、 2：月、 3：年
        @param sum:购买总数
        @return:
        '''
        with allure.step('登录官网进入首页'):
            LoginPage().login(driver, url, username, password)
        with allure.step('首页购买厘清账号'):
            ClientLiQingDetailPage().purchaseLiQing(driver, active, bind, duration, sum)
