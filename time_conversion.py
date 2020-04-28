s = input()
a = int(s[:2])
a1 = s[:2]
if s[8] == 'P' and a<12 and a1!='00':
    b = 12 + a
elif s[8] == 'A' and a1 == '12':
    b = '00'
else:
    b = a1


print(str(b)+s[2:-2])
