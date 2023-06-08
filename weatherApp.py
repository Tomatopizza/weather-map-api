import requests
import googlemaps # pip install googlemaps
import json
from dotenv import load_dotenv
import os
load_dotenv()
weather_key = os.environ.get('WEATHER_KEY')
google_key = os.environ.get('GOOGLE_API_KEY')

url ='http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst' # https로 하니깐 sslv3 alert illegal parameter 오류 발생

para={'ServiceKey':weather_key, 'pageNo':1,'numOfRows':'1000','dataType': 'JSON', 'base_date':'20230608','base_time':'1900','nx':'55','ny':'127'}
res = requests.get(url, params=para)

res_json = json.loads(res.content)
items=res_json['response']['body']['items']['item']
for i in items:
    print(i)

# json.decoder.JSONDecodeError는 인코딩 키가 아니라 디코딩 키를 이용하면 된다!
####################################################

url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={google_key}'
data = {
    'considerIp': True, # 현 IP로 데이터 추출
}

result = requests.post(url, data) # 해당 API에 요청을 보내며 데이터를 추출한다.

print(result.text)
result2 = json.loads(result.text)

lat = result2["location"]["lat"] # 현재 위치의 위도 추출
lng = result2["location"]["lng"] # 현재 위치의 경도 추출

gmaps = googlemaps.Client(google_key)
reverse_geocode_result = gmaps.reverse_geocode((lat, lng),language='ko')
# 좌표값을 이용해 목적지를 알아내는 코드

print(reverse_geocode_result)
