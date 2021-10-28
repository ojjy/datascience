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
        url = "http://apis.data.go.kr/B551182/yadmOpCloInfoService/getHospPharmacyOpCloList?crtrYm={}&yadmTp=0&opCloTp=0&_type=json&serviceKey={}".format(month_before,coninfo['servicekey_p'])
        json_data = json.loads(requests.get(url).text)
        totalCount = json_data['response']['body']['totalCount']
        maxpageno = math.ceil(totalCount/numOfRows)
        # print(f"month_before: {month_before}, totalCount: {totalCount}, maxpageno: {maxpageno}")
        with conn.cursor() as cur:
            # cur.execute(f"TRUNCATE TABLE {table_name}")
            for pageno in range(1, maxpageno+1):
                url = "http://apis.data.go.kr/B551182/yadmOpCloInfoService/getHospPharmacyOpCloList?pageNo={}&crtrYm={}&yadmTp=0&opCloTp=0&_type=json&serviceKey={}".format(pageno, month_before, coninfo['servicekey_p'])
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
                    value = "("+"'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(addr, clCdNm, cnclDd, crtrYm, estbCnclTp, estbDd, shwSbjtCdNm, telno, yadmNm, ykiho, REGT_ID, REG_DTTM)+")"
                    print(value)
                    sql = "INSERT INTO {} VALUES {}".format(table_name, value)
                    with conn.cursor() as cur:
                        print(sql)
                        cur.execute(sql)
                    conn.commit()

def main():
    table_name = os.path.basename(__file__).replace(".py", "")+"_test"
    print(table_name, "START")
    HospPharmacyOpCloList(table_name)
    print(table_name)
    print(table_name, "END")

if __name__ == "__main__":
    main()