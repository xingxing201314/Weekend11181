from selenium.webdriver.common.by import By
class LoginPage:

    #构造方法的作用
    #实例化LoginPage对象的时候，需要把driver作为参数传进去，方便别的属性和方法使用driver。
    def __init__(self,driver):
        self.driver = driver
    title = "用户登录 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"
    #小括号表示元祖，元祖中有两个元素，第一个元素是控件的定位方式，第二个元素是控件定位的具体值。
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    login_click = (By.CLASS_NAME,"login_btn")

    def open(self):
        self.driver.get(self.url)
    def input_username(self,username):
        #self.driver.find_element_by_id("username").send_keys("qiyuan")
       # self.driver.find_element_by_id("password").send_keys("123456")
        #星号的作用就是把一个元祖中的元素分别传入方法参数中
        #前面加一个星号，表示传入就不是元祖了。而是元祖中的两个元素。
        self.driver.find_element(*self. username_input_loc,).send_keys(username)
    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.login_click).click()





