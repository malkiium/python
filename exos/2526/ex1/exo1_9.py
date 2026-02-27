for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                aa = str(a)+str(a)
                bb = str(b)+str(b)
                cc = str(c)+str(c)
                dd = str(d)+str(d)
                ccdd = cc+dd
                aai, bbi, cci, ddi, ccddi = int(aa), int(bb), int(cc), int(dd), int(ccdd)
                if aai*bbi == ccddi:
                    print(aa, "x", bb, "=", ccdd)