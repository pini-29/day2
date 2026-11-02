#2
def add_price(total, price):
    return total+price
print(add_price(10,30))
#3
TAX = 1.17
def apply_tax(prices):
    result = []
    for i in prices:
        result.append(i*TAX)
    return result
prices = [100, 50]
with_tax = apply_tax(prices)
print(prices)
print(with_tax)
#4
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total
def show_total(prices):
    print("total:" ,calculate_total(prices))
show_total([10, 20, 30])    

