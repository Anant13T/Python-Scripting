import time

#no of seconds passed from the 1st januray 2022
a=time.time()
print(a)
#formatting the 'a' 
localtime=time.localtime(a)
print(localtime)
#to extract a particular value
print(localtime.tm_year)
#to display the 'a' information in a more formatted way we use the ctime
print(time.ctime(a))