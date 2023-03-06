

"""Programme permettant de remplacer '%' par 'M' et 'M' par '%'"""

texte=("La %ort 100M")

def transcription_clavier(texte):
    res = ""
    for i in range(len(texte)):
        if texte[i] == "M":
            res += "%"
        elif texte[i] == "%":
            res += "M"
        else:
            res += texte[i]
    return res

print(transcription_clavier(texte))