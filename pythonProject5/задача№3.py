with open ('1.txt', encoding='utf-8') as f, open('2.txt', encoding='utf-8') as f1, open('3.txt', encoding='utf-8') as f2, open('4.txt', 'w', encoding='utf-8') as f3:
    name_f = '1.txt'
    name_f1 = '2.txt'
    name_f2 = '3.txt'
    #print(strings)
    name = [name_f1, name_f, name_f2]
    #print(name)
    res = [f1.readlines(), f.readlines(), f2.readlines()]
    #print(res)
    string1 = len(res[0])
    string = len(res[1])
    string2 = len(res[2])
    strings = [string1, string, string2]
    #print(strings)
    for n in range(len(res)):
        f3.write(f'{"".join(name[n])}\n')
        f3.write(f'{str(strings[n])}\n')
        f3.write(f'{"".join(res[n])}\n')



