import urllib.request
from bs4 import BeautifulSoup

#웹페이지의 소스를 가져온다.
url = "https://maplestory.nexon.com/Ranking/World/Total?page=1"
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()

# 첫 페이지
for i in range(1,4):
    #소스에서 img_area 클래스 하위의 소스를 가져온다.
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find("tr",class_ = "rank0"+str(i))
    soup = soup.find("span",class_ = "char_img")

    #이미지 경로를 받아온다.
    imgURL = soup.find("img")["src"]

    urllib.request.urlretrieve(imgURL,str(i)+'rank.jpg')
    print(imgURL)
    
for j in range(4,11):
    #소스에서 img_area 클래스 하위의 소스를 가져온다.
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.select("div.rank_table_wrap > table > tbody > tr:nth-child("+str(j)+") > td.left > span > img:nth-child(1)")

    urllib.request.urlretrieve(soup[0]['src'],str(j)+'rank.jpg')
    print(imgURL)



# 그 이후 페이지
for i in range(2,11):
    # 페이지마다 url이 다르니까 요렇게
    url = "https://maplestory.nexon.com/Ranking/World/Total?page=" + str(i)
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()
    for j in range(1,11):
        soup = BeautifulSoup(source, 'html.parser')
        soup = soup.select("div.rank_table_wrap > table > tbody > tr:nth-child("+str(j)+") > td.left > span > img:nth-child(1)")

        urllib.request.urlretrieve(soup[0]['src'],str(j+(i-1)*10)+'rank.jpg')
        print(imgURL)    
    

    

