def fonction(*args):
    if len(args) == 0:
        return "etcetc"
    elif len(args) == 1:
        return args[0] * 2
    else:
        return ''.join(args)

text = input("bonjour, enter des arguments. ")

fonction(text)