print('___Simple GFR calculator___')
print('Enter this values:')
age = int(input('Enter your age (in Year): '))
weight = int(input('Enter your weight (in KG): '))
sc = float(input('Your serum creatinine level: '))
a = float((140 - age) * weight)
b = float(72 * sc)
c = a / b
print('Your creatinine clearance is', c, 'mL/min')
