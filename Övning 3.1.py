abonnemang = int(input("Hur många samtals minuter per månad? ")) #Ber om en input i data typen int

if abonnemang <= 33: #Om inputen är 33 eller mindre så kommer den att skriva ut att man bör använda kontant abonnemanget
    print("Välj kontant abonnemanget")
elif abonnemang > 33 and abonnemang < 66: #Om inputen var mellan 33 och 66 så skriver den att man ska använda normala abonnemanget
    print("Välj normal abonnemanget")
elif abonnemang <= 66: #Om man skriver något högre än 66 så kommer den skriva ut att man ska använda sig av plus abonnemanget
    print("Välj plus abonnemanget")
