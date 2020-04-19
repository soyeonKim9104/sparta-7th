import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

host = 'http://openapi.airport.co.kr/service'
serviceKey = 'y7pMhOU8g9nUPMZeare2UibAJZm453CLckGI9xub5arSby6dFF6TjctFdkaC4PwVlzHN%2B1NRquo8o0%2Fdzo2L%2FA%3D%3D'

#나라 명
def get_air_code():
    for i in range(10):
        url = '{}/rest/AirportCodeList/getAirportCodeList?ServiceKey={}&pageNo={}'.format(host, serviceKey, i + 1)
        headers = {
            'Content-Type': 'application/xml'
        }
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        citycode = soup.select("item")

        for city in citycode:
            citynamekor = city.select_one('item > citykor').text
            cityCode = city.select_one('item > cityCode').text
            
            if citynamekor is not None and cityCode is not None:
                doc = {
                    'citynamekor': citynamekor,
                    'cityCode': cityCode
                }
                db.citycode.insert_one(doc)


#국내선 운항 스케줄 
def get_air_d_flight():
    url = '{}/rest/FlightScheduleList/getDflightScheduleList?ServiceKey={}&pageNo={}'.format(host, serviceKey, 1)
    headers = {
        'Content-Type': 'application/xml'
    }
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    flightdomestic = soup.select("item")

    for domestic in flightdomestic:
        #출발공항
        startcity = domestic.select_one('item > startcity').text
        #출발시간
        domesticStartTime = domestic.select_one('item > domesticStartTime').text
        #도착공항
        arrivalcity = domestic.select_one('item > arrivalcity').text
        #도착시간
        domesticArrivalTime = domestic.select_one('item > domesticArrivalTime').text
        #항공사(국문)
        airlineKorean = domestic.select_one('item > airlineKorean').text

        print(startcity,domesticStartTime,arrivalcity,domesticArrivalTime,airlineKorean)

        if startcity is not None and domesticStartTime is not None and arrivalcity is not None and domesticArrivalTime is not None and airlineKorean:
            doc = {
                'startcity' : startcity,
                'domesticStartTime' : domesticStartTime,
                'arrivalcity' : arrivalcity,
                'domesticArrivalTime' : domesticArrivalTime,
                'airlineKorean' : airlineKorean
            }

            db.flightdomestic.insert_one(doc)
    

def get_air_i_flight():
    url = '{}/rest/FlightScheduleList/getIflightScheduleList?ServiceKey={}&pageNo={}'.format(host, serviceKey, 1)
    headers = {
        'Content-Type': 'application/xml'
    }
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    flightinternational = soup.select("item")

    for inter in flightinternational:
    #기준공항
    airport = inter.select_one('item > airport').text
    #운항구간
    city = inter.select_one('item > city').text
    #출/입국코드
    internationalIoType = inter.select_one('item > internationalIoType').text

if __name__ == '__main__':
    get_air_d_flight()
