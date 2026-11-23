class Warehouse:
    def __init__(self, name: str):
        self.__name = name
        self.__products: dict = dict()

    def deserialize(self, products: dict, format_file: str) -> None:
        print(f"Файл десериализован из формата - {format_file}")
        self.__products = products

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

    def get_categories(self) -> list:
        category_index = 2

        categories = []
        for _, items in self.__products.items():
            category = items[category_index]
            categories.append(category)

        return categories

    def __str__(self):
        return self.__name

