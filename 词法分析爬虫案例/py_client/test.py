#encoding:UTF-8
# chenzy python
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import time


print("——》  开始截图！")
# 配置属性--解决速度慢的问题
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.startup.homepage", "about:blank")
profile.set_preference("startup.homepage_welcome_url", "about:blank")
profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")
profile.set_preference('permissions.default.image', 1)    #1 允许所有图片；2 阻止所有图片；3 阻止第三方服务器图片
profile.set_preference('browser.migration.version', 9001) #部分需要加上这个
profile.assume_untrusted_cert_issuer =True

# 配置属性--解决在Linux上运行问题（有这个就不用打开远程打开浏览器）
options = FirefoxOptions()
options.add_argument("--headless")

# 获取火狐浏览器驱动
browser = webdriver.Firefox(firefox_options=options,firefox_profile=profile)
# 设定页面加载限制时间
# browser.set_page_load_timeout(30)

# 当前页面大小：
jsonWidthAndHeigth = browser.get_window_size()
width = jsonWidthAndHeigth['width']
browser.set_window_size(width=width, height=width*1.2)
print ("——》  当前截取页面大小：[宽度：",width,",高度：",width*1.2 ,"]")
# 获取网页信息
browser.get('http://www.home898.com/zixun/1800130820.html')
classname = browser.find_element_by_class_name("body_left")
imgPath = "/root/server/python/sanya_house_py/py_client/img/login.png"


browser.maximize_window()
    


# time.sleep(5)
print("——》  程序睡眠5秒钟！",classname)
# 截图--success返回值：true
success = browser.save_screenshot("login.png") 
if success == True:
    print("——》  截图成功！")
else:
    print("——》  截图失败！")
browser.close()