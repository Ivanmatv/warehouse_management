from product import Product
from supplier import Supplier
from warehouse import Warehouse


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

supplier = Supplier("Иван")
warehouse_13 = Warehouse("Склад-13")

for product in supplier_products:
    supplier.add_product(product)

format_file = 'JSON'
products_data = supplier.serialize(format_file)


def show_product_in_warehouse(
        warehouse: Warehouse,
        products: dict,
        category: str,
        format_file: str
) -> None:
    warehouse.deserialize(products=products, format_file=format_file)

    warehouse_products = warehouse.get_products_by_category(category)

    print(f"На складе храниться товар категории - {category}:")
    for items in warehouse_products:
        product, quantity = items
        print(f"Продукт: {product} - {quantity} шт.")

def show_categories_in_warehouse(warehouse: Warehouse, products: dict, format_file: str):
    warehouse.deserialize(products=products, format_file=format_file)

    warehouse_categories = warehouse.get_categories()
    formatted_warehouse_categories = ", ".join(warehouse_categories)
    print(
        f"На складе храняться категории:"
        f" {formatted_warehouse_categories}"
    )


print()


show_product_in_warehouse(
    warehouse=warehouse_13,
    products=products_data,
    category=milk_category,
    format_file=format_file
)


print()


show_categories_in_warehouse(
    warehouse=warehouse_13,
    products=products_data,
    format_file=format_file
)