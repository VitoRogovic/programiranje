#DZ

def izracunaj_serijski_otpor(r1, r2):
    """Računa serijski otpor dvaju otpornika."""
    return r1 + r2

def izracunaj_paralelni_otpor(r1, r2):
    """Računa paralelni otpor dvaju otpornika."""
    try:
        return 1 / ((1 / r1) + (1 / r2))
    except ZeroDivisionError:
        print("GREŠKA: Otpor ne smije biti nula.")
        return None

def izracunaj_dijeljenje_napona(u, r1, r2):
    """Računa napon na R2 u serijskom spoju (naponski djelitelj)."""
    try:
        return u * (r2 / (r1 + r2))
    except ZeroDivisionError:
        print("GREŠKA: Zbroj otpora ne smije biti nula.")
        return None


def izracunaj_sumu_liste(lista_vrijednosti):
    """Prima listu brojeva i vraća njihovu sumu."""
    suma = 0
    for vrijednost in lista_vrijednosti:
        suma += vrijednost
    return suma


def ispisi_izbornik():
    print("\n=== KALKULATOR v2.0 ===")
    print("  1. Izračun serijskog otpora (2 otpornika)")
    print("  2. Izračun paralelnog otpora (2 otpornika)")
    print("  3. Naponski djelitelj (U, R1, R2)")
    print("  4. Izračun ukupnog serijskog otpora (N otpornika)")  
    print("  0. Izlaz")



def main():
    while True:
        ispisi_izbornik()
        opcija = input("\nOdaberite opciju: ")

   
        if opcija == "0":
            print("Hvala na korištenju kalkulatora. Doviđenja!")
            break


        elif opcija == "1":
            print("\n--- Serijski otpor (2 otpornika) ---")
            try:
                r1 = float(input("Unesite R1 (Ω): "))
                r2 = float(input("Unesite R2 (Ω): "))
                rezultat = izracunaj_serijski_otpor(r1, r2)
                print(f"Ukupni serijski otpor je: {rezultat:.4f} Ω")
            except ValueError:
                print("GREŠKA: Morate unijeti brojeve.")

    
        elif opcija == "2":
            print("\n--- Paralelni otpor (2 otpornika) ---")
            try:
                r1 = float(input("Unesite R1 (Ω): "))
                r2 = float(input("Unesite R2 (Ω): "))
                rezultat = izracunaj_paralelni_otpor(r1, r2)
                if rezultat is not None:
                    print(f"Ukupni paralelni otpor je: {rezultat:.4f} Ω")
            except ValueError:
                print("GREŠKA: Morate unijeti brojeve.")

        elif opcija == "3":
            print("\n--- Naponski djelitelj ---")
            try:
                u = float(input("Unesite ukupni napon (V): "))
                r1 = float(input("Unesite R1 (Ω): "))
                r2 = float(input("Unesite R2 (Ω): "))
                rezultat = izracunaj_dijeljenje_napona(u, r1, r2)
                if rezultat is not None:
                    print(f"Napon na R2 iznosi: {rezultat:.4f} V")
            except ValueError:
                print("GREŠKA: Morate unijeti brojeve.")

   
        elif opcija == "4":
            print("\n--- Izračun serijskog otpora (N otpornika) ---")
            lista_otpora = []

            while True:
                print(f"   Trenutni otpornici u listi: {[f'{x:.2f} Ω' for x in lista_otpora]}")
                unos_str = input("Unesite vrijednost otpora (ili 'kraj' za izračun): ")

                if unos_str.lower() == "kraj":
                    break

                try:
                    vrijednost = float(unos_str)
