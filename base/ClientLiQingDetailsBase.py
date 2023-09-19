# -*- coding=utf-8 -*-
# @Time : 2023/9/11 10:38
# @Author : yangyang
# @File : bss-ui/ClientLiQingDetailsBase.py
class ClientLiQingDetailsBase:
    '''
    厘清详情页面Xpath
    '''

    def purchaseDurationOneDayXpath(self):
        '''
        购买时长1天Xpath
        @return:
        '''
        return "//span[text()='天']"

    def purchaseDurationOneMonthXpath(self):
        '''
        购买时长1个月Xpath
        @return:
        '''
        return "//span[text()='个月']"

    def purchaseDurationOneYearXpath(self):
        '''
        购买时长1年Xpath
        @return:
        '''
        return "//span[text()='年']"

    def autoActiveMethodXpath(self):
        '''
        自动激活方式Xpath
        @return:
        '''
        return "//div[contains(text(),'自动激活')]"

    def manualActiveMethodXpath(self):
        '''
        手动激活方式Xpath
        @return:
        '''
        return "//div[contains(text(),'手动激活')]"

    def autoBindMethodXpath(self):
        '''
        自动绑定方式Xpath
        @return:
        '''
        return "//div[contains(text(),'自动绑定')]"

    def manualBindMethodXpath(self):
        '''
        手动绑定方式Xpath
        @return:
        '''
        return "//div[contains(text(),'手动绑定')]"

    def purchaseSumXpath(self):
        '''
        购买数量Xpath
        @return:
        '''
        return "//input"

    def purchaseButtonXpath(self):
        '''
        立即购买button的Xpath
        @return:
        '''
        return "//span[text()='立即购买']"

    def purchaseSumMoneyXpath(self):
        '''
        购买总额Xpath
        @return:
        '''
        return "//div[text()='应付总额：']/following-sibling::div"

    def submitOrderButtonXpath(self):
        '''
        提交订单按钮Xpath
        @return:
        '''
        return "//button"

    def confirmPaymentButtonXpath(self):
        '''
        确认支付按钮
        @return:
        '''
        return "//button"

    def paySuccessIdentificationXpath(self):
        '''
        支付成功标识Xpath
        @return:
        '''
        return "//div[text()='订单支付成功']"
