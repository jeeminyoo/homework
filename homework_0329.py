#지니 뮤직 스크래핑
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#############################
music_info = soup.select('table.list-wrap>tbody>tr')
rank = 0
for music in music_info:
    print("*"*60)
    song_info = music.select('a')
    rank += 1
    title = song_info[2].text
    artist = song_info[3].text
    print(rank,str.strip(title),'/',artist)
