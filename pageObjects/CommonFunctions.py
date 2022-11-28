class CommonFunctions:

    def __init__(self, driver):
        self.driver = driver

    def convertPriceIntoInteger(self, price_string):  # Converts string from integer like
        price_string = price_string.replace(',', '')    # ex- In Amazon page,price is converted from 12,999 t0 12999
        price_integer = int(price_string)
        return price_integer
