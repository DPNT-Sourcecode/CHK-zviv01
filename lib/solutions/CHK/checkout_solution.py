PRICES = {
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

OFFERS = [
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

    basket = ''
    total = 0

    def sort_basket(self) -> None:
        self.basket = ''.join(sorted(self.basket, key=self.basket.count, reverse=True))
        print("sorted basket", self.basket)

    def remove_unrelated_offers(self, skus) -> list[dict]:
        remaining_offers = [offer for offer in OFFERS if offer['item'] in skus]
        return sorted(remaining_offers, key=lambda x: x['required'], reverse=True)   
    
    def apply_offer(self, offer: dict) -> None:
        print("applying offer", offer)
        sku_count = self.basket.count(offer['item'])
        div = sku_count // offer['required']
        if div > 0:
            self.basket = self.basket.replace(offer['item'], '', offer['required'])
            if 'free_item' in offer.keys():
                print("free item")
                self.total += offer['required'] * PRICES[offer['item']]
                self.basket = self.basket.replace(offer['free_item'], '', 1)
            elif 'discounted_price' in offer.keys():
                print("discounted price")
                self.total += offer['discounted_price']
            print("remaining", self.basket)
            print("total", self.total)

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        
        if len(skus) == 0:
            return 0
        self.total = 0
        self.basket = skus
        self.sort_basket()

        sorted_offers = self.remove_unrelated_offers(skus)
        
        
        while len(self.basket) > 0:
            item = self.basket[0]
            if item in PRICES.keys():
                if item in [offer['item'] for offer in sorted_offers]:
                    for offer in sorted_offers:
                        if offer['item'] == item:
                            self.apply_offer(offer)
                            break
                else:
                    sku_count = self.basket.count(item)
                    self.total += sku_count * PRICES[item]
                    self.basket = self.basket.replace(item, '', sku_count)
            else:
                return -1                
        return self.total

client = CheckoutSolution()
tests = ["FFFF", "FFFFF", "FFFFFF"]
for test in tests:
    print(f"Test: {test}")
    print("RESULT = ", client.checkout(test))

