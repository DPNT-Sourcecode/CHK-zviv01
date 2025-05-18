
class CheckoutSolution:
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
    }

    offers = {
        'A': [
            {
                'count': 5,
                'price': 200
            },
            {
                'count': 3,
                'price': 130
            },
        ],
        'B': [
            {
                'count': 2,
                'price': 45
            }
        ],
    }

    def apply_offers(self, skus, sku) -> int:
        total = 0
        rem_skus = skus.count(sku)
        for offer in self.offers[sku]:
            div = rem_skus // offer['count']
            if div > 0:
                total += div * offer['price']
                rem_skus = rem_skus % offer['count']
        return total + rem_skus * self.prices[sku]
                

    def total_sku(self, skus, sku) -> int:
        count = skus.count(sku)
        if sku in self.offers.keys():
            return self.apply_offers(skus, sku)
        return count * self.prices[sku]

    # skus = unicode string
    def checkout(self, skus) -> int:
        e_count = skus.count('E')
        if e_count > 1:
            div = e_count // 2
            skus = skus.replace('B', '', div)

        rem_skus = skus
        total = 0
        while len(rem_skus) > 0:
            if rem_skus[0] in self.prices.keys():
                total += self.total_sku(rem_skus, rem_skus[0])
                rem_skus = rem_skus.replace(rem_skus[0], '')
            else:
                return -1                
        return total

# client = CheckoutSolution()
# print(client.checkout("EEB"))




