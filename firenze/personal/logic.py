
class Favourites:
    def __init__(self, request, session_id="favourites"):
        self.session = request.session
        cart = self.session.get(session_id)
        if not cart:
            cart = self.session[session_id] = []
        self.cart = cart

    def add(self, id):
        if not(id in self.cart):
            self.cart.append(id)
        self.save()

    def delete(self, id):
        if (id in self.cart):
            self.cart.remove(id)
        self.save()

    def check_if_exists(self, id):
        if (id in self.cart):
            return True
        return False
    def get_context_data(self):
        return self.cart
    def save(self):
        self.session.modified = True

