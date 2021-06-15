def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[(len(quotes)-1)])

if __name__== "__main__":
    while True:

        primary()
        input()
