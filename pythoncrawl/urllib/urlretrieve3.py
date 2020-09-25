# urlretrieve : 요청하는 url의 정보를 로컬 파일로 저장
#               cvs 파일, api 데이터 등 많은 양의 데이터를 한꺼번에 저장할 때 사용
# 좋아하는 연예인 사진 저장하기
import urllib.request as req
# 요청 url
img_url1 ="https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5648%2F2020%2F07%2F07%2F0000014799_001_20200707154035606.jpg&type=sc960_832"
img_url2 ="https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F005%2F2020%2F02%2F24%2F611811110014273837_1_20200224093502379.jpg&type=sc960_832"
# 로컬 파일
save_img1 = "d:/wooni1.png"
save_img2 = "d:/wooni2.png"
try:
    file1, header1 = req.urlretrieve(img_url1, save_img1)
    file2, header2 = req.urlretrieve(img_url2, save_img2)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("성공")
