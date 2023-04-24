from time import sleep
import allure


def add_img_to_report(driver, step_name, need_sleep=True):
    '''
    截图并插入allure测试报告
    @param driver:
    @param step_name:
    @param need_sleep:
    @return:
    '''
    if need_sleep:
        sleep(2)
    allure.attach(driver.get_screenshot_as_png(),step_name + '.png', attachment_type=allure.attachment_type.PNG)
