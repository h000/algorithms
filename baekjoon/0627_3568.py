string = input()
str = string.split(' ')
s_type = str[0]
del str[0]

for s in str:
    ans = s_type
    s = s.replace(",", '').replace(";", '')
    for i in range(len(s) -1, 0, -1):
        if s[i].isalpha():
          continue
        if s[i] == ']':
          ans += '['
        elif s[i] == '[':
          ans += ']'
        else:
          ans += s[i]
    ans += ' '
    for i in range(len(s)):
      if s[i].isalpha():
        ans += s[i]
    ans += ';'
    print(ans)