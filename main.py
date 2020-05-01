import os, shelve, pprint

current_directory = os.path.curdir
########### saving data using shelve ###########
# mydata = shelve.open('mydata')
# user_name = ['Shahin', 26, 'programmer']
# mydata['user'] = user_name
# print(mydata['user'])
# mydata.close()

############ saving data using puthon file ##########
about_me = [{'hobby': ['programming', 'gaming', 'watching movie'], 'age':26}]
about_me_string = pprint.pformat(about_me)
shahin_file = open('shahin.py','w')
shahin_file.write('about_me = '+ about_me_string)
shahin_file.close()
import shahin
print(shahin.about_me)
