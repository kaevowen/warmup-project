
a = str()

with open('./input.txt', 'r') as f:
    a = f.read()

with open('./output.txt', 'w') as f:
    f.write(f'Processed: {a}')
