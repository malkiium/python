limtbot = 0
limttop = 25700000
steps = 0

while limttop - limtbot > 1:
    limtmid = (limttop + limtbot) // 2
    a = 0
    a += limtmid
    b = 0
    b += limtmid
    
    print(f"{limtmid}, :: {id(a) == id(b)}")

    if id(a) == id(b):
        limtbot = limtmid
    else:
        limttop = limtmid
    steps+=1

print(f"  {limtbot} est caché")
print(f"  {limtbot + 1} n'est PAS caché")
print(f"{steps} steps")