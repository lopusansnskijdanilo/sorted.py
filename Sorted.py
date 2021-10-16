choose=str(input('Choose a or b:'))
if choose == 'a':
 text=str(input("Enter text: "))
 SplitString=text.split()
 x=""
 for i in sorted(SplitString):
    x=x+" " +i
 print(x)
 d={}
 for char in set(text):
    d[char]=text.count(char)
 print(d)
elif choose == 'b':
    text1=str(input("Enter text: "))
    SplitString1= sorted(text1.split())
    print(SplitString1)
else:
    print('Uncorrect input')