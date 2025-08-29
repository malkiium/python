def correspond(motif:str, chaine:str, position:int):
    if motif in chaine:
        if chaine[position:position + len(motif)] == motif:
            print(motif, chaine, position)
            return True
    return False

def est_inclus(brin:str, gene:str):
    if brin in gene:
        print(brin, gene)
        return True
    return False



assert correspond("AA", "AAGGTTCC", 4) == False
assert correspond("AT", "ATGCATGC", 4) == True

assert est_inclus("AATC", "GTACAAATCTTGCC") == True
assert est_inclus("AGTC", "GTACAAATCTTGCC") == False
assert est_inclus("AGTC", "GTACAAATCTTGCA") == False
assert est_inclus("AGTC", "GTACAAATCTAGTC") == True