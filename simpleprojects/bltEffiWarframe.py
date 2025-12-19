print("\n\n\n")

maxBlts = float(input("what is the Magazine's Max ammo ? : "))
ammoEffi = float(input("what is the Ammo Efficiency, in %  : "))

bltPrBlt = 1-(ammoEffi/100)

efctBlt = maxBlts/bltPrBlt

print(
    "\n\n",
    "Number of Bullets in Magazine", maxBlts, "\n",
    "Number of efficienty applied :", ammoEffi, "%", "\n",
    "Number of Magazine Bullet used Per Bullet used :", bltPrBlt, "\n",
    "Number of Effective Bullets in Magazine", efctBlt, "\n",
    )