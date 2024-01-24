print("აირჩიეთ კატეგორია:")
print("1. მობილურები")
print("2. ტაბები")
print("3. ლეპტოპები")

answer = input("აირჩიეთ კატეგორია: ")
if answer.lower() == "მობილურები" or answer == "1":
    budget = int(input("რა არის თქვენი ბიუჯეტის მაქსიმუმი?: "))
    if budget < 339:
        print("ბოდიში, ამ თანხაში არ გვაქვს პროდუქტი")
    if budget >= 339:
        print("samsung galaxy a04s - 339₾")
    if budget >= 439:
        print("xiamo redmi 13 c - 439₾")
    if budget >= 599:
        print("Samsung galaxy a24 - 599₾")
    if budget >= 900:
        print("xiaomi poco x5 - 679₾")
    if budget >= 799:
        print("samsung galaxy s10e - 799₾")
    if budget >= 829:
        print("samsung galaxy a34 - 829₾")
    if budget >= 1199:
        print("xiaomi poco f5 - 1199₾")
    if budget >= 1699:
        print("samsung galaxy s22 - 1699₾")
    if budget >= 1949:
        print("apple iphone 13 - 1949₾")
if answer.lower() == "ტაბები" or answer == "2":
    budget = int(input("რა არის თქვენი ბიუჯეტის მაქსიმუმი?: "))
    if budget < 349:
        print("ბოდიში, ამ თანხაში არ გვაქვს პროდუქტი")
    if budget >= 349:
        print("Samsung sm-t225 - 349₾")
    if budget >= 599:
        print("realme pad 10.4 inch - 599₾")
    if budget >= 799:
        print("lenovo tab m10 plus - 799₾")
    if budget >= 949:
        print("apple ipad 2021 - 949₾")
    if budget >= 2299:
        print("samsung sm-x710 - 2299₾")
if answer.lower() == "ლეპტოპები" or answer == "3":
    budget = int(input("რა არის თქვენი ბიუჯეტის მაქსიმუმი?: "))
    if budget < 399:
        print("ბოდიში, ამ თანხაში არ გვაქვს პროდუქტი")
    if budget >= 399:
        print("Acer Travelmate - 399₾")
    if budget >= 599:
        print("Acer aspire 3 - 599₾")
    if budget >= 899:
        print("Asus 15 - 899₾")
    if budget >= 999:
        print("Asus vivobook go 15 - 999₾")
    if budget >= 1249:
        print("acer aspire 5 - 1249₾")
