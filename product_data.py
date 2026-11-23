from product import Product

milk_category = "Milk"
cookie_category = "Cookie"
paper_category = "Paper"
bread_category = "Bread"
wood_category = "Wood"

domic_v_derevne = Product(name="Домик в деревне", category=milk_category, barcode=12345, amount=10, storage_temperature=5)
milka = Product(name="Milka", category=cookie_category, barcode=22233, amount=20, storage_temperature=10, storage_humidity=5)
bumaga = Product(name="Бумага", category=paper_category, barcode=77788, amount=20, storage_humidity=5)
borodinsky = Product(name="Бородинский", category=bread_category, barcode=11111, amount=15, storage_humidity=10)
doska = Product(name="Брус", category=wood_category, barcode=89765, amount=15, storage_temperature=10, storage_humidity=5)
ovsaynoe_pechene = Product(name="Овсянное", category=cookie_category, barcode=32145, amount=20, storage_temperature=10, storage_humidity=5)

supplier_products = [domic_v_derevne, milka, bumaga, borodinsky, doska, ovsaynoe_pechene]