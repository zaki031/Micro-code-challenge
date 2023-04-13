print(''.join(chr(len(i)) for i in open("t.txt").read().replace("M", "").split("C")))
