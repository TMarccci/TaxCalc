taxrate = input("Add meg az adó értékének az országkódját! (Magyarország: hun) \n ")
if taxrate == "hun":
  taxratefull = 0.27
  print("Beállítva! 27% áfa")
  taxrateback = 1.27
else:
  print("Érvénytelen formátum")
print(" ")

arfolyam = input("Add meg az valuta típusát! (Forint: ft) \n ")
if arfolyam == "ft":
  valuta = "HUF"
  print ("Beállítva! Magyar Forint")
else:
  print ("Érvénytelen valuta!")
print("")

nvagyb = input("Hogyan szeretnél számolni? \n Nettó összegből bruttó összeget vagy bruttó össszeget nettóra? \n Nettó -> Bruttó = nb \n Bruttó -> Nettó = bn \n \n ")
print(' ')

if nvagyb == "nb":
  netto = input("Add meg a nettó összeget! \n ")
  afanb = int(netto) * taxratefull
  nbvegfull = int(afanb) + int(netto)
  print(" ")
  print("Nettó összeg: ", netto, valuta)
  print("Bruttó összeg: ", nbvegfull, valuta)
  print("Áfa összege: ", afanb, valuta)
elif nvagyb == "bn":
  brutto = input("Add meg a bruttó összeget! \n ")
  bnvegfull = int(brutto) / taxrateback
  afabn = int(bnvegfull) - int(brutto)
  print(" ")
  print("Nettó összeg: ", bnvegfull, valuta)
  print("Bruttó összeg: ", brutto, valuta)
  print("Áfa összege: ", afabn, valuta)
else:
  print(" ")
  print("Érvénytelen módszer!")

print(" ")
input("Nyomj egy Enter a kilépéshez!")

