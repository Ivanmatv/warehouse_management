from supplier import Supplier
from warehouse import Warehouse
from product_data import supplier_products

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