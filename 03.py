s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

for i in s.split():
  if "." in i:
    print(len(i)-1 ,end="")
  else:
    print(len(i) ,end="")
print("")
