#break and continue Statements, and else Clauses on Loops¶
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break;
    else:
        print(n, 'is a prime number')

for i in [5, 4, 3, 2, 1]:
    print(i)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print("Happy new Year:", friend)
print('Done!')

