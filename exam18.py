import datetime, time

now = datetime.datetime.now()

# {} format
'''
print(" {}년 {}월 {}일 {}시:{}분:{}초"\
      .format(now.year,now.month,now.day,now.hour,now.minute,now.second))
'''

'''
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
'''

'''
s = now.strftime('%Y-%m-%d %H:%M:%S')
print(s)

timestamp = time.time()
s = str(timestamp)
print(s)
'''

if now.hour < 12:
  print("현재 시각은 {}시로 오전입니다.!".format(now.hour))
else:
  print("현재 시각은 {}시로 오후입니다.!".format(now.hour))


s = '2017-03-26 12:12:12'
dt = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')  
print(dt, type(dt))
timestamp = time.mktime(datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S').timetuple())
print(timestamp)