astr = 'Hello World'
try: 
    istr = int(astr) #dangerous code
except:
    istr = -1 #quando falhar o código cairá aqui

print('First', istr)