maior = -1
print('Before', maior)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > maior:
        maior = the_num
    print(maior, the_num)

print('After', maior)