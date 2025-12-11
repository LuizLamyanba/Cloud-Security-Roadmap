import pyperclip
import sys

TEXT = {"hello":"""hello name is luiz how r u what u doing""",
        "busy":"""sorrry man im busy today can we talk later""",
        "sell":"""starting my new buisness today what about you mann im love making money"""}

if len(sys.argv) < 2:
    print("Usage: python multi_clip_autom.py [keyphrase] - copy to clipboard phrase text")
    sys.exit()

keyphrase = sys.argv[1]

while True:
 if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("text for "+keyphrase+' copie to clipboard')
    break
 else:
    print("no keyphrase assigned sorry")
    
 ans = input("Add new phrase: Y/N: ")
 if ans == 'N':
    print('thank you will meet you again')
    break
 if ans == 'Y':
    k = input("enter the keyphrase: ")
    v = input('enter the line: ')
 TEXT.update({k:v})



