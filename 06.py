s1="paraparaparadise"
s2="paragraph"

def char_ngram(s,n):
  ls=set()
  for i in range(len(s)-n+1):
    ls.add(s[i:i+n])
  return ls

# def prnt(ls):
#   for i in ls:
#     print(i,end=" ")
#   print("")

def main():
  n=2
  x=char_ngram(s1, n)
  y=char_ngram(s2, n)
  wa=x|y
  seki=x&y
  sa=x-y
  if "se" in x:
    print("X has \"se\"")
  else:
    print("X doesnt have \"se\"")
  if "se" in y:
    print("Y has \"se\"")
  else:
    print("Y doesnt have \"se\"")
  
  # prnt(x)
  # prnt(y)
  # prnt(wa)
  # prnt(seki)
  # prnt(sa)

if __name__ == "__main__":
  main()
