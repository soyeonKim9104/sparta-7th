import requests

host = 'http://openapi.airport.co.kr/service'
serviceKey = 'y7pMhOU8g9nUPMZeare2UibAJZm453CLckGI9xub5arSby6dFF6TjctFdkaC4PwVlzHN%2B1NRquo8o0%2Fdzo2L%2FA%3D%3D'

def get_air_code():
    url = '{}/rest/AirportCodeList/getAirportCodeList?ServiceKey={}&pageNo={}'.format(host, serviceKey, 1)
    headers = {
        'Content-Type': 'application/xml'
    }
    res = requests.get(url, headers=headers)
    print(res.text)

def get_air_d_flight():
    url = '{}/rest/FlightScheduleList/getDflightScheduleList?ServiceKey={}&pageNo={}'.format(host, serviceKey, 1)
    headers = {
        'Content-Type': 'application/xml'
    }
    res = requests.get(url, headers=headers)
    print(res.text)

def get_air_i_flight():
    url = '{}/rest/FlightScheduleList/getIflightScheduleList?ServiceKey={}&pageNo={}'.format(host, serviceKey, 1)
    headers = {
        'Content-Type': 'application/xml'
    }
    res = requests.get(url, headers=headers)
    print(res.text)


def get_air_status_flight():
    url = '{}/rest/FlightStatusList/getFlightStatusList?ServiceKey={}&pageNo={}'.format(host, serviceKey, 1)
    headers = {
        'Content-Type': 'application/xml'
    }
    res = requests.get(url, headers=headers)
    print(res.text)

if __name__ == '__main__':
    get_air_code()
    get_air_d_flight()
    get_air_i_flight()
    get_air_status_flight()