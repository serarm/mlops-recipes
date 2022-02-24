"""
This module is used to calculate the free gift cost
This is my solution.
Author: Serjesh
Date: 2/24/2022
"""

import numpy as np


def calculate_total_price(gift_file_pth, gift_limit, tax):
    """
    This function use to calculate the the price of total gift
    Argument:
    gift_file_pth->string: Filename with gift name
    gift_limit->int: Price below which gift is free to customer
    tax->int: Tax over price of gift
    Returns ->int:
    total_price : Cost of total free gift
    """

    with open(gift_file_pth,encoding='utf8') as file_pth:
        gift_costs = file_pth.read().split('\n')

    gift_costs = np.array(gift_costs).astype(int)  # convert string to int
    total_price = (gift_costs[gift_costs < gift_limit]
                   ).sum() * (1 + float(tax / 100))
    return total_price


if __name__ == "__main__":
    TOTAL_PRICE = calculate_total_price('gift_costs.txt', 25, 8)
    print(TOTAL_PRICE)
