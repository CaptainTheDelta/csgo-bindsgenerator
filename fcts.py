# coding: utf-8

def bind(key,cmd):
    """Renvoie le bind de la touche et de la commande.

    Args:
        key (str): Touche à bind.
        cmd (str): Commande du bind.
    
    Return:
        (str): Texte du bind.
    """
    if type(key) != str and type(cmd) != str:
        raise TypeError

    return f"bind {key} '{cmd}'"

def save(binds,file):
    """Enregistre les binds dans file.

    Args:
        binds (lst): Liste de binds.
        file (str): Chemin du fichier file.
    """
    if type(binds) != list and type(file) != str:
        raise TypeError

    with open(file,'w') as f:
        f.write('\n'.join([bind(k,c) for k,c in binds]))


def load(file):
    """Lit le fichier et renvoie la liste des binds.

    Args:
        file (path): Chemin du fichier file.

    Return:
        (list): Liste des binds.
    """
    if type(file) != str:
        raise TypeError

    data = []
    binds = []

    with open(file,'r') as f:
        data = f.read().splitlines()

    for d in data:
        if d.startswith('bind '):
            d = d[5:].replace('"','').replace("'",'')
            i = d.find(' ')

            k,c = d[:i], d[i:]
            c = ' '.join(c.split())

            binds.append((k,c))

    return binds