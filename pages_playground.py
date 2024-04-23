class BasePage:

    def find_el(self):
        print('Finding element')


    def click(self):
        print('Clicking')

    def verify_text(self, expected_text):
        print(f'Checking for {expected_text}')


class LoginPage(BasePage):
    def __init__(self):
        self.default_pw = 'Password'


    def login(self, email, pw):
        print('login...')

    def verfiy_TC(self):
        self.verify_text('TC text')


class RegPage(BasePage):

    def register(self):
        print('Registering...')

login_page = LoginPage()
reg_page = RegPage()
login_page.click()
#login_page.login()

print(login_page.default_pw)











