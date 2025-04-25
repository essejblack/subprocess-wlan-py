import subprocess

data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wlan=[i.split(':')[1][1:-1] for i in data if 'All User Profile' in i]
wifi=[]
for name in wlan:
    data=subprocess.check_output(['netsh','wlan','show','profile',name,'key=clear']).decode('utf-8').split('\n')
    password=[i.split(':')[1][1:-1] for i in data if 'Key Content' in i]
    wifi.append({'ssid':name,'password':password[0] if password else None})
print(wifi)