def brainSort(tab):
    n = len(tab)

    if n <= 1:
        return tab

    # Positions dont on sait que l'élément est définitivement bien placé
    placed = set()

    # ------------------------------------------------------------
    # 1. On cherche le plus grand élément
    # ------------------------------------------------------------

    maxIndex = 0

    for i in range(1, n):
        if tab[i] > tab[maxIndex]:
            maxIndex = i

    # ------------------------------------------------------------
    # 2. On met le plus grand tout à la fin
    # ------------------------------------------------------------

    if maxIndex != n - 1:
        # L'élément qui était à la fin est éjecté à maxIndex.
        tab[maxIndex], tab[n - 1] = tab[n - 1], tab[maxIndex]

        # C'est donc lui qu'on va maintenant essayer de placer.
        currentIndex = maxIndex

    else:
        # Le maximum était déjà correctement placé.
        # Aucun élément n'a été éjecté.
        currentIndex = None

    placed.add(n - 1)

    # ------------------------------------------------------------
    # 3. Placement des autres éléments
    # ------------------------------------------------------------

    while len(placed) < n:

        # Si le cycle précédent est terminé,
        # on prend simplement une position pas encore résolue.
        if currentIndex is None or currentIndex in placed:
            for i in range(n):
                if i not in placed:
                    currentIndex = i
                    break

        x = tab[currentIndex]

        # --------------------------------------------------------
        # Trouver la position de x
        #
        # Sa position est égale au nombre d'éléments < x.
        # --------------------------------------------------------

        target = 0

        for value in tab:
            if value < x:
                target += 1

        # --------------------------------------------------------
        # Doublons
        #
        # Si un x est déjà placé à cette position :
        #
        #     x -> position n
        #     x -> position n + 1
        #     x -> position n + 2
        #     ...
        # --------------------------------------------------------

        while (
            target < n
            and target in placed
            and tab[target] == x
        ):
            target += 1

        # --------------------------------------------------------
        # x était déjà exactement à sa bonne position
        # --------------------------------------------------------

        if target == currentIndex:
            placed.add(currentIndex)

            # Ce cycle est terminé.
            currentIndex = None
            continue

        # --------------------------------------------------------
        # Sécurité
        # --------------------------------------------------------

        if target >= n:
            raise RuntimeError(
                f"Impossible de trouver une position pour {x}"
            )

        if target in placed:
            raise RuntimeError(
                f"Tentative de modifier la position déjà placée {target}"
            )

        # --------------------------------------------------------
        # Placement
        #
        # x va à sa position définitive.
        #
        # L'élément qui était là est éjecté vers currentIndex.
        # Ce sera donc automatiquement le prochain élément traité.
        # --------------------------------------------------------

        tab[currentIndex], tab[target] = (
            tab[target],
            tab[currentIndex]
        )

        placed.add(target)

    return tab


# ================================================================
# TESTS
# ================================================================

tests = [
    [7, 2, 9, 4, 1, 6, 8, 3, 5],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    # Doublons
    [4, 2, 4, 1, 2, 4, 3],
    [5, 5, 5, 5],
    [3, 1, 3, 2, 1],

    # Cas limites
    [],
    [1],
    [2, 1],
    [1, 2],
    [2, 2],

    # Négatifs
    [-1, 5, 0, -1, 3]
]


for test in tests:
    original = test.copy()

    result = brainSort(test)

    print(original)
    print("->", result)
    print("correct:", result == sorted(original))
    print()
