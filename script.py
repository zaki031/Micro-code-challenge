list_=open("txt.txt").read()
print(''.join(chr(len(i)) for i in list_.replace("M", "").split("C")))
