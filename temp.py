import random
import time

import requests

link = "https://www.swiggy.com/dapi/order/trackV2/de?order_key=afe8153632b43ef90bed62c2c01e55&type=full&version=V2&order_id=*"



def get_cords(n):
    valid = []
    orders = list(range(152529716794, 152529716794+1000))
    failed = 0
    for order in orders[:n]:
        res = requests.get(link.replace("*", str(order)))
        if "Tracking de data not available" in res.text:
            failed += 1
            if failed > 10:
                break
            continue

        temp_dict = res.json()['data']['location']
        temp_dict['size'] = random.randint(1, 20)
        print(temp_dict)
        valid.append(temp_dict)
        print(order)
        time.sleep(0.1)
    return valid

if __name__ == "__main__":
    get_cords(1000)