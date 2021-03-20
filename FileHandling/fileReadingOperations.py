f = open('xyz.txt','r')
lst = ['Hello\n','This is the second first line in the new file.\n','This is the second line in the new file.\n']
s = f.readlines()
print(s)
print(' ')
rd = f.readline()
print(rd)
print(' ')
f.close()