import MeCab

m_t = MeCab.Tagger('-Owakati')
def tokenizer_mecab_neologd(text):
  text = m_t.parse(text)
  return text.strip().split()

def main():
  
  result = tokenizer_mecab_neologd("ボーボーなボボボーボ・ボーボボとボーちゃん")
  # print(result)
  for i in result:
    print(i,end=" ")
  print()


if __name__ == "__main__":
  main()
