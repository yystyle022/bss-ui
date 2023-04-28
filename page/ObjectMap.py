import time
from time import sleep


class ObjectMap:
    def element_appear(self, driver, locateType, locateValue, timeout=5):
        '''
        判断元素是否出现
        @param driver: 驱动
        @param locateType: 定位方式
        @param locateValue: 定位值
        @param timeout: 超时时间
        @return:
        '''
        if locateType:
            startTime = time.time() * 1000
            stopTime = startTime + (timeout * 1000)
            for i in range(int(timeout * 10)):
                try:
                    element = driver.find_element('{}'.format(locateType), '{}'.format(locateValue))
                    if element.is_displayed():
                        return True
                except Exception:
                    nowTime = time.time() * 1000
                    if nowTime > stopTime:
                        break
                    else:
                        sleep(0.1)
            return False
        else:
            raise Exception('未传入定位方式，请传入正确的定位方式')

    def element_disappear(self, driver, locateType, locateValue, timeout=10):
        '''
        判断元素是否消失
        @param driver: 驱动
        @param locateType: 定位方式
        @param locateValue: 定位值
        @param timeout: 超时时间
        @return:
        '''
        if locateType:
            startTime = time.time() * 1000
            stopTime = startTime + (timeout * 1000)
            for i in range(int(timeout * 10)):
                try:
                    element = driver.find_element('{}'.format(locateType), '{}'.format(locateValue))
                    if element.is_displayed():
                        nowTime = time.time() * 1000
                        if nowTime > stopTime:
                            break
                        else:
                            sleep(0.1)
                except Exception:
                    return True
            return False
        else:
            raise Exception('未传入定位方式，请传入正确的定位方式')
