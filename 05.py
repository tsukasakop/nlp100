s="I am an NLPer"


def sprit(s):
  sp=s.split()
  sp[-1].rstrip(".")
  return sp

def char_ngram(s,n):
  ls=list()
  for i in range(len(s)-n+1):
    ls.append(s[i:i+n])
  return ls

def word_ngram(sp,n):
  ls=list()
  for i in range(len(sp)-n+1):
    ls.append(sp[i:i+n])
  return ls

def main():
  s="I am an NLPer"
  n=2
  sp=sprit(s)
  cg=char_ngram(s, n)  
  wg=word_ngram(sp, n)
  # for i in range(len(cg)):
  #   print(cg[i])
  # for i in range(len(wg)):
  #   print(wg[i])

if __name__ == "__main__":
  main()
