print('welcome to the pig latin translator')

pyg = 'ay'

Original = input("enter a word:")

if len(Original) > 0 and Original.isalpha():
    print(Original)
else:
    print("empty")