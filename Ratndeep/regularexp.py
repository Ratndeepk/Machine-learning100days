import re 
match = re.search('iig','called piig') 
print(match.group())  # output - 'iig' 

match = re.search('igs','called piig') 
#print(match.group())  # error None

def find(pat,text):
    match=re.search(pat,text)
    if match:
        print(match.group()) 
    else:
        print("Not Found") 

find('asdav','asdvads')
find('..d','asdvadsv') # '.' when value could be anything

find(r'c\.l','c.lled piiiig') # r means raw text

'''
\w word char
\w digit
\s whitespace
\S non-whitespace
'''
find(r'\d\s+\d\s+\d','1        2         3') # '+' stands for 1 or more
# '*' stands for 0 or more 

find(r'[\w.]+@[\w.]+','blah .nic.p@gmail.com wawsf @') #[] will take as raw value inside []
# .nic.p@gmail.com 
find(r'\w[\w.]+@[\w.]+','blah .nic.p@gmail.com wawsf @')
# nic.p@gmail.com 

m =re.search(r'(\w[\w.]+)@([\w.]+)','blah .nic.p@gmail.com wawsf @')
print(m.group())  #nic.p@gmail.com
print(m.group(1)) #nic.p
print(m.group(2)) #gmail.com

print(re.findall(r'\w[\w.]+@[\w.]+','blah .nic.p@gmail.com wawsf foo@bar'))
# ['nic.p@gmail.com','foo@bar']

print(re.findall(r'(\w[\w.]+)@([\w.]+)','blah .nic.p@gmail.com wawsf foo@bar'))
# [('nic.p'),('gmail.com'),'('foo','bar')]

print(dir(re)) #help fo re

