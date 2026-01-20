first = ['Mike','Joe','Carlos','Jake','Maria','Alice','Lori','Eva','Kate','Luke']
last = ['Smith','Johnson','Myers','Kruger','Mann','Chase','Grana','Clark','Williams','Jacobs']
products = ['glasses','cruches','fan','cup','desk','ipod','phone','lamp','tv','drill']
email = 
print(f'Length of first name list: {len(first)}\
\nLength of last name list: {len(last)}\
\nLength of products list: {len(products)}')
for name in range(len(first)):
    print(f'{first[name]} {last[name]}: {products[name]}\n{first[name].lower()}.{last[name].lower()}@redlands.edu\
    \nDear {first[name]} {last[name]}, I have the following item available for sale: {products[name]}.\nIf you are interested please email me.\n')
