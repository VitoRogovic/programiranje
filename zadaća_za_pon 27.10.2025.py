#1. zadatak
#pitamo korisnika za broj godina
g_u=input("ispiši koliko imaš godina")
#koristimo samo input jer ćemo u sljedećoj komandi pretvorit taj unos u cijeli broj
g=int(g_u)
#korištenjem komande int pretvaramo unosi iz kmande input u cijeli broj
if g>=18:
    print("punoljetni ste")
else:
    print("maloljetni ste")
#ovim grananjem koristimo dobivenu informaciju te određujemo dali je korisnik 18+ ili je maloljetan. Ako je relutat tj vrijednost dobivena korisnikovim unosom veća od 18 oda se izvršava komanda if i ispisuje se text: punoljetni ste. Svi rezultati manji od 18 aktiviraju else komandu koja ispisuje maloljetni ste.
#2. zadatak
print("ovaj program će ispisati sve brojeve od 1 do broja kojeg upišete")
n_u:input("unesite jedan cijeli pozitivan broj")
#ovom funkcijom trazimo unos korisnika za jedan cijeli pozitivan broj kako bismo znali do kojeg broja da progam ispisuje, kosristimo input a ne int(input) jer ćemo int iskoristit u nastavku koda
n=int(n_u)
#funkicja int pretvara rezultat koji je unio korisnik u cijeli broj
print(f"brojevi od 1 do ",{n}":")
for broj in range (1,n+1):
    print(broj)
#for broj in range funkicja će nam definirat brojeve od 1 do n ( n+1 je definiran zato jer ako stavimo samo n će nam ispisat broje do n a ne i sam n)
#3.zadatak
def kreiraj_pozdrav(ime)
pozdravna poruka=f"pozdrav",{ime}"!"
return pozdravna_poruka
pozdrav za anu=kreiraj pozdrav("Ana")
pozdrav_za_marka=kreiraj_pozdrav("Marko")
print(pozdrav za anu)
print(pozdrav_za_marka)
