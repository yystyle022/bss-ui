class ClientLeftNavigationBar():
    def consoleOverviewXpath(self):
        '''
        控制台概览
        @return:
        '''
        return "//span[text()='控制台概览']"

    def accountManagementXpath(self):
        '''
        服务号管理Xpath
        @return:
        '''
        return "//span[text()='服务号管理']"

    def accountCmXpath(self):
        '''
        厘米级服务Xpath
        @return:
        '''
        return "//span[text()='厘米级服务']"

    def accountCmOverviewXpath(self):
        '''
        厘米级服务概览Xpath
        @return:
        '''
        return "//span[text()='概览']"

    def accountCmInstanceXpath(self):
        '''
        厘米级服务实例Xpath
        @return:
        '''
        return "//span[text()='厘米级服务']/../../following-sibling::ul//span[text()='实例']"

    def accountCmFormalNumberXpath(self):
        '''
        厘米级服务正式账号Xpath
        @return:
        '''
        return "//span[text()='厘米级服务']/../../following-sibling::ul//span[text()='正式账号']"

    def accountCmTryNumberXpath(self):
        '''
        试用账号Xpath
        @return:
        '''
        return "//span[text()='厘米级服务']/../../following-sibling::ul//span[text()='试用账号']"
