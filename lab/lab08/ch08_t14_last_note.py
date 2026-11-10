inventory = {
    'gold': 500,
    # Assigned a new list to 'pouch' key
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
# 1. 新增 'pocket' 鍵與其對應的串列
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# 2. 將 'backpack' 內的物品排序
inventory['backpack'].sort()

# 3. 將 'dagger' 從 'backpack' 中移除
inventory['backpack'].remove('dagger')

# 4. 將 'gold' 增加 50
inventory['gold'] = inventory['gold'] + 50 