
res, summy = n, 0
dummy = [n]
while res != 1:
      s = str(res)
      for i in range(len(s)):
            summy += (int(s[i]) ** 2)
      res = summy
      summy = 0
      if res in dummy:
             return False
      dummy.append(res)
      return True
