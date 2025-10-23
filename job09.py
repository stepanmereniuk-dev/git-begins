nom ="AMD RYZEN 4000 series"
prix = 300.0
quantite = 4

def augment():
    prix_en_pr = prix*0.10
    print(f"{prix + prix_en_pr}")
    prix_aug = prix + prix_en_pr 
    return prix_aug

while True:
    print(f"{nom}, {prix}, {quantite}")
    res = input("Do you want buy AMD RYZEN 4000 series? ")
    if res == "yes":
        if quantite == 0:
            print("Sorry, we are out of stock")
            break
        prix = augment()
        quantite -= 1
        print(f"Your price is {prix}, and your quantity is {quantite}")
    if res == "no":
        break
    else:
        print("Please answer with 'yes' or 'no'")
print("Thank you for your visit")
    



