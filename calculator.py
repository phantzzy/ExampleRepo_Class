"""
Kalkulatora modulis ar vienkāršām matemātiskām funkcijām.

Šis fails demonstrē:
- Funkciju definēšanu
- Docstrings (dokumentācijas teksti)
- Moduļu importēšanu
"""


def saskaitit(a, b):
    """
    Saskaita divus skaitļus.
    
    Args:
        a: Pirmais skaitlis
        b: Otrais skaitlis
    
    Returns:
        Summa
    """
    return a + b


def atnemit(a, b):
    """
    Atņem otro skaitli no pirmā.
    
    Args:
        a: Pirmais skaitlis
        b: Otrais skaitlis
    
    Returns:
        Starpība
    """
    return a - b


def reizinaat(a, b):
    """
    Reizina divus skaitļus.
    
    Args:
        a: Pirmais skaitlis
        b: Otrais skaitlis
    
    Returns:
        Reizinājums
    """
    return a * b


def daliit(a, b):
    """
    Dala pirmo skaitli ar otro.
    
    Args:
        a: Dalāmais
        b: Dalītājs
    
    Returns:
        Dalījums vai kļūdas paziņojums
    """
    if b == 0:
        return "Kļūda: Nevar dalīt ar nulli!"
    return a / b
