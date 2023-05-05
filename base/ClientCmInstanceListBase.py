# -*- coding=utf-8 -*-
# @Time : 2023/5/5 9:27
# @Author : yangyang
# @File : bss-ui/ClientCmInstanceListBase.py
class ClientCmInstanceList:

    def listExpandButtonXpath(self,instance):
        '''
        返回实例列表展开按钮的Xpath
        @param instance:
        @return:
        '''
        return "//td[text()='{}']/..//span[@class='expand-icon']".format(instance)

    def listAsXpath(self,instance):
        '''
        返回列表实例AS的Xpath
        @param instance:
        @return:
        '''
        return "//td[text()='{}']/../following-sibling::tr[1]//span[contains(text(),'AppSecret')]/following-sibling::span".format(instance)

