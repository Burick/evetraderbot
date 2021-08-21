# -*- coding: utf-8 -*-
import requests as req
import time

class Market:
    pers = {
        "Karabasovich": "Derelik",
        "LenaBu": "Heimatar",
        "Radigostiya": "Devoid",
        "Radigost": "Metropolis",
        "TimeUpEve": "Solitude",
        "Amarrka": "Khanid",

        "Kor": "Kor-Azor",
        "Ari": "Aridia",
    }
    regions = {
        "Derelik": 10000001,
        "Heimatar": 10000030,
        "Devoid": 10000036,
        "Metropolis": 10000042,
        "Solitude": 10000044,
        "Khanid": 10000049,

       "Kor-Azor": 10000065,
        "Aridia": 10000054,
    }

    items = {
        "Morphite": 11399,
        "Fullerides": 16679,
        "Fernite Carbide": 16673,

        "Helium Isotopes": 16274,
        "Hydrogen Isotopes": 17889,
        "Nitrogen Isotopes": 17888,
        "Oxygen Isotopes": 17887,

    }

    prices = {}
    
    def __init__(self):
        pass

    def test(self):
        message = []
        for name, region in self.pers.items():

            type_id = 11399
            region_id =  self.regions[region]
            url =  f' https://esi.evetech.net/latest/markets/{region_id}/orders/?&order_type=buy&type_id={type_id}'
            resp = req.get(url)
            orders = resp.content
            if self.prices.get(name) != orders:
                self.prices[name] = orders
                print('Изменение', name, ' - ', region)
                message.append(f'Изменение {name} - {region}')
        message = ''.join(message)
        if message:
            return message
        else:
            return False

        pass

market = Market()
def run():
    while True:
        result = market.test()
        time.sleep(60)
    pass


def main():
    run()


if __name__ == '__main__':
    main()
