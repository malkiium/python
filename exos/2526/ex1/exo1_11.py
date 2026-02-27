def hammingplus(word1 : str, word2 : str) -> int:
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
        print(dif)
        return(dif)

def hamming(word1 : str, word2 : str) -> int:
    word1, word2 = list(word1), list(word2)
    print(word1, word2)
    dif = len(word1)

    if len(word1) != len(word2):
        return(-1)
    else:
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                dif -=1
        print(dif)
        return(dif)
    


hammingplus("hello", "ehooo")
hamming("hello", "ehooo")