f = open('xyz.txt','w')
lst = ['Hello\n','This is the second first line in the new file.\n','This is the second line in the new file.\n']
f.writelines(lst)
f.close()