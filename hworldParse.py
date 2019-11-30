import time
print("init parser")

#remember filepath runs from root directory of Python? or OS?
#defintely python in our case 
filepath = 'yoScripts/twocities.txt'

#note in below that we need to specify encoding or else it fails with charmap error
with open(filepath, encoding="utf-8") as fp:
	line = fp.readline()
	numwords = 0
	cnt = 1
	while line:
		print("Line {}: {}".format(cnt, line.strip()))
		time.sleep(.125)
		line = fp.readline()
		cnt += 1
		