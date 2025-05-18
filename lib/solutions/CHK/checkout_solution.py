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

offers = [
    {
        'item': 'A',
        'required': 3,
        'discounted_price': 130
    },
    {
        'item': 'A',
        'required': 5,
        'discounted_price': 200
    },
    {
        'item': 'B',
        'required': 2,
        'discounted_price': 45
    },
    {
        'item': 'E',
        'required': 2,
        'free_item': 'B'
    },
    {
        'item': 'F',
        'required': 2,
        'free_item': 'F'
    },
    {
        'item': 'H',
        'required': 5,
        'discounted_price': 45
    },
    {
        'item': 'H',
        'required': 10,
        'discounted_price': 80
    },
    {
        'item': 'K',
        'required': 2,
        'discounted_price': 150
    },
    {
        'item': 'N',
        'required': 3,
        'free_item': 'M'
    },
    {
        'item': 'P',
        'required': 5,
        'discounted_price': 200
    },
    {
        'item': 'Q',
        'required': 3,
        'discounted_price': 80
    },
    {
        'item': 'R',
        'required': 3,
        'free_item': 'Q'
    },
    {
        'item': 'U',
        'required': 3,
        'free_item': 'U'
    },
    {
        'item': 'V',
        'required': 2,
        'discounted_price': 90
    },
    {
        'item': 'V',
        'required': 3,
        'discounted_price': 130
    },
]


class CheckoutSolution:

    total: int = 0

    class Item:
        count: int

    def offers_sorted_by_required(self, input_offers: list[dict]) -> list[dict]:
        return sorted(input_offers, key=lambda x: x['required'], reverse=True)
    
    def remove_unrelated_offers(self, skus) -> list[dict]:
        return [offer for offer in self.offers if offer['item'] in skus]


    def apply_discount(self, skus, sku) -> int:
        total = 0
        rem_skus = skus.count(sku)
        for discount in self.discount[sku]:
            div = rem_skus // discount['count']
            if div > 0:
                total += div * discount['price']
                rem_skus = rem_skus % discount['count']
        return total + rem_skus * self.prices[sku]
    
    def apply_discount(self, item, offer):
        pass
                

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
# offers = client.remove_unrelated_offers('ABCDH')
# print(client.offers_sorted_by_required(offers))




