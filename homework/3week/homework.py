import requests
from bs4 import BeautifulSoup

# lstrip : left 방향의 white space 제거
# retrip : right 방향의 white space 제거

def genie_music():
    url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200328'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    musics = soup.select('.music-list-wrap .list-wrap > tbody > tr')
    rank = 1
    for music in musics:
        title_tag = music.select_one('.info > .title')
        title = title_tag.text.lstrip()

        artist_tag = music.select_one('.info > .artist')
        artist = artist_tag.text

        print(rank, '', title, '', artist)
        rank +=1


if __name__ == '__main__':
    genie_music()
    
# if __name__ == '__main__' 의미 -> 해당 파일이 실행될 때 (이 문구는 외우기)