pessoas = []
total_pessoas = int(input('Quantas pessoas deseja cadrastrar? '))

while len(pessoas) < total_pessoas:
    pessoas.append(input('Nome:'))

for pessoa in sorted(pessoas):  
    print(pessoa)