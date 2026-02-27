def anagram(word1 : str, word2 : str) -> bool:
    word1, word2 = list(word1), list(word2)
    print(word1, word2)

    if len(word1) != len(word2):
        return(False)
    else:
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    word1[i] = None
                    word2[j] = None
                    break
        for i in range(len(word1)):
            if word1[i] != None:
                print("ce ne sont pas des anagrames.")
                print(word1)
                return(False)
        print("ce sont des anagrames.")
        return(True)

anagram("chine", "niche")