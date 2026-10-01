print('welcome to the pig latin translator')

pyg = 'ay'

Original = input("enter a word:")

if len(original) > 0 and original.isalpha():
    print(original)
else:
    print("empty")