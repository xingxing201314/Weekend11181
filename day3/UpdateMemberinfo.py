# 1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("changcheng")
# Chains链表和数组不同,数组有固定锝长度, 链表必须有明确锝结束标志
ActionChains(driver).send_keys(Keys.TAB).send_keys("123654").send_keys(Keys.ENTER).perform()
# 2.点击账号设置
driver.find_element_by_link_text("账号设置").click()
# 3.点击个人资料
driver.find_element_by_partial_link_text("个人资料").click()
# 4.修改个人信息'
# clear是清空的意思.用来清空元素中原本的内容
# 更好的编程习惯是, 在每次执行sendkeys之前, 都进行一遍 clear操作.
# 4a.真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("万里")
# 4b.性别
# css可以用多个属性组合定位一个元素
# 一个元素的多个属性之前不能有空格
driver.find_element_by_css_selector('#xb[value="2"]').click()
# javascript是一个单独语言, 和python的语法不一样, 不能直接在pycharm中执行
# js = 'document.getElementById("date").removeAttribute("readonly")'
# driver.execute_script(js)
# driver.find_element_by_id("date").clear()
# driver.find_element_by_id("date").send_keys("2001-11-21")
# 用arguments改写上面输入: 用selenium的定位方式,定位元素之后,对元素执行javascript脚本,删除readonly属性
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")', date)
date.clear()
date.send_keys("1980-11-21")
# 用selenium调用javascript 一共有两个关键字:
# 1.arguments[0]: 表示用python语言代替一部分javascript
# 好处是, 有时, selenium定位比较容易
# 2. return 把javascript的执行结果返回给python语言
# 好处是, 有时, selenium定位不到的元素, 我们可以用javascript定位到

# date = driver.execute_script("return document.getElementById('date')")
# 这句话等于   date = driver.find_element_by_id("date")
# date.click()
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("4564565852")
driver.find_element_by_class_name("btn4").click()
# 右键检查不了html代码的弹出框,叫做alert, 有单独的方法来处理
time.sleep(3)
#alert控件不是html代码生成的, 所以implicitly_wait对这个控件不管用
# 所以就算上面写了implicitly_wait, 这个time.sleep()方法不能胜率
# 切换到alert的方法, 和切换窗的方法类似
# alert 弹出框, accept 接受, 同意, 确定, dismiss 拒绝, 取消
driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

# 页面太长, 点击不了下面的button, 怎么操作滚动条
# range是区间, 默认从0开始, 到(长度-1)结束,  range(10)表示0到9, 一共10个数字
# ac = ActionChains(driver)
# for i in range(10):
#     ac.send_keys(Keys.ARROW_DOWN)
# ac.perform()

driver.execute_script("window.scrollTo(400,700)")










