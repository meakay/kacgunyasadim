print("Kaç gün yaşadım ?")
dogumYılı = input("Hangi yılda doğdunuz: ")
ay = input("Kaçıncı ayda doğdunuz: ")
gun = input("Ayın kaçında doğdunuz: ")
formul = ((2020-int(dogumYılı))*365) + ((1 + int(ay))*30) + (25 + int(gun))
anaFormul = formul*24
babaFormul = anaFormul*60
cocukFormul = babaFormul*60
print(cocukFormul, "saniyedir")
print(babaFormul, "dakikadır")
print(anaFormul, "saatdir")
print(formul,"gündür yaşıyorsunuz.")
cıkma = input("Çıkmak için herhangi bir tuşa basınız: ")