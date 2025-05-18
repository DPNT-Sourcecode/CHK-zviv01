
class CheckoutSolution:
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }

    offers = {
        'A': {
            'count': 3,
            'price': 130
        },
        'B': {
            'count': 2,
            'price': 45
        },
    }

    def total_sku(self, skus, sku) -> int:
        count = skus.count(sku)
        if sku in self.offers.keys() and count % self.offers[sku]['count'] > 0:
            rem = count % self.offers[sku]['count']
            rem_total = rem * self.prices[sku]
            offer_total = count // self.offers[sku]['count'] * self.offers[sku]['price']
            return rem_total + offer_total
        return count * self.prices[sku]

    # skus = unicode string
    def checkout(self, skus):
        total = 0
        for item in self.prices.keys():
            if item in skus:
                total += self.total_sku(skus, item)
        return total


