import requests
import os
from twilio.rest import Client

API_key=  os.environ.get('API_KEY')
lat = -1.292066
lon = 36.821945
part = "hourly,daily"
TWILIO_ACCOUNT_SID= os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

parameter = {
    'lat':11.825138,
    'lon':36.821945,
    'part': 'weekly,daily,minute,current',

}
response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={parameter['lat']}&lon={parameter['lon']}&exclude={parameter['part']}&appid={API_key}")
response.raise_for_status()
dat = response.json()


t = dat['hourly']
# print(t[0]['weather'][0]["id"])
twelve_hrs = slice(0,12)
v= t[twelve_hrs]
# print(v[0])
weather_code = []

for x in range(0,11):
  # print(v[x]['weather'][0]["id"])
  weather_code.append(v[x]['weather'][0]["id"])
print(weather_code)

def wil_rain():

    for x in weather_code:
        if x < 700:
            return True
if wil_rain():
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain ⛈ today. Please remember to bring an ☂",
        from_='+13203387380',
        to='+254717143790'
    )

    print(message.status)



#
# daily = []
# for x in range(0,12):
#     daily+=(t[x]['weather'])
#
# weather = []
# def if_might_rain():
#     for x in range(0,12):
#         weather.append(daily[x]['id'])
#         if weather[x] < 700:
#             return True
#         break
#
# if if_might_rain():
#     print("Please Bring an umbrella")
#     account_sid = "ACf52a092602490fcd210e96d7190fe39d"
#     auth_token = "fab84f7d55d29edbc0a00a851750bfd1"
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#         body="It will rain ⛈ today. Please remember to bring an ☂",
#         from_='+13203387380',
#         to='+254717143790'
#     )
#
#     print(message.status)
# else:
#     print("It wont rain")
#
