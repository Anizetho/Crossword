

import re

# Grille 3X3
lines = [r'(WA|AW)[WXY]', r'[^HEX][GROS].', r'O?.[ÉS|SÉ]']
columns = [r'[^ALZ](XM|MX)', r'[AEIOU]+[SON]', r'[^XYZ](TÉ|ÉT)']
myanswer = ['WAW','MOT','XSÉ']


def checkregexcrossword(linesregex, columnsregex,answer) :

    # vérification horizontale
    i = 0
    for elemhor in answer :
        p = re.compile(linesregex[i])
        #print(p)
        #print(p.match(elemhor))
        if p.match(elemhor) is not None :
            pass
        else :
            return str(False) + " --> erreur horizontalement"
        i += 1

    # vérification verticale
    j = 0
    while j < 3 :
        elemvert = answer[0][j] + answer[1][j] + answer[2][j]
        # print(word)
        p = re.compile(columnsregex[j])
        if p.match(elemvert) is not None :
            pass
        else :
            return str(False) + " --> erreur verticalement"
        j += 1

    return str(True) + " --> Tu as gagné !"

print(checkregexcrossword(lines, columns, myanswer))
