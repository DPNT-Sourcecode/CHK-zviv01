
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
        rem_skus = skus
        total = 0
        while len(rem_skus) > 0:
            if rem_skus[0] in self.prices.keys():
                total += self.total_sku(rem_skus, rem_skus[0])
                rem_skus = rem_skus.replace(rem_skus[0], '')
            else:
                return -1                
        return total


