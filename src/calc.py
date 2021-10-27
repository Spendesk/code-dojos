from functools import reduce
from decimal import Decimal
def add(arg1=None):
    if arg1=="":
        return "0"

    string_with_commas = arg1.replace('\n', ',')
    double_comma = string_with_commas.find(",,")
    list_args = string_with_commas.split(',')
    if not double_comma == -1:
        return f"Number expected but '{arg1[double_comma+1]}' found at position {double_comma+1}."

    list_dec = [Decimal(u) for u in list_args]
    return str(sum(list_dec))
    


