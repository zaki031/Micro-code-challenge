print(''.join(chr(len(i)) for i in open("txt.txt").read().replace("M", "").split("C")))
