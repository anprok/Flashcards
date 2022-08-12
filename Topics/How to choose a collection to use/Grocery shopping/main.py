from collections import Counter

shopping_list = input().split()
ob = Counter(shopping_list)
for i, k in ob.items():
    print("{} {}".format(k, i))
