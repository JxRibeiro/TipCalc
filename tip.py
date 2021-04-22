# Tip calculator
import random
import numpy as np

def tipcalc(bill):
    
    tip = round(bill * 0.10)
    total = round(bill + tip)
    p30 = round(total * 0.30)
    p70 = round(total * 0.70)
    p1 = random.randrange(1,2)
    print(f'Bill is ${bill}\nTip is ${tip}\nTotal ${total}')
    if p1 == 1:
        print(f'{name1} pays: ${p30}\n{name2} pays: ${p70}')
    else:
        print(f'{name1} pays: ${p70}\n{name2} pays: ${p30}')
name1 = str(input('Enter your name: '))
name2 = str(input('Enter your companion name: '))
bill = float(input('How much is the bill?\n'))
tipcalc(bill)