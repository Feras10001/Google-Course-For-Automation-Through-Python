#!/usr/bin/env python3
import re, operator, csv, os
file = 'log.txt'

pattern = r'ticky: (INFO|ERROR): (.*) \((.*)\)'
err_dic ={}
usr = {}

with open(file) as f:
 for line in f.readlines():
  result = re.search(pattern, line)
  if result.group(1) == 'ERROR':
   error = str(result.group(2))
   usr1 = str(result.group(3))
   usr.setdefault(usr1,[0,0])[1]+=1
   if error not in err_dic:
    err_dic[error] = 1
   else:
    err_dic[error] += 1
  else:
   user = str(result.group(3))
   usr.setdefault(user,[0,0])[0]+=1
  #if user not in usr:
   #usr[user] = [0,
  #else:
   #usr[user] +=1


error_sorted = sorted(err_dic.items(), key = operator.itemgetter(1), reverse = True)
user_sorted = sorted(usr.items())
print (error_sorted)
print (user_sorted)

with open('error_message.csv','w') as output:
  writer = csv.writer(output)
  writer.writerow(['Error','Count'])
  writer.writerows(error_sorted)

with open('user_statistics.csv','w') as output:
  writer = csv.writer(output)
  writer.writerow(['Username','INFO','ERROR'])
  for item in user_sorted:
      onerow = [item[0],item[1][0],item[1][1]]
      writer.writerow(onerow)
#print (err_dic, usr)
