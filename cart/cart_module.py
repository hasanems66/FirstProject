from product.models import Book

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self,request):
        self.session = request.session

        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart


    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            book= Book.objects.get(id=int(item['id']))
            item['book'] = book
            item['total'] = int(item['quantity']) * int(item['price'])
            item['id'] = book.id
            yield item

    def add(self, book, quantity):
        book_id = str(book.id)
        if book_id not in self.cart:
            if book.discount:
                self.cart[book_id] = {'quantity': 0, 'price': str(book.discounted_price), 'id': str(book.id)}
            else:
                self.cart[book_id] = {'quantity': 0, 'price': str(book.price), 'id': str(book.id)}

        self.cart[book_id]['quantity'] += int(quantity)
        self.save()

    # method total price
    def total(self):
        cart= self.cart.values()
        total = 0
        for item in cart:
            total += int(item['price']) * int(item['quantity'])

        return total

    # remove method product from cart
    def delete(self,id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    #The method of removing products from the shopping cart after placing an order
    def remove_cart(self):
        del self.session[CART_SESSION_ID]

    def save(self):
        self.session.modified = True



