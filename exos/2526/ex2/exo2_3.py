def anagram(word1 : str, word2 : str) -> bool:
    word1, word2 = list(word1), list(word2)
    print(word1, word2)
    dif = len(word1)-1

    if len(word1) != len(word2):
        return(-1)
    else:
        for i in range(len(word1)):
            for j in range(i, len(word2)):
                if word1[i] == word2[j]:
                    dif -=1
        dif -= 1
        if dif > 0:
            print("ce ne sont pas des anagrames.")
            print(dif)
            return(False)
        else:
            print("ce sont des anagrames.")
            return(True)

anagram("chine", "niche")