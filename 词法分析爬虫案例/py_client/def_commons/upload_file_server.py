#encoding:UTF-8
# chenzy python
import requests,time,json

# 泪历(请看官网)：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
# 图片上传到服务器
def upload_post_img(serverUrl,imgPath):
    try:
        boundary = '----------%s' % hex(int(time.time() * 1000))
        files = {
            'file': ('w.png', open(imgPath, 'rb'), 
                    'Content-Type: multipart/form-data; boundary=%s' % boundary )
            }
        responseData = requests.post(serverUrl, files=files)
        # {"imageUrls":["2018/7/20/566ef43ce7794b559528e159851ae249.png"],"result":{"resultCode":1,"resultMsg":"success"}}
        jsonData = json.loads(responseData.text)
        imageUrls = jsonData['imageUrls'][0]
    except Exception as e:
        print("——》  图片上传服务器异常：",e)
        return False
    print("——》  图片上传服务器成功，返回路径：",imageUrls)
    return imageUrls

# test
# upload_post_img("url","F:\codePython\czy-study-python\sanya_house_py\py_client\img\img20180720100033.png")