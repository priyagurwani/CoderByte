def check(strParam):
  if strParam.count('x')==strParam.count('o'):
    return True
  else:
    return False
  return strParam
print(check('xoxoxo'))

# Or

def check2(struser):
    num_x=''
    num_o=''
    for i in struser:
        if i=='x':
            num_x+=i
    for j in struser:
        if j=='o':
            num_o+=j

    output=[True if len(num_x)==len(num_o) else False]
    return output
print(check2('xoxox'))
print(check2('xxxooo'))


