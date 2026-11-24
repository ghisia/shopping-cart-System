class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def addProduct(self, product):
        self.products.append(product)
        print(f"{product.name} added to cart.")
       
    def removeProduct(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} removed from cart.")
        else:
            print("product not found in cart.")

    def calculateTotal(self):
        subtotal = 0

        for product in self.products:
            subtotal += product.price * product.qty
        return subtotal

    def calculateDiscount(self):
        subtotal = self.calculateTotal()

        if subtotal > 100000:
            return subtotal * 0.10
        else:
            return 0

    def displayCart(self):
        print("\nShoping Cart\n")

        for product in self.products:
            print(f"Product: {product.name}")
            print(f"Price: {product.price} RWF")
            print(f"Quantity: {product.qty}")
            print()

        subtotal = self.calculateTotal()
        discount = self.calculateDiscount()
        total = subtotal - discount  

        print(f"Subtotal: {subtotal:.0f} RWF")
        print(f"Discount: {discount:.0f} RWF")
        print(f"Total: {total:.0f} RWF")


laptop = Product("Laptop", 800000, 1)
mouse = Product("Mouse", 15000, 2)

cart = ShoppingCart()


cart.addProduct(laptop)
cart.addProduct(mouse)

cart.displayCart()





