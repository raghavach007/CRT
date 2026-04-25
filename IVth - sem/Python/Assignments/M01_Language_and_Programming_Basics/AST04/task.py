def Reverse_String(s: str) -> str:
      #Task
      reversed_string = ""
      for i in range(len(s)-1, -1, -1):
         reversed_string += s[i]
      return reversed_string
   


if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))
