# email=input('enter email: ').strip()

# if '@' in email and '.' in email:
#     print('valid email')
# else:
#     print('invalid')

# email=input('enter email: ').strip()
# username,domain=email.split('@')
# if username and '.' in domain:
#      print('valid email')
# else:
#     print('invalid')

# import re

# email=input('enter email: ').strip()

# if re.search('@',email):  #same as  if '@' in email
#     print('valid')
# else:
#     print('invalid')


# import re

# email=input('enter email: ').strip()

# if re.search('.+@.+',email): #.+ are patterns in re library
#     print('valid')
# else:
#     print('invalid')


# import re

# email=input('enter email: ').strip()

# if re.search(r'^.+@.+\.com$',email):
# #the \ is used in python for another thing so for this library to understand you have to specify with r key word like f string og 
# #/Users/milhan/Downloads/cs50/set 7/cs50p_7.py:39: SyntaxWarning: invalid escape sequence '\.' if re.search('.+@.+\.edu',email):
#     print('valid')
# else:
#     print('invalid')


# import re

# email=input('enter email: ').strip()

# if re.search(r'^[^@.]+@[^@]+\.com$',email): #[^@] refer to any char except @
#     print('valid')
# else:
#     print('invalid')

# import re

# email=input('enter email: ').strip()

# if re.search(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$',email): #[] refer to any char inside bracket
#     print('valid')
# else:
#     print('invalid')


# import re

# email=input('enter email: ').strip()

# if re.search(r'\w+@\w+\.(com|edu|net)$',email): #\w refers to word category as well as numbers and compliments
#     print('valid')
# else:
#     print('invalid')


# import re

# email=input('enter email: ').strip()

# if re.search(r'\w+@(\w|.)+\.(com|edu|net)$',email,re.IGNORECASE): 
#     print('valid')
# else:
#     print('invalid')

# import re

# email=input('enter email: ').strip()

# if re.search(r'\w+@(\w+\.)?\w+\.(com|edu|net)$',email,re.IGNORECASE):  
# #? refers to 0 or 1 iteration this is done as if someone type less thand 2 dots itll count as error 
#     print('valid')
# else:
#     print('invalid')

#now reformatting user
# import re

# name=input('whats your name:').strip()
# if "," in name:
#     last,first=name.split(', ') 
#     name=f'{first} {last}'
# print(f'hello {name}')

# import re

# name=input('whats your name:').strip()
# matches=re.search(r"^(.+), (.+)$",name)
# if matches:
#     last,first=matches.group()
#     name=f'{first} {last}'
# print(f'hello {name}')

# import re

# name=input('whats your name:').strip()
# 
# if matches:
#     last=matches.group(1) #group 1 (.+) before ,
#     first=matches.group(2)  #group 2 (.+) after ,
#     name=f'{first} {last} '
# print(f'hello {name}')

# import re

# name=input('whats your name:').strip()

# if matches:=re.search(r"^(.+), *(.+)$",name): #:= walrus operator assigns and use variables for direct comparison
#     last=matches.group(1) #group 1 (.+) before ,
#     first=matches.group(2)  #group 2 (.+) after ,
#     name=f'{first} {last} '
# print(f'hello {name}')

# url=input('whats your url:').strip()
# username=url.replace("https://twitter.com/","")
# print("username:",username)


# url=input('whats your url:').strip()
# username=url.removeprefix("https://twitter.com/") #if at start itll remove in output
# print("username:",username)

# import re
# url=input('whats your url:').strip()
# username=re.sub(r"https://twitter.com/","",url) #substitutes value here . could refer anything after twitter so remember keywords of re
# print("username:",username)


# import re
# url=input('whats your url:').strip()
# username=re.sub(r"https?://(www\.)?twitter\.com/","",url) #? refers to 0 or 1 s ie http or https
# print("username:",username)

# import re
# url=input('whats your url:').strip()
# matches=re.search(r"https?://(www\.)?twitter\.com/(.+)",url,re.IGNORECASE) 
# if matches: 
#     print("username:",matches.group(2)) # group 1 was (www.) and 2 was (.+)


import re
url=input('whats your url:').strip()
if matches:=re.search(r"https?://(?:www\.)twitter\.com/([a-zA-Z0-9]+)",url,re.IGNORECASE) : 
    print("username:",matches.group(1)) #used (?:...)