import re

'''
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류  에러 1033"
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo != None:
    print(mo.group()) 
'''

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")


match0 = pat.search(data)
match1 = pat.finditer(data)
match2 = pat.findall(data)

for match in match1:
    print(match.group())
    #print(match.start())
    #print(match.end())
    #print(match.span())

print(match2)
#for match in match2:
#    print(match)
# print(pat.sub("\g<1>-******",data))