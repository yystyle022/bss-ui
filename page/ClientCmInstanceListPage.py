# -*- coding=utf-8 -*-
# @Time : 2023/5/5 9:23
# @Author : yangyang
# @File : bss-ui/ClientCmInstanceListPage.py
from base.ClientCmInstanceListBase import ClientCmInstanceList

class ClientCmInstanceListPage:

    def get_AS(self,instance):
        '''
        获取实例AK
        @return:
        '''
        return ClientCmInstanceList().listAsXpath(instance).text