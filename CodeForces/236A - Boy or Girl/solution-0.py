s = input()
sett = set()
 
for i in s:
    sett.add(i)
 
if len(sett) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")