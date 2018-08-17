#  # -*- coding: utf-8 -*-
# """
# Spyder Editor
# This is a temporary script file.
# """
# #! /usr/bin/env python3.6
# import requests
# import gzip
 

# # 案例
# def main():
#     url = 'http://127.0.0.1:801/health/index.php/mobile/test/getBanners'    
#     data = {'test': 'data'}
#     headers ={"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0",
#               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#               #"Accept-Language":"en-US,en;q=0.5",
#               "Accept-Encoding":"gzip, deflate",
#               #"Connection":"keep-alive",
#               "Content-Type":"application/x-www-form-urlencoded",
#               }
 
#     resp = requests.get(url, headers=headers, params=data) 
#     #resp = requests.post(url, data=data, headers=headers)
    
#     if resp.status_code == 200:
        
#         print('gzip data: ',resp.content)
#         data = gzip.decompress(resp.content).decode("utf-8")
#         print("ungzip data: ",data)
#     else:
#         print("error")
 
# if __name__ == '__main__':
#     main()  
