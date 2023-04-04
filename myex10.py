import os

def search(dirname):
  filenames = os.listdir(dirname)
  for filename in filenames:
     full_filename = os.path.join(dirname, filename)
     print(full_filename)


spath = input("폴더명을 입력하세요:")
search(spath)