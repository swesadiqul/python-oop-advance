class ElectronicDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ProductReview:
    def write_review(self):
        return "Writing a product review..."

class ProductSales:
    def sell(self):
        return "Selling the product..."

class Smartphone(ElectronicDevice, ProductReview, ProductSales):
    pass

phone = Smartphone("Samsung", "Galaxy S21")

print(phone.brand, phone.model)  # Output: Samsung Galaxy S21
print(phone.write_review())      # Output: Writing a product review...
print(phone.sell())              # Output: Selling the product...
