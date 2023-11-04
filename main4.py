class FoodName:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, food_item, quantity=1):
        self.items.append((food_item, quantity))
    
    def calculate_total(self):
        total = 0
        for item, quantity in self.items:
            total += item.price * quantity
        return total

def main():
    print("Ласкаво просимо до ресторану!")
    menu = [
        FoodName("Піца Маргарита", 10.99),
        FoodName("Спагетті Карбонара", 12.99),
        FoodName("Салат Цезар", 6.99),
        FoodName("Чікен Нагетс", 8.99)
    ]

    order = Order()

    while True:
        print("\nМеню:")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.name} - ${item.price}")
        
        choice = input("Виберіть страву за номером ('q' для завершення замовлення): ")
        
        if choice == 'q':
            break
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(menu):
                food_item = menu[choice - 1]
                quantity = int(input(f"Скільки порцій {food_item.name} ви хочете замовити? "))
                order.add_item(food_item, quantity)
            else:
                print("Невірний вибір, спробуйте ще раз.")
        except (ValueError, IndexError):
            print("Невірний вибір, спробуйте ще раз.")
    
    total = order.calculate_total()
    print(f"\nЗагальна сума до оплати: ${total:.2f}")
    print("Дякуємо за ваше замовлення!")

if __name__ == "__main__":
    main()