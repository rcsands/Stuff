import requests
import sys
import webbrowser
import random

ct = 0
bufsize = 1
low = int(sys.argv[1])
high = int(sys.argv[2])
with open('/Users/charlessands/Desktop/epic' + str(high) + '.txt', 'w', bufsize) as f:
	for x in range(low,high):
		#y =  random.randint(low, high)
		#URL = 'http://www.propertydeal.us/' + '%0*d'%(6,y)
		URL = 'http://forsalebyowners.house/' + '%0*d'%(6,x)
		#print(URL)
		try:
			r = requests.get(URL, timeout=2.0)
			#print r.status_code
		except:
			continue
		
		ct = ct + 1
		if r.status_code == 200 and 'Mercedes' in r.text:
				#print(URL)
				#webbrowser.open(URL)
				f.write(URL + '\n')
				
		if ct%10==0 and ct!=0:
					print(ct)
		# else:
		# 	if ct%10==0 and ct!=0:
		# 		print(ct)
		# 		continue

