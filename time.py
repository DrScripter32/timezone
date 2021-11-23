import time
import random
red = '\x1b[31m'
blue = '\x1b[34m'
green = '\x1b[32m'
print(blue)
print ("""
|-----------------------------|
|---------TIME-ZONE-----------|
|-----------------------------|
|--C-O-D-E---S-C-R-I-P-T-E-R--|
email : ef7hast@gmail.com
""")

print('------------------------')
time.sleep(random.randint(1 , 2))
now = time.localtime()

print (red + "    [1]", green + "year")
time.sleep(0.4)
print (red + "    [2]" , green + "mon")
time.sleep(0.4)
print (red + "    [3]" , green + "day")
time.sleep(0.4)
print (red + "    [4]" , green + "hour")
time.sleep(0.4)
print (red + "    [5]" , green + "min")
time.sleep(0.4)
print (red + "    [6]" , green + "sec")
time.sleep(0.4)
print (red + "    [7]" , green + "day year")
time.sleep(0.4)
print (red + "    [8]" , green + "all")

m = int(input("--- [ ] ---"))



if m == 1:
     print ( red + "year :" , now.tm_year )
     exit()
elif m == 2:
     print (red + "mon :" ,now.tm_mon)
     exit()
elif m == 3:
     print (red + "day :" ,now.tm_mday)
     exit()
elif m == 4:
     print(red + "hour :" ,now.tm_hour)
     exit()
elif m == 5:
     print(red + "min :" ,now.tm_min)
     exit()
elif m == 6:
     print(red + "sec :" ,now.tm_sec)
     exit()
elif m == 7:
     print(red + "day year :" ,now.tm_yday)
     exit()
elif m == 8:
          time.sleep(0.3)
          print(blue)
          time.sleep(0.3)
          print("year :" , now.tm_year)
          time.sleep(0.3)
          print("mon  :" , now.tm_mon)
          time.sleep(0.3)
          print("day  :" , now.tm_mday)
          time.sleep(0.3)
          print("hour :" ,  now.tm_hour)
          time.sleep(0.3)
          print("min  :" , now.tm_min)
          time.sleep(0.3)
          print("sec  :" , now.tm_sec)
          time.sleep(0.3)
          print("yday :" , now.tm_yday)
          print("-------------------")
          print(now.tm_year ,"/" , now.tm_mon ,"/", now.tm_mday)
          print("-------------------")
          time.sleep(0.3)
          exit()
