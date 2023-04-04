import os
name = "c:\temp\python\Text.txt"
s = "abc"
ss = os.path.splitext(name) # 파일명을 이름과 확장자로 분리해서 반환하는 함수
print(os.path.splitext(name))
print(ss[0])
print(ss[1])
print(s[-1])

for(path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print(f"{path}\\{filename}")


