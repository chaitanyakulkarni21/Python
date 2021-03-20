#WAP to find HCF of two numbers 
def hcf(a,b):
  if a > b:
    small = b
  else:
    small = a
  for i in range(1, small+1):
    if (i%a == 0) and (i%b == 0):
      hcf = i
  return hcf
  
print(hcf(20,40))
