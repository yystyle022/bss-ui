class ManagementNewAddApplicationBase:
    def commonModelXpath(self):
        '''
        通用模式选项
        @return:
        '''
        return "//div[text()='通用模式']"

    def newPurchaseSelectionBoxXpath(self):
        '''
        新购选择框
        @return:
        '''
        return "//span[contains(text(),'新购')]"

    def expandNumberSelectionBoxXpath(self):
        '''
        扩容点选框
        @return:
        '''
        return "//span[contains(text(),'扩容')]"

    def renewSelectionBoxXpath(self):
        '''
        续费点选框
        @return:
        '''
        return "//span[contains(text(),'续费')]"

    def customerNumberInputXpath(self):
        '''
        客户编号输入框
        @return:
        '''
        return "//label[@title='客户编号']/../following-sibling::div"

    def serviceProductInputXpath(self):
        '''
        服务产品输入框
        @return:
        '''
        return "//label[@title='服务产品']/../following-sibling::div"

    def liQingServiceProductSelectionXpath(self):
        '''
        厘清服务产品
        @return:
        '''
        return "//li[contains(text(),'厘清')]"

    def xingCanServiceProductSelectionXpath(self):
        '''
        星璨服务产品
        @return:
        '''
        return "//li[contains(text(),'星璨')]"

    def fenMingServiceProductSelectionXpath(self):
        '''
        分明服务产品
        @return:
        '''
        return "//li[contains(text(),'分明')]"

    def testActivationTrueXpath(self):
        '''
        测试激活：是
        @return:
        '''
        return "//span[contains(text(),'是')]/preceding-sibling::span"

    def testActivationFalseXpath(self):
        '''
        测试激活：否
        @return:
        '''
        return "//span[contains(text(),'否')]/preceding-sibling::span"

    def testActivationTimeInputXpath(self):
        '''
        测试激活时长输入框
        @return:
        '''
        return "//label[text()='测试激活时长']/../following-sibling::div//input"

    def ntripOrSdkLinkMethodXpath(self):
        '''
        链接方式Ntrip或Sdk
        @return:
        '''
        return "//label[text()='链接方式']/..//following-sibling::div//label[1]/span"

    def ntripLinkMethodXpath(self):
        '''
        链接方式Ntrip
        @return:
        '''
        return "//label[text()='链接方式']/..//following-sibling::div//label[2]/span"

    def sdkLinkMethodXpath(self):
        '''
        链接方式sdk
        @return:
        '''
        return "//label[text()='链接方式']/..//following-sibling::div//label[3]/span"

    def autoActivationXpath(self):
        '''
        自动激活
        @return:
        '''
        return "//span[contains(text(),'自动激活')]"

    def manualActivationXpath(self):
        '''
        手动激活
        @return:
        '''
        return "//span[contains(text(),'手动激活')]"

    def autoBindXpath(self):
        '''
        自动绑定
        @return:
        '''
        return "//span[contains(text(),'自动绑定')]"

    def manualBindXpath(self):
        '''
        手动绑定
        @return:
        '''
        return "//span[contains(text(),'手动绑定')]"

    def purchaseNumberInputXpath(self):
        '''
        购买数量输入框
        @return:
        '''
        return "//label[text()='购买数量']/../following-sibling::div"

    def purchaseTimeInputXpath(self):
        '''
        购买时长
        @return:
        '''
        return "//label[text()='购买时长']/../following-sibling::div"

    def yearPurchaseTimeXpath(self):
        '''
        购买时长单位：年
        @return:
        '''
        return "//li[contains(text(),'年')]"

    def monthPurchaseTimeXpath(self):
        '''
        购买时长：月
        @return:
        '''
        return "//li[contains(text(),'月')]"

    def dayPurchaseTimeXpath(self):
        '''
        购买时长：天
        @return:
        '''
        return "//li[contains(text(),'天')]"

    def purchasePriceInputXpath(self):
        '''
        购买价格输入框
        @return:
        '''
        return "//label[text()='购买价格']/../following-sibling::div"

    def offlineContractTimeInputXpath(self):
        '''
        线下合同时间输入框
        @return:
        '''
        return "//label[text()='线下合同时间']/../following-sibling::div"

    def todayOfflineContractTimeXpath(self):
        '''
        线下合同时间：今天
        @return:
        '''
        return "//a[text()='今天']"
