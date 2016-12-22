while True:
      x = input(int('Put a number: '))
      try:
         print(bin(x))
         print(hex(x))
         print(oct(x))
      except TypeError as EX:
            print(EX)
