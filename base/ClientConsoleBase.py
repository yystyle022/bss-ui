class ClientConsoleBase():

    def buyNumCmXpath(self):
        '''
        厘米级总服务账号个数Xpath
        @return:
        '''
        return "//p[contains(text(),'厘米级')]/span[@class='buy-num']"

    def buyNumDmXpath(self):
        '''
        亚米级总服务账号个数Xpath
        @return:
        '''
        return "//p[contains(text(),'亚米级')]/span[@class='buy-num']"

    def purchaseCmAccountButtonXpath(self):
        '''
        购买厘米级服务账号按钮Xpath
        @return:
        '''
        return "//p[text()=' 厘米级 ']/../button"

    def purchaseDmAccountButtonXpath(self):
        '''
        购买亚米级服务账号按钮Xpath 
        @return:
        '''
        return "//p[text()=' 亚米级 ']/../button"
