class Cart:
    def __init__(self, request, session_id="cart"):
        self.session = request.session
        cart = self.session.get(session_id)
        
        if not cart:
            cart = self.session[session_id] = {}
        self.cart = cart
        
    def add(self, id, count=1):
        if not(self.cart.get(id)):
            self.cart[id] = count
        self.save()


    def delete(self, id):
        if (self.cart.get(id)):
            del self.cart[id]
        self.save()

    def check_if_exists(self, id):
        if (self.cart.get(id)):
            return True
        return False

    def get_context_data(self):
        return self.cart

    def save(self):
        self.session.modified = True

