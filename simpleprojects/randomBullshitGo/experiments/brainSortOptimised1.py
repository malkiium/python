def brainSortUnique(tab):
    """
    Brain Sort sur un tableau contenant uniquement
    des valeurs uniques.
    """

    n = len(tab)

    if n <= 1:
        return tab

    placed = set()

    # ------------------------------------------------------------
    # Si un élément est déjà correctement placé :
    #
    # n-1, n+1, n-2, n+2...
    # ------------------------------------------------------------

    def getNextIndex(index):
        for distance in range(1, n + 1):

            left = index - distance
            right = index + distance

            if left >= 0 and left not in placed:
                return left

            if right < n and right not in placed:
                return right

        return None

    # ============================================================
    # 1. PRENDRE LE PLUS GRAND
    # ============================================================

    maxIndex = 0

    for i in range(1, n):
        if tab[i] > tab[maxIndex]:
            maxIndex = i

    lastIndex = n - 1

    # ============================================================
    # 2. LE PLACER À LA FIN
    # ============================================================

    if maxIndex != lastIndex:

        tab[maxIndex], tab[lastIndex] = (
            tab[lastIndex],
            tab[maxIndex]
        )

        # Élément éjecté
        heldIndex = maxIndex

    else:
        # Maximum déjà correctement placé
        heldIndex = None

    placed.add(lastIndex)
    lastPlacedIndex = lastIndex

    # ============================================================
    # 3. BRAIN SORT
    # ============================================================

    while len(placed) < n:

        # --------------------------------------------------------
        # Aucun élément éjecté :
        # prendre l'élément voisin.
        # --------------------------------------------------------

        if heldIndex is None or heldIndex in placed:

            heldIndex = getNextIndex(lastPlacedIndex)

            if heldIndex is None:
                break

        heldItem = tab[heldIndex]

        # --------------------------------------------------------
        # Calculer son rang.
        #
        # Nombre d'éléments plus petits = position finale.
        # --------------------------------------------------------

        placementIndex = 0

        for item in tab:
            if item < heldItem:
                placementIndex += 1

        # --------------------------------------------------------
        # Déjà correctement placé
        # --------------------------------------------------------

        if placementIndex == heldIndex:

            placed.add(heldIndex)

            lastPlacedIndex = heldIndex

            # Rien n'a été éjecté
            heldIndex = None

            continue

        # --------------------------------------------------------
        # Placement
        # --------------------------------------------------------

        tab[heldIndex], tab[placementIndex] = (
            tab[placementIndex],
            tab[heldIndex]
        )

        placed.add(placementIndex)
        lastPlacedIndex = placementIndex

        # heldIndex ne change pas :
        #
        # l'élément qui était à placementIndex
        # vient d'être éjecté à heldIndex.

    return tab


def brainSort(tab):
    """
    Brain Sort complet avec gestion séparée des doublons.
    """

    if len(tab) <= 1:
        return tab

    unique = []
    duplicates = {}
    seen = set()

    # ============================================================
    # 1. SÉPARER LES DOUBLONS
    # ============================================================

    for item in tab:

        if item in seen:

            # Ce n'est plus un élément à trier.
            # On le met avec ses frères.
            duplicates[item].append(item)

        else:

            seen.add(item)

            # Premier exemplaire :
            # celui-ci participera au Brain Sort.
            unique.append(item)

            duplicates[item] = []

    # ============================================================
    # 2. BRAIN SORT UNIQUEMENT SUR LES VALEURS UNIQUES
    # ============================================================

    brainSortUnique(unique)

    # ============================================================
    # 3. RECONSTRUIRE LE TABLEAU
    # ============================================================

    result = []

    for item in unique:

        # Exemplaire principal
        result.append(item)

        # Ses doublons
        result.extend(duplicates[item])

    # Modification du tableau original
    tab[:] = result

    return tab


# ================================================================
# TESTS
# ================================================================

tests = [
    [7, 2, 9, 4, 1, 6, 8, 3, 5],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 0, 3],
    [2, 2, 0, 1],

    [4, 2, 4, 1, 2, 4, 3],
    [5, 5, 5, 5],
    [3, 1, 3, 2, 1],

    [],
    [1],

    [2, 1],
    [1, 2],
    [2, 2],

    [-1, 5, 0, -1, 3],
]


for test in tests:

    original = test.copy()

    result = brainSort(test)

    print(original)
    print("->", result)
    print("correct:", result == sorted(original))
    print()
