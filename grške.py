#izbornik za kalkulator pretvorbe mjernih jedinica
print("izbornik za kalkulator pretvorbe mjernih jedinica")
print("-----------------------")

def ispisi_izbornik():
    print("izaberi opciju: ")
    print("0. izlaz iz programa")
    print("1. pretvorba napona v->mV")
    print("2. pretvorba jakosti struje A->mA")
    print("3. pretvorba otpora ohm->Kohm")
def pretvori_ohm_u_kohm():
    R=float(input("upiši otpor u ohm: "))
    otpor=R/1000
    print(f"jakost je: {otpor} Kohm")
def pretvori_A_u_mA():
   
 I=float(input("upiši jakost struje u A: "))
 jakost=I*1000
 print(f"jakost struje je: {jakost} mA")
  #pretvor otpora
      
def pretvori_V_u_mV():
    U=float(input("upiši napon u V: "))
            
    napon=U*1000
    print(f"napon je: {napon} mV")
   #pretvor jakosti struje
    # Ovdje dolazi kod za pretvorbu volti


    print("-------------------------")
while True:
            ispisi_izbornik()
            try:

                opcija=float(input("izaberi opciju (0/1/2/3): "))
            except Exception as greska:
             print(greska)
            #struktura grananja
            #pretvaranje naponaž
        
            if opcija == 1:
                 pretvori_V_u_mV()
        
            elif opcija == 2:
                pretvori_A_u_mA()
                 
               
            
            elif opcija == 3:
                pretvori_ohm_u_kohm()


               




            elif opcija == 0:
                print("Hvala na korištenju. Doviđenja!")
                break#

            else:
                print("pogrešan unos")
