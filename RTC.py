
def RTC():
	import datetime as dt
	string = str(dt.datetime.now())
	Today= dt.datetime.strptime(string,"%Y-%m-%d %H:%M:%S.%f")
	return Today
if __name__ == "__main__":
	input('welcome\n')
	print(RTC().date())
	print(RTC().time())
	print('The current hour is',RTC().hour)
	print('The current minute is',RTC().minute)
	print('The current date is',RTC().day)
	print('The current month is',RTC().month)
	print('The current year is',RTC().year)
	print('The current sec is', RTC().second)
	print('The current milisec is', RTC().microsecond/1000)
