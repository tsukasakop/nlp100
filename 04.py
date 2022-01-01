s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

sp=s.split()
sp[-1].rstrip(".")
mp=dict()
for i in range(len(sp)):
  if i+1 in [1,5,6,7,8,9,15,16,19]:
    mp[sp[i][0]]=i
  else:
    mp[sp[i][0:2]]=i
# print(mp)
