def match(string, substring):
    submatch = []
    index = []

    for i in range(len(string)-len(substring)):
        if (string[i] == substring[0]):
            submatch = []
            for j in range(len(substring)):
                if (string[i+j] == substring[j]):
                    submatch.append(string[i+j])
                else:
                    submatch = "".join(submatch)
                    for k in range(1,len(submatch)):
                        if (submatch[k:len(submatch)] == submatch[0:len(submatch)-k]):
                            i =  (i+j) - len(submatch[k:len(submatch)])
                            break
                        elif (k == len(submatch)-1):
                            i = i+j
                        else:
                            continue
                    break
                if (j == len(substring)-1):
                    index.append(i)
    return index

dna = "GTTATCCCATTCACCCTATAATCGGCGTTGGACCATCGATGG"
cari_dna = "ATC"
pencocokan = match(dna, cari_dna)
print(pencocokan)
print("terdapat "+str(len(pencocokan))+" DNA "+ cari_dna)