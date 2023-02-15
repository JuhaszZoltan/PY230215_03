from module import Kategoria

kategoriak:list[Kategoria] = []
file = open(file='titanic.txt', mode='r', encoding='utf-8')
for s in file: kategoriak.append(Kategoria(s))

print(f'2. feladat: {len(kategoriak)} db')

usz:int = 0
for k in kategoriak:
    usz += (k.eltuntek + k.tulelok)
print(f'3. feladat: {usz} fő')

kulcsszo:str = input('4. feladat: Kulcsszó: ')
volt_talalat:bool = False
for k in kategoriak:
    if kulcsszo in k.nev:
        print('\tVan találat!')
        volt_talalat = True
        break
else: print('\tNincs találat!')

if volt_talalat:
    print('5. feladat:')
    for k in kategoriak:
        if kulcsszo in k.nev:
            print(f'\t{k.nev} {k.tulelok + k.eltuntek} fő')

meghaladta:list[str] = []
for k in kategoriak:
    if k.eltuntek > (k.eltuntek + k.tulelok)* .6:
        meghaladta.append(k.nev)
print('6. feladat:')
for kn in meghaladta:
    print(f'\t{kn}')

m:int = 0
for i in range(1, len(kategoriak)):
    if kategoriak[i].tulelok > kategoriak[m].tulelok:
        m = i
print(f'7. feladat: {kategoriak[m].nev}')