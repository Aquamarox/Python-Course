from typing import Union


class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category: str) -> None:
        self.category = new_category

    def edit_price(self, new_price: float) -> None:
        self.price = new_price

    def set_sale(self, sale: float) -> None:
        if 0 <= sale <= 100:
            self.sale = sale
        else:
            raise ValueError("Скидка должна быть в диапазоне от 0 до 100%")

    def cancel_sale(self) -> None:
        self.sale = 0

    def get_price(self) -> float:
        if self.sale > 0:
            discounted_price = self.price * (1 - self.sale / 100)
            return round(discounted_price, 2)
        return self.price

    def __repr__(self) -> str:
        price_with_sale = self.get_price()
        if self.sale > 0:
            return (f"Product(name='{self.name}', "
                    f"category='{self.category}', "
                    f"price={self.price}, "
                    f"sale={self.sale}%, "
                    f"final_price={price_with_sale})")
        else:
            return (f"Product(name='{self.name}', "
                    f"category='{self.category}', "
                    f"price={self.price})")
