# 1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("userverify").submit()

# 2. 商品管理
driver.find_element_by_link_text("商品管理").click()
# 3.添加商品
driver.find_element_by_link_text("添加商品").click()

# 4.商品名称
# 有一种特殊的网页, 比如左边或者上边有一个导航条.这时就要注意了
# 开发很喜欢在一个页面中嵌套多个页面
# 其中"商品管理"和"添加商品"属于页面根节点的网页
# 商品名称属于frame框架里的子网页
# 之前讲过窗口切换, 用于不同网页之间的页面切换,
# 现在也是需要切花网页
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphone x")
# 5.商品分类
driver.find_element_by_xpath('//*[@id="1"]').click()
# driver.find_element_by_css_selector("#2")
driver.find_element_by_css_selector("[id='2']").click()
driver.find_element_by_id("6").click()
# driver.find_element_by_id("7").click()
# 双击是特殊的元素操作, 所有的特殊操作被封装到ActionChains这个类中
# java封装到Actions这个类中
# 链表必须以perform方法作为结尾
# 可以用来执行一组操作, 只要最后以perform()结束就可以了
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
# 6.商品品牌
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_index(1)

# 7.点击商品图册
driver.find_element_by_link_text("商品图册").click()
# 有些页面控件是javascript在页面加载之后生成的,
# implicitily_wait是用来判断整个网页是否加载完毕
# 有时页面加载完, 但是javascript的控件还没有创建好,
# 所以需要time.sleep()提高程序的稳定性
time.sleep(2)
# driver.find_element_by_css_selector("#filePicker label").click()
# 因为真正负责上传文件的页面元素是<input type="file"...
# 所以我们可以直接操作这个控件
# 这个控件可以直接输入图片的路径
driver.find_element_by_name("file").send_keys("D:/uploader.png")

# 页面太长, 点击不了下面的button, 怎么操作滚动条
# range是区间, 默认从0开始, 到(长度-1)结束,  range(10)表示0到9, 一共10个数字
ac = ActionChains(driver)
for i in range(10):
    ac.send_keys(Keys.ARROW_RIGHT)
ac.perform()

# 点击开始上传, 同时用三个class 定位
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
# alert这个控件不是直接弹出来的,需要时间等待
time.sleep(3)
driver.switch_to.alert.accept()



# 7.提交
driver.find_element_by_class_name("button_search").click()
