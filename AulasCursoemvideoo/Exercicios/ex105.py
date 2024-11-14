def notas(*notas, sit = False):
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['média'] = sum(notas)/len(notas)
    if sit:
        if r['média'] >= 7:
            r['Situação'] = "BOA"
        elif r['média'] >= 5:
            r['Situação'] = "RAZOÁVEL"
        else:
            r['Situação'] = "RAZOÁVEL"
    return r



resp = notas(5.5, 9.5,10,6.5, sit=True)
print(resp)