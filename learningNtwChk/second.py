# Let's build a robot barista !!

print("----------------")

print("Hello ! welcome to NetworkChuck coffee !!!!!!!!!!")

clientName = input("What is your name ? : ")

print("Hello", clientName, "thank you so much for comming in today !")

mennu = """
- hot chocolate
- latte
- tea
- dark coffee
- espresso
"""
price = 8.99

order = input("today on the menu we have : \n" + mennu + "\nwhich do you want ? : ")
amnt = int(input("ok ? and how many do oyu want ? : "))
total = price*amnt
print("the total will be", total)

print()
print("Ok, your", order, "will be ready in a bit")
