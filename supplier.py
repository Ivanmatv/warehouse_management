from product import Product


class Supplier:
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

    def serialize(self, file_format: str) -> dict:
        print(f"Список продуктов преобразован в формат - {file_format}")
        return self.__products

    def __str__(self):
        return self.__name