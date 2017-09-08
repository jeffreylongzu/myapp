#!/usr/bin/python
#--*--coding:utf-8--*--
import glob,datetime
#for x,y,z in os.walk("/opt/Manauto/data/db"):


#	print x,y,z
ss = glob.glob('/opt/Manauto/data/db/*')
T = []
for TX in range(10):
	TN = datetime.datetime.now()
	TD = TN - datetime.timedelta(days=TX)
	FX = TD.strftime("%Y%m%d")
	for sss in ss:
		if sss.find(FX) != -1 and not sss.find("OA") != -1:
			T.append(sss)
T.sort()
for x in T:
	print x
