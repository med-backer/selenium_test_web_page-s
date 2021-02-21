class BasePage():
    def __init__(self,browser,url):
        self.browser=browser
        self.url=browser
    def open(self):
        self.browser.get(self.url)
