import requests

host = 'http://openapi.airport.co.kr/service'
serviceKey = 'y7pMhOU8g9nUPMZeare2UibAJZm453CLckGI9xub5arSby6dFF6TjctFdkaC4PwVlzHN%2B1NRquo8o0%2Fdzo2L%2FA%3D%3D'

def get_airlines():
    url = '{}/rest/AirportCodeList/getAirportCodeList?ServiceKey={}&pageNo={}'.format(host, serviceKey, 1)
    headers = {
        'Content-Type': 'application/xml'
    }
    res = requests.get(url, headers=headers)
    print(res.text)


if __name__ == '__main__':
    get_airlines()