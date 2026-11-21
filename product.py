class Product:
    def __init__(
            self,
            name: str,
            category: str,
            barcode: int,
            amount: int,
            storage_temperature: float = None,
            storage_humidity: float = None
    ):
        self.__name = name
        self.__category = category
        self.__barcode = barcode
        self.__amount = amount
        self.__storage_temperature = storage_temperature
        self.__storage_humidity = storage_humidity

    def get_name(self) -> str:
        return self.__name

    def get_category(self) -> str:
        return self.__category

    def get_barcode(self) -> int:
        return self.__barcode

    def get_amount(self) -> int:
        return self.__amount

    def get_storage_temperature(self) -> float:
        return self.__storage_temperature

    def get_storage_humidity(self) -> float:
        return self.__storage_humidity
