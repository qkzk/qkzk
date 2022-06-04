from string import ascii_lowercase as lettres


def derniere_occurence(motif):
    taille_motif = len(motif)
    dict_derniere_occurence = {
        lettre: taille_motif for lettre in lettres + ' '}
    for i in range(taille_motif - 1):
        dict_derniere_occurence[motif[i]] = taille_motif - i - 1
    return dict_derniere_occurence


def bmh(motif, texte):
    taille_motif = len(motif)
    taille_texte = len(texte)
    dict_derniere_occurence = derniere_occurence(motif)

    occurences = []
    j = 0
    while j <= taille_texte - taille_motif:
        i = taille_motif - 1
        while i >= 0 and texte[j + i] == motif[i]:
            i -= 1
        if i == -1:
            occurences.append(j)
            j += 1
        else:
            indice_non_corresp = j + i
            decalage = dict_derniere_occurence[texte[indice_non_corresp]]
            j += decalage
    return occurences


if __name__ == '__main__':
    texte = "bonjour bon bonne nuit bonnet bno bonbon"
    motif = "bon"
    print(bmh(motif, texte))
