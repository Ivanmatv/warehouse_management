from product import Product


class Warehouse:
    def __init__(self, name: str):
        self.__name = name
        self.__products: dict = dict()

    def add_product(self, product: Product) -> None:
        name = product.get_name()
        barcode = product.get_barcode()
        category = product.get_category()
        amount = product.get_amount()
        storage_temperature = product.get_storage_temperature()
        storage_humidity = product.get_storage_humidity()

        self.__products[barcode] = [
            name, product, category, amount, storage_temperature, storage_humidity
        ]

    def get_products_by_category(self, category: str) -> list[tuple[str, int]]:
        name_index = 0
        category_index = 2

        products = []
        products_count = []

        for _, items in self.__products.items():
            if items[category_index] == category:
                product_name = items[name_index]
                products.append(product_name)
                products_count = [
                    (product, products.count(product)) for product in set(products)
                ]

        return products_count

    def get_category_count(self) ->list[tuple[str, int]]:
        category_index = 2

        categories = []
        categories_count = []

        for _, items in self.__products.items():
            category = items[category_index]
            categories.append(category)
            categories_count = [
                (category, categories.count(category)) for category in set(categories)
            ]

        return categories_count

    def __str__(self):
        return self.__name

