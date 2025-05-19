from collections import Counter

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
        'discounted_price': 130,
        'offer_value': 20
    },
    {
        'item': 'A',
        'required': 5,
        'discounted_price': 200,
        'offer_value': 50
    },
    {
        'item': 'B',
        'required': 2,
        'discounted_price': 45,
        'offer_value': 15
    },
    {
        'item': 'E',
        'required': 2,
        'free_item': 'B',
        'offer_value': 30
    },
    {
        'item': 'F',
        'required': 2,
        'free_item': 'F',
        'offer_value': 10
    },
    {
        'item': 'H',
        'required': 5,
        'discounted_price': 45,
        'offer_value': 5
    },
    {
        'item': 'H',
        'required': 10,
        'discounted_price': 80,
        'offer_value': 20
    },
    {
        'item': 'K',
        'required': 2,
        'discounted_price': 150,
        'offer_value': 10
    },
    {
        'item': 'N',
        'required': 3,
        'free_item': 'M',
        'offer_value': 15
    },
    {
        'item': 'P',
        'required': 5,
        'discounted_price': 200,
        'offer_value': 50
    },
    {
        'item': 'Q',
        'required': 3,
        'discounted_price': 80,
        'offer_value': 10
    },
    {
        'item': 'R',
        'required': 3,
        'free_item': 'Q',
        'offer_value': 30
    },
    {
        'item': 'U',
        'required': 3,
        'free_item': 'U',
        'offer_value': 40
    },
    {
        'item': 'V',
        'required': 2,
        'discounted_price': 90,
        'offer_value': 10
    },
    {
        'item': 'V',
        'required': 3,
        'discounted_price': 130,
        'offer_value': 20
    },
]


class CheckoutSolution:

    basket = ''
    total = 0

    def sort_basket(self) -> None:
        applicable_offer_items = [offer['item'] for offer in OFFERS if self.can_apply_offer(offer)]

        offer_basket = ''.join([item for item in self.basket if item in applicable_offer_items])
        sorted_offer_basket = ''.join([item for items, c in Counter(offer_basket).most_common() for item in [items] * c])
        
        non_offer_basket = ''.join([item for item in self.basket if item not in applicable_offer_items])
        sorted_non_offer_basket = ''.join([item for items, c in Counter(non_offer_basket).most_common() for item in [items] * c])
        
        self.basket = sorted_offer_basket + sorted_non_offer_basket
        print("sorted basket", self.basket)

    def can_apply_offer(self, offer: dict) -> bool:
        sku_count = self.basket.count(offer['item'])
        if sku_count >= offer['required']:
            if 'free_item' in offer.keys():
                free_item_count = self.basket.count(offer['free_item'])
                if free_item_count > 0:
                    return True
                return False
            
            return True
        return False
    
    def find_applicable_offers(self, item: str) -> list[dict]:
        item_offers = [offer for offer in OFFERS if offer['item'] == item and self.can_apply_offer(offer)]
        return sorted(item_offers, key=lambda x: x['required'], reverse=True)

    def find_all_applicable_offers(self) -> list[dict]:
        applicable_offers = [offer for offer in OFFERS if self.can_apply_offer(offer)]
        return sorted(applicable_offers, key=lambda x: x['offer_value'], reverse=True)
    
    def apply_offer(self, offer: dict) -> None:
        print("applying offer", offer)
        sku_count = self.basket.count(offer['item'])
        div = sku_count // offer['required']
        if div > 0:
            self.basket = self.basket.replace(offer['item'], '', offer['required'])
            if 'free_item' in offer.keys():
                self.total += offer['required'] * PRICES[offer['item']]
                self.basket = self.basket.replace(offer['free_item'], '', 1)
            elif 'discounted_price' in offer.keys():
                self.total += offer['discounted_price']
            print("total", self.total)

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        
        if len(skus) == 0:
            return 0
        if set(skus) - set(PRICES.keys()):
            return -1

        self.total = 0
        self.basket = skus
        self.sort_basket()

        applicable_offers = self.find_all_applicable_offers()
        while len(applicable_offers) > 0:
            offer = applicable_offers[0]
            if offer['item'] in self.basket:
                self.apply_offer(offer)
                self.sort_basket()
                applicable_offers = self.find_all_applicable_offers()
            else:
                applicable_offers.remove(offer)
        
        while len(self.basket) > 0:
            item = self.basket[0]
            sku_count = self.basket.count(item)
            self.total += sku_count * PRICES[item]
            self.basket = self.basket.replace(item, '', sku_count)
            self.sort_basket()
           
        return self.total

# client = CheckoutSolution()
# tests = [
#     "",
#     "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ",
#     "LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH", 
#     "PPPPQRUVPQRUVPQRUVSU"
# ]
# for test in tests:
#     print(f"Test: {test}")
#     print("RESULT = ", client.checkout(test))