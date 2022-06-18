import re

# var_input = input('input any variable')

# content = 'Google Chrome'
# pattern = 'ro'

# reg = re.compile(pattern)
# result = reg.match(content)



# if result:
#      print(result.group())
     

# result = reg.search(content)

# if result:
#      print(result.group())

#------------------------------------------------

def print_regular_exp(cont,pat):
     reg = re.compile(pat)
     result = reg.match(cont)

     if result:
          print(result.group())

     else:
          print("not match")

content = 'Google a35, 85r Cloud'
pattern1 = r'^Google'
pattern2 = r'oud$'

print_regular_exp(content,pattern1)
print_regular_exp(content,pattern2)

content = 'windows 10 MacOS X Ubuntu 20.02 CentOS'
pattern3 = r'.*'
pattern4 = r'\w+'
pattern5 = r'.+\d+\s'


print_regular_exp(content,pattern3)
print_regular_exp(content,pattern4)
print_regular_exp(content,pattern5)

#---------------------------------------------

content = '0120-45-4914'
pattern6 = r'^\d{4}-\d{2}-\d{4}$'
print_regular_exp(content,pattern6)

content = 'https://flfie/gksiekg/index.html'
pattern7 = r'^https://(\w+/?)+(\.[a-z]+/?)?$'
print_regular_exp(content,pattern7)
content = 'http://hgski/gksie.jp'
print_regular_exp(content,pattern7)

content = 'https://hgski/gksie/s.us'
print_regular_exp(content,pattern7)

content = 'https://hgski/gksie/gsjkgw03/gjsk395892/jff.jp/'
print_regular_exp(content,pattern7)