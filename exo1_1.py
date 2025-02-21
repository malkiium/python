"""Sachant que la somme : 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 – 1/15 + … tend vers π/4, écrire un
programme permettant de calculer une valeur approchée de π. On pourra écrire deux versions :
selon que l’on demande à l’utilisateur le nombre de termes souhaités, ou la valeur du dénominateur
du dernier terme pris en compte dans le calcul."""

# Function to approximate π using a specified number of terms
def pi1(n):
    pi = 0
    for i in range(n):
        pi += (-1)**i * 1/(2*i+1)  # Add or subtract the term based on the index
    return pi*4  # Multiply the sum by 4 to get the approximation of π

# Function to approximate π using a specified denominator value for the last term
def pi2(d):
    pi = 0
    i = 0
    while 1/(2*i+1) >= 1/d:  # Continue until the term is smaller than 1/d
        pi += (-1)**i * 1/(2*i+1)  # Add or subtract the term based on the index
        i += 1
    return pi*4  # Multiply the sum by 4 to get the approximation of π

# Ask the user for the number of terms and print the approximation of π
nmb = input("Combien de termes souhaités ? ")
print(pi1(int(nmb)))

# Ask the user for the denominator value and print the approximation of π
d = input("Valeur du dénominateur du dernier terme pris en compte dans le calcul ? ")
print(pi2(int(d)))