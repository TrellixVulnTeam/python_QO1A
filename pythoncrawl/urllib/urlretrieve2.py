# urlretrieve : 요청하는 url의 정보를 로컬 파일로 저장
#               cvs 파일, api 데이터 등 많은 양의 데이터를 한꺼번에 저장할 때 사용
import urllib.request as req

# 요청 url
img_url ="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA4MDdfMTE5%2FMDAxNTk2NzYyNTAxNzM2.RUw6zNIYhIw9RCdtTXRYafqzJhXEi8bRrGQWWHt8HT4g.iJ6k5rPOVPzzMa9HlzRaPbCl_kcgKrIQUut1PD8xJpIg.JPEG.hot0219zzang%2F7DF3C987-D4ED-4853-9089-D0D27CFE43F0-11130-000009374B04B9B8_file.jpg&type=sc960_832"
html_url = "http://google.com"
# 로컬 파일
save_html = "d:/google.html"
save_img = "d:/save1.png"

try:
    file1, header1 = req.urlretrieve(img_url, save_img)
    file2, header2 = req.urlretrieve(html_url, save_html)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("성공")
