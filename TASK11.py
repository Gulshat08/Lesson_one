melt = {'Sn':232,'Zn':420,'Fe':1539,'Ni':1455,'Si':1415,'Be':1287}
a1 = input()
a2 = input()
print(abs(melt.get(a1,0) - melt.get(a2)))