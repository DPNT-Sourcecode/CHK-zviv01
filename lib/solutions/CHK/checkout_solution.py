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
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
}

OFFERS = [
    {
        'items': ['A'],
        'required': 3,
        'discounted_price': 130,
    },
    {
        'items': ['A'],
        'required': 5,
        'discounted_price': 200,
    },
    {
        'items': ['B'],
        'required': 2,
        'discounted_price': 45,
    },
    {
        'items': ['E'],
        'required': 2,
        'free_item': 'B',
    },
    {
        'items': ['F'],
        'required': 2,
        'free_item': 'F',
    },
    {
        'items': ['H'],
        'required': 5,
        'discounted_price': 45,
    },
    {
        'items': ['H'],
        'required': 10,
        'discounted_price': 80,
    },
    {
        'items': ['K'],
        'required': 2,
        'discounted_price': 120,
    },
    {
        'items': ['N'],
        'required': 3,
        'free_item': 'M',
    },
    {
        'items': ['P'],
        'required': 5,
        'discounted_price': 200,
    },
    {
        'items': ['Q'],
        'required': 3,
        'discounted_price': 80,
    },
    {
        'items': ['R'],
        'required': 3,
        'free_item': 'Q',
    },
    {
        'items': ['U'],
        'required': 3,
        'free_item': 'U',
    },
    {
        'items': ['V'],
        'required': 2,
        'discounted_price': 90,
    },
    {
        'items': ['V'],
        'required': 3,
        'discounted_price': 130,
    },
    {
        'items': ['S', 'T', 'X', 'Y', 'Z'],
        'required': 3,
        'discounted_price': 45,
    }
]


class CheckoutSolution:

    basket = ''
    total = 0
    
    def count_offer_items(self, offer: dict) -> int:
        return sum([self.basket.count(i) for i in offer['items']])
    
    def calculate_offer_value(self, offer: dict) -> int:
        if 'free_item' in offer.keys():
            return PRICES[offer['free_item']] 
        basket = self.basket
        total = 0
        value_ordered_items = sorted(offer['items'], key=lambda x: PRICES[x], reverse=True)
        required = offer['required']
        while required > 0:
            for item in value_ordered_items:
                if item in basket:
                    basket = basket.replace(item, '', 1)
                    total += PRICES[item]
                    required -= 1
                    break
        return total - offer['discounted_price']

    def can_apply_offer(self, offer: dict) -> bool:
        sku_count = self.count_offer_items(offer)
        if sku_count >= offer['required']:
            if 'free_item' in offer.keys():
                free_item_count = self.basket.count(offer['free_item'])
                if free_item_count > 0:
                    return True
                return False
            return True
        return False
    
    def remove_items_for_offer(self, offer: dict) -> None:
        if len(offer["items"]) == 1:
            self.basket = self.basket.replace(offer['items'][0], '', offer['required'])
        else:
            value_ordered_items = sorted(offer['items'], key=lambda x: PRICES[x], reverse=True)
            required = offer['required']
            while required > 0:
                for item in value_ordered_items:
                    if item in self.basket:
                        print('removing', item)
                        self.basket = self.basket.replace(item, '', 1)
                        required -= 1
                        break


    def find_all_applicable_offers(self) -> list[dict]:
        applicable_offers = [offer for offer in OFFERS if self.can_apply_offer(offer)]
        return sorted(applicable_offers, key=lambda x: self.calculate_offer_value(x), reverse=True)
    
    def apply_offer(self, offer: dict) -> None:
        print("applying offer", offer)
        sku_count = self.count_offer_items(offer)
        div = sku_count // offer['required']
        if div > 0:
            self.remove_items_for_offer(offer)
            if 'free_item' in offer.keys():
                self.total += offer['required'] * PRICES[offer['items'][0]]
                self.basket = self.basket.replace(offer['free_item'], '', 1)
            elif 'discounted_price' in offer.keys():
                self.total += offer['discounted_price']

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        
        if len(skus) == 0:
            return 0
        if set(skus) - set(PRICES.keys()):
            return -1

        self.total = 0
        self.basket = skus

        applicable_offers = self.find_all_applicable_offers()
        while len(applicable_offers) > 0:
            offer = applicable_offers[0]
            if self.count_offer_items(offer) >= offer['required']:
                self.apply_offer(offer)
                applicable_offers = self.find_all_applicable_offers()
            else:
                applicable_offers.remove(offer)
        
        while len(self.basket) > 0:
            item = self.basket[0]
            sku_count = self.basket.count(item)
            self.total += sku_count * PRICES[item]
            self.basket = self.basket.replace(item, '', sku_count)
           
        return self.total

client = CheckoutSolution()
tests = [
    # "",
    # "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ",
    # "LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH", 
    # "PPPPQRUVPQRUVPQRUVSU",
    # "STXYZ",
    "STX",
    "STXSTX",
    "SSS",
    # "FFFF",
    # "FFFFFF",
    # "FFFFFF",
    # "KK",
    # "KKK",
    # "KKKK"
]
for test in tests:
    print(f">>>>>>>>>>>>>>>>Test: {test}")
    print("RESULT = ", client.checkout(test), "<<<<<<<<<<<<<<<<<<")
