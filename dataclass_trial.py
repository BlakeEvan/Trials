from dataclasses import dataclass


@dataclass
class Inventory:
    price: float
    quantity: int
    name: str


items = {1: Inventory(price=12.50, quantity=50, name='small sourdough loaf'),
         2: Inventory(price=25.00, quantity=10, name='large sourdough loaf'),
         3: Inventory(price=3.50, quantity=20, name='cinnamon roll'),
         4: Inventory(price=2.00, quantity=15, name='blueberry scone'),
         5: Inventory(price=7.00, quantity=30, name='coffee cake roll')}

for x in range(1, 6):
    bread_sale = items.get(x)
    print(f'{bread_sale.name.title()}. We have {bread_sale.quantity} on hand at ${bread_sale.price} a piece.')
