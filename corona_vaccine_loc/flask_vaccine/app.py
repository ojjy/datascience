from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
from folium import Map, Marker, Icon, Figure
from folium.plugins import MarkerCluster
import folium
import requests
import json
# 유성구에서 에러 확인 필요
app = Flask(__name__)

def getLatLng(addr):
    print("getLatLng function call")
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK 9689cf5d703ad53dba79703ad0ebc485"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    print(requests.get(url, headers=headers))
    print(result)
    match_first = result['documents'][0]['address']
    lon = match_first['x']
    lat = match_first['y']
    print(lon, lat)
    print(match_first)

    return lon, lat

@app.route('/index')
def base():
    map = folium.Map(
        location=[36.5053542, 127.7043419]
    )
    addr_lon, addr_lat = getLatLng("대전광역시 유성구 유성대로 976")
    return map._repr_html_()

@app.route('/')
def hello_world():
    # db연결
    dbcon = create_engine("mysql+pymysql://test:test@127.0.0.1/testdb")
    # df = pd.read_csv("vacloc.csv")
    df = pd.read_csv("vacloc_20210315.csv")
    # dataframe내 데이터를 db에 넣는다 테이블이 없으면 생성하고 테이블과 데이터가 있으면 삭제하고 다시 생성
    df.to_sql(name='vaccine_loc', con=dbcon, if_exists='replace')
    # row갯수 만큼 for문을 돌아서 row들의 데이터를 각각 저장한다 iterrows()

    figure = Figure()
    m = Map(location=[36.5053542, 127.7043419], zoom_start=8)
    m.add_to(figure)

    print(df)
    for idx in range(len(df)):
        print(df.loc[idx, "시설명"], df.loc[idx, "주소"])
        location_name = df.loc[idx, "시설명"]
        addr = df.loc[idx, "주소"]
        addr_lon, addr_lat = getLatLng(addr)
    # 데이터내 주소를 지도에 찍는다
        Marker(location=[addr_lat, addr_lon], popup="<b>"+location_name+"</b>", icon=Icon(color='green', icon='flag')).add_to(m)
    figure.render()
    return m._repr_html_()

if __name__ == '__main__':

    app.run()


# References
# https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/