def ispisi_izbornik():
    # Izbornik za kalkulator

    print("----------------------")
    print("Izbornik za kalkulator")
    print("----------------------")
    print("1. Izračun napona struje")
    print("2. Izračun otpora struje")
    print("3. Izračun jakosti struje")
    print("0=izlaz")
    print("----------------------")
def izracunaj_napon(jakost,otpor):
    return jakost*otpor
def izracunaj_otpor(jakost,napon):
    return napon/jakost
def izracunaj_jakost(napon,otpor):
    return napon/otpor
    






while True:
    ispisi_izbornik()
    try:
        opcija = int(input("Izaberite operaciju (1 / 2 / 3/ 0):"))
    except Exception as greska:
        print(f"pogrešan unos. Molim unesite broj od 0 do 3.\nodaberi 0 za izlaz.")
        continue
    #Struktura grananja
    if opcija == 1: 
        try:    # == != < > <> >= <= - operatori usporedbe
            print("Izračun napona struje")
            jakost = int(input("Upiši jakost struje: "))
            otpor = int(input("Upiši otpor: "))
            napon = izracunaj_napon(jakost,otpor)
            print(f"Napon struje je: {napon} V")
        except ValueError:
            print(f"pogrešan unos. Molim unesite broj \n")
            continue
        except ZeroDivisionError:
            print(f"nemogu dijelit brojeve!!!")
            continue
        except Exception as greska:
            print(f"nepoznata greška pokušaj ponovo")
            continue
    elif opcija == 0:
        print("pozdrav")
        break
    elif opcija == 2:
        try:
            print("Izračun otpora struje")
            napon = int(input("Upiši napon: "))
            jakost = int(input("Upiši jakost struje: "))
            otpor = izracunaj_otpor(napon,jakost)
            print(f"Otpor je: {otpor} Ohm")
        
        except ValueError:
            print(f"pogrešan unos. Molim unesite broj \n")
            continue
        except ZeroDivisionError:
            print(f"nemogu dijelit brojeve!!!")
            continue
        except Exception as greska:
            print(f"nepoznata greška pokušaj ponovo")
            continue
    elif opcija == 3:
        try:
            print("Izračun jakosti struje")
            napon = int(input("Upiši napon: "))
            otpor = int(input("Upiši otpor: "))
            jakost = izracunaj_jakost(napon,otpor)
            print(f"Jakost struje je: {jakost} A")
        except Exception as greska:
            print(f"nepoznata greška pokušaj ponovo")
            continue
        except ValueError:
            print(f"pogrešan unos. Molim unesite broj \n")
            continue
        except ZeroDivisionError:
            print(f"nemogu dijelit brojeve!!!")
            continue
    else:
        print("Pogrešan unos")
        
