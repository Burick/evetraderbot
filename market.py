# -*- coding: utf-8 -*-
import requests as req
import time
import urllib.parse
#urllib.parse.quote_plus(query)
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
        # "The Forge":10000002,
    }

    types = {
        "Morphite": 11399,
        "Fullerides": 16679,
        "Fernite Carbide": 16673,

        "Helium Isotopes": 16274,
        "Hydrogen Isotopes": 17889,
        "Nitrogen Isotopes": 17888,
        "Oxygen Isotopes": 17887,

    }

    prices = {}

    burick_type_ids = []
    burick_orders = {}
    # region_id_jita = 10000002

    type_names = [
        # "Customs Office Gantry",
        "Eifyr and Co. \'Alchemist\' Biology BY-805",
        # "Inherent Implants \'Noble\' Repair Systems RS-601",
        "Zainou \'Gypsy\' Signature Analysis SA-701",
        # "Zainou \'Gnome\' Weapon Upgrades WU-1001",
        "Republic Fleet Torpedo Launcher",
        "Republic Fleet 720mm Howitzer Artillery",
        "Republic Fleet 425mm Autocannon",

        # "High-grade Grail Alpha",
        #"High-grade Grail Beta",
        "High-grade Grail Delta",
        # "High-grade Grail Epsilon",
        # "High-grade Grail Gamma",
        # "High-grade Grail Omega",
        # "High-grade Jackal Alpha",
        # "High-grade Jackal Beta",
        # "High-grade Jackal Delta",
        "High-grade Jackal Epsilon",
        "High-grade Jackal Gamma",
        # "High-grade Jackal Omega",
        # "High-grade Spur Alpha",
        "High-grade Spur Beta",
        # "High-grade Spur Delta",
        "High-grade Spur Epsilon",
        # "High-grade Spur Gamma",
        # "High-grade Spur Omega",
        "High-grade Talon Alpha",
        # "High-grade Talon Beta",
        # "High-grade Talon Delta",
        "High-grade Talon Epsilon",
        "High-grade Talon Gamma",
        # "High-grade Talon Omega",
    ]
    
    def __init__(self):
        self.getTypeId()
        pass

    def test(self):
        message = []
        for name, region in self.pers.items():
        # for type_name, type_id in self.types.items():
            type_name = "Morphite"
            type_id = 11399
            region_id =  self.regions[region]
            url =  f' https://esi.evetech.net/latest/markets/{region_id}/orders/?&order_type=buy&type_id={type_id}'
            resp = req.get(url)
            orders = resp.content
            if self.prices.get(name) != orders:
                self.prices[name] = orders
                # print('Изменение', name, ' - ', region)
                message.append(f'Изменение {name} - {region} - {type_name}\n')

        message = ''.join(message)
        if message:
            return message
        else:
            return False

    def getBuricklOrders(self):
        msg = []
        region_id = 10000002 # The Forge Jita
        for item in self.burick_type_ids:
            url =  f' https://esi.evetech.net/latest/markets/{region_id}/orders/?&order_type=buy' \
                   f'&type_id={item["typeID"]}'

            order = req.get(url).content
            if self.burick_orders.get(item['typeName']) != order:
                self.burick_orders[item['typeName']] = order
                msg.append(f'Изменение {item["typeName"]}\n')
                # print(item['typeID'], ' - ', item['typeName'])
        msg = ''.join(msg)
        if msg:
            return msg
        else:
            return False

    def getTypeId(self):
        query_string = urllib.parse.quote_plus('|'.join(self.type_names))
        try:
            self.burick_type_ids = req.get(f'https://www.fuzzwork.co.uk/api/typeid2.php?typename={query_string}').json()
        except:
            self.burick_type_ids = False
        return self.burick_type_ids

        pass

market = Market()
def run():
    while True:
        burick_orders = market.getBuricklOrders()
        if burick_orders:
            print(burick_orders)
        time.sleep(60)
    pass


def main():
    run()


if __name__ == '__main__':
    main()
