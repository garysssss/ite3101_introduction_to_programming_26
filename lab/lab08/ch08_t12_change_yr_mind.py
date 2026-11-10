# key - animal_name : value - location
zoo_animals = {'Unicorn': 'Cotton Candy House',
               'Sloth': 'Rainforest Exhibit',
               'Bengal Tiger': 'Jungle House',
               'Atlantic Puffin': 'Arctic Exhibit',
               'Rockhopper Penguin': 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']         # 刪除樹懶
del zoo_animals['Bengal Tiger']  # 刪除孟加拉虎

print(zoo_animals)