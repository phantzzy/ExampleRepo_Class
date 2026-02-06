"""
Galvenā programma - Python piemērs Git mācībām
"""

from calculator import saskaitit, atnemit, reizinaat, daliit


def main():
    """Galvenā funkcija, kas demonstrē kalkulatora izmantošanu."""
    print("=" * 40)
    print("🧮 Vienkāršais Kalkulators")
    print("=" * 40)
    
    # Piemēri ar skaitļiem
    a = 10
    b = 5
    
    print(f"\nSkaitļi: a = {a}, b = {b}")
    print("-" * 40)
    
    print(f"Saskaitīšana: {a} + {b} = {saskaitit(a, b)}")
    print(f"Atņemšana:    {a} - {b} = {atnemit(a, b)}")
    print(f"Reizināšana:  {a} × {b} = {reizinaat(a, b)}")
    print(f"Dalīšana:     {a} ÷ {b} = {daliit(a, b)}")
    
    print("\n" + "=" * 40)
    print("Paldies par kalkulatora izmantošanu! 👋")
    print("=" * 40)


if __name__ == "__main__":
    main()
