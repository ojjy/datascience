"""
개발자: 조예진
개발일: 210830
함수명: HospPharmacyOpCloList
테이블명: Medinst_HospPharmacyOpCloList
설명: 병원약국개폐업목록_요양기관개폐업정보조회서비스_건강보험심사평가원_공공데이터포털
기준년월 등을 통해 기준년월에 개업 또는 폐업한 병원과 약국의 요양기관명, 개폐업구분, 전화번호, 주소 등을 조회하는 병원과 약국의 개폐업 목록조회
URL: https://www.data.go.kr/data/15051043/openapi.do

{'addr': 86, 'clCdNm': 4, 'cnclDd': 8, 'crtrYm': 6, 'estbCnclTp': 2, 'estbDd': 8, 'shwSbjtCdNm': 12, 'telno': 13, 'yadmNm': 24, 'ykiho': 80, 'REGT_ID': 7, 'REG_DTTM': 19}
Medinst_HospPharmacyOpCloList테이블 row총갯수: 880개, 테이블용량:240.0KB, 테이블설명: 병원약국개폐업목록_요양기관개폐업정보조회서비스_건강보험심사평가원_공공데이터포털
Medinst_HospPharmacyOpCloList 실행완료
"""

import requests
import json
import os
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
import snowflake.connector


def nullify(str):
    if str == None:
        return ""
    else:
        return str


def HospPharmacyOpCloList(table_name):
    """
    API를 호출하여 1년 전까지의 년월 값을 파라미터로 넣어 데이터를 얻고 얻은 데이터를 바탕으로 SQL에 넣는다.
    :param table_name:
    :return:
    """

    for month in range(15, -1, -1):
        # print(month)
        current_date=datetime.now().strftime('%Y-%m-%d')
        month_before = (datetime.strptime(current_date, '%Y-%m-%d') - relativedelta(months=month)).strftime('%Y%m')
        numOfRows = 100
        with open("dbinfo.json") as fp:
            coninfo = json.loads(fp.read())

        conn = snowflake.connector.connect(user = coninfo["SF_USER"],
                                          password = coninfo["SF_PWD"],
                                          account = coninfo["SF_ACCOUNT"],
                                          schema = coninfo["SF_SCHEMA"],
                                          warehouse = coninfo["SF_WH"],
                                          database = coninfo["SF_DB"])
        url = f"http://apis.data.go.kr/B551182/yadmOpCloInfoService/getHospPharmacyOpCloList?crtrYm={month_before}&yadmTp=0&opCloTp=0&_type=json&serviceKey={coninfo['servicekey_p']}"
        json_data = json.loads(requests.get(url).text)
        totalCount = json_data['response']['body']['totalCount']
        maxpageno = math.ceil(totalCount/numOfRows)
        print(f"month_before: {month_before}, totalCount: {totalCount}, maxpageno: {maxpageno}")
        with conn.cursor() as cur:
            cur.execute(f"TRUNCATE TABLE {table_name}")
            for pageno in range(1, maxpageno+1):
                url = f"http://apis.data.go.kr/B551182/yadmOpCloInfoService/getHospPharmacyOpCloList?pageNo={pageno}&crtrYm={month_before}&yadmTp=0&opCloTp=0&_type=json&serviceKey={coninfo['servicekey_p']}"
                print(url)
                res = requests.get(url).text
                json_data = json.loads(res)
                items = json_data['response']['body']['items']['item']
                for idx, item in enumerate(items):
                    addr = nullify(item.get('addr'))
                    clCdNm = nullify(item.get('clCdNm'))
                    cnclDd = nullify(item.get('cnclDd'))
                    crtrYm = nullify(item.get('crtrYm'))
                    estbCnclTp = nullify(item.get('estbCnclTp'))
                    estbDd = nullify(item.get('estbDd'))
                    shwSbjtCdNm = nullify(item.get('shwSbjtCdNm'))
                    telno = nullify(item.get('telno'))
                    yadmNm = nullify(item.get('yadmNm'))
                    ykiho = nullify(item.get('ykiho'))
                    REGT_ID = "yejinjo"
                    REG_DTTM = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    value = f"{addr, clCdNm, cnclDd, crtrYm, estbCnclTp, estbDd, shwSbjtCdNm, telno, yadmNm, ykiho, REGT_ID, REG_DTTM}"
                    print(value)
                    sql = f"INSERT INTO {table_name} VALUES {value}"
                    with conn.cursor() as cur:
                        print(sql)
                        cur.execute(sql)
                    conn.commit()

def main():
    table_name = os.path.basename(__file__).replace(".py", "")
    print(table_name, "실행시작")
    HospPharmacyOpCloList(table_name)
    print(table_name)
    print(table_name, "실행완료")

if __name__ == "__main__":
    main()