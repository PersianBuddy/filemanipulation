import os, shelve

current_directory = os.path.curdir
########### saving data using shelve ###########
mydata = shelve.open('mydata')
user_name = ['Shahin', 26, 'programmer']
mydata['user'] = user_name
print(mydata['user'])
mydata.close()