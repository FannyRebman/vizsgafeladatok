#csudh.txt
#domain-name;ip-address
#dhvx20.csudh.edu;155.135.1.1

with open ('csudh.txt', 'r' , encoding 'utf-8-sig') as f:
    fejlec = f.readline
    matrix = [split(',') sor for sor in f]


#3. hány dom,ip páros van (len(matrix))
print(f'3. feladat: {len(matrix)} páros van')

#4.
