#izbornik za kalkulator
print("izbornik za kalkulator")
print("-----------------------")
print("izaberi opciju: ")
print("1. izračun napona")
print("2. izračun otpora")
print("3. iračun jakosti struje")
print("4. zbroj otpornika (serijski)")
print("5. zbroj otpornika (paralelno)")
print("-------------------------")
opcija=int(input("izaberi opciju (1/2/3/4/5): "))
#struktura grananja
if opcija == 1:
    jakost=int(input("upiši jakost struje: "))
    otpor=int(input("upiši otpor: "))
    napon=jakost*otpor
    print(f"napon je: {napon} V")
elif opcija == 2:
 jakost=int(input("upiši jakost struje: "))
 napon=int(input("upiši napon: "))
 otpor=napon/jakost
 print(f"otpor je: {otpor} Ohm")
elif opcija == 3:

 napon=int(input("upiši napon: "))
 otpor=int(input("upiši otpor: "))
 jakost=napon*otpor
 print(f"jakost je: {jakost} A")
elif opcija == 4:
    otpornik1=int(input("upiši otpor prvog otpornika"))
    otpornik2=int(input("upiši otpor drugog otpornika"))
    otpor=otpornik1+otpornik2
    print(f"otpor je{otpor} Ohm") 
elif opcija == 5:
    otpornik1=int(input("upiši otpor prvog otpornika"))
    otpornik2=int(input("upiši otpor drugog otpornika"))
    otpor=(otpornik1*otpornik2)/(otpornik1+otpornik2)
    print(f"otpor je{otpor} Ohm")
else:
    print("pogrešni unos")