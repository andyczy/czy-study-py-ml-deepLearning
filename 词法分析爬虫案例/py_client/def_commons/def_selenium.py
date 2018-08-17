#encoding:UTF-8
# chenzy python
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from def_commons import def_path
import time

# Windows 两个函数都可以用
def getScreenshot(url,fileName):
    # path = def_path.init_mkdir(paths)  #创建目录
    driver = webdriver.Firefox()
    driver.get(url)
    # driver.set_window_position(x=50,y=60)
    # driver.set_window_size(width=50, height=50)
    # driver.save_screenshot(paths+"\\"+fileName+".png") # 返回值：true
    driver.quit()
    # pathStr = paths+"\\"+fileName+".png"
    # return pathStr

# linux
def getScreenshotLinux(paths,url,fileName):
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("——》  开始截图：",nowTime)

    # 配置属性--解决速度慢的问题
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.startup.homepage", "about:blank")
    profile.set_preference("startup.homepage_welcome_url", "about:blank")
    profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")
    profile.set_preference('permissions.default.image', 3)    #1 允许所有图片；2 阻止所有图片；3 阻止第三方服务器图片
    profile.set_preference('browser.migration.version', 9001) #部分需要加上这个
    profile.assume_untrusted_cert_issuer =True

    # 配置属性--解决在Linux上运行问题（有这个就不用打开远程打开浏览器）
    options = FirefoxOptions()
    options.add_argument("--headless")
    try:
        # 获取火狐浏览器驱动
        browser = webdriver.Firefox(firefox_options=options,firefox_profile=profile)
        # 设定页面加载限制时间
        # browser.set_page_load_timeout(50)

        # print("——》  程序睡眠2秒钟！")
        # time.sleep(2)

        # 当前页面大小：
        jsonWidthAndHeigth = browser.get_window_size()
        width = jsonWidthAndHeigth['width']
        browser.set_window_size(width=width-50, height=width*1.5)
        print("——》  当前截取页面大小：[宽度：",width,",高度：",width*1.5 ,"]")

        # 获取网页信息
        browser.get(url)
        # 创建目录   
        path = def_path.init_mkdir(paths+"/img")  
        imgPath = path+"/"+fileName+".png"
        success = browser.save_screenshot(imgPath) # 返回值：true

        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    except Exception as e:
        print("——》  截图异常信息：",nowTime, e)
        return False
    if success == True:
        print("——》  截图成功！",nowTime)
    else:
        print("——》  截图失败！",nowTime)
    return imgPath


# test
# print(getScreenshotLinux("F:\codePython","http://www.home898.com/zixun/1800256213.html","11111"))