def prime_numbers(number=250):
    data = set()
    for i in range(2, number + 1):
        for b in range(2, int((i/2))+1):
            if i % b == 0:
                break
            else:
                data.add(i)
    return print(data)


prime_numbers()

with open('results.txt', 'w') as f:
    f.write(str(prime_numbers()))
    print('Worked out')
