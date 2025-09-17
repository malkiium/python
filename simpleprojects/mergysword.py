import matplotlib.pyplot as plt
import random

# 60 images par seconde
FPS = 560
delaytime = 3 / FPS  

def show_list(lst, highlight=None, delay=delaytime):
    plt.clf()  # efface l'ancienne figure
    colors = ['skyblue'] * len(lst)
    
    # Si on veut mettre en valeur des indices
    if highlight:
        for i in highlight:
            colors[i] = 'orange'
    
    plt.bar(range(len(lst)), lst, color=colors)
    plt.pause(delay)

def merge_sort(lst, left=0, right=None, delay=delaytime):
    if right is None:
        right = len(lst) - 1

    if left < right:
        mid = (left + right) // 2
        merge_sort(lst, left, mid, delay)
        merge_sort(lst, mid + 1, right, delay)
        merge(lst, left, mid, right, delay)

def merge(lst, left, mid, right, delay):
    n1 = mid - left + 1
    n2 = right - mid

    L = lst[left:left+n1]
    R = lst[mid+1:mid+1+n2]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        show_list(lst, highlight=[k], delay=delay)
        k += 1

    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1
        show_list(lst, highlight=[k-1], delay=delay)

    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1
        show_list(lst, highlight=[k-1], delay=delay)


# Exemple
if __name__ == "__main__":
    liste = [random.randint(1, 500) for _ in range(150)]
    print("Liste de départ :", liste)

    plt.ion()  # mode interactif
    show_list(liste, delay=1)
    merge_sort(liste, delay=delaytime)
    show_list(liste, delay=2)
    plt.ioff()
    plt.show()

    print("Résultat final :", liste)
