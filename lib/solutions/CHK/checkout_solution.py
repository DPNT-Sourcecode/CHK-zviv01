
class CheckoutSolution:
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
    }

    discount = {
        'A': [
            {
                'count': 5,
                'price': 200
            },
            {
                'count': 3,
                'price': 130
            }
        ],
        'B': [
            {
                'count': 2,
                'price': 45
            }
        ],
        'F': [
            {
                'count': 3,
                'price': 20
            }
        ],
        'H': [
            {
                'count': 5,
                'price': 45
            },
            {
                'count': 10,
                'price': 80
            }
        ],
        'K': [
            {
                'count': 2,
                'price': 150
            }
        ],
        'P': [
            {
                'count': 5,
                'price': 200
            }
        ],
        'Q': [
            {
                'count': 3,
                'price': 80
            }
        ],
        'V': [
            {
                'count': 2,
                'price': 90
            },
            {
                'count': 3,
                'price': 130
            }
        ]
    }

    free = {

    }

    def apply_discount(self, skus, sku) -> int:
        total = 0
        rem_skus = skus.count(sku)
        for discount in self.discount[sku]:
            div = rem_skus // discount['count']
            if div > 0:
                total += div * discount['price']
                rem_skus = rem_skus % discount['count']
        return total + rem_skus * self.prices[sku]
                

    def total_sku(self, skus, sku) -> int:
        count = skus.count(sku)
        if sku in self.discount.keys():
            return self.apply_discount(skus, sku)
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
# print(client.checkout("EEBFFFFFF"))
