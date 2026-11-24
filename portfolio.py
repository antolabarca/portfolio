class Stock:

    """
    Represents a possible Stock

    Attributes:
    name (str) : the name of the company
    __price (num) : the current price of one stock
    """

    def __init__(self, name, current_price):
        self.name = name
        self.__price = current_price

    @property
    def current_price(self):
        return self.__price

    @current_price.setter
    def current_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = new_price


class Portfolio:

    """
    Represents one person's portfolio of stocks

    Attributes:
    __stocks (dict) : a dictionary with keys corresponding to a Stock and values
                    corresponding to amount of each stock in the portfolio
    __allocated (dict) : a dictionary with keys corresponding to a Stock and values 
                    corresponding to allocated/target amount of each stock
    """

    def __init__(self, allocated):
        """
        Initializes a portfolio with no stocks and an allocated target
        
        Args:
        allocated (dict) : the allocated target

        Raises:
        ValueError if allocated doesn't add up to 100
        """
        if sum(allocated.values())!=100:
            raise ValueError("allocated must add up to 100%")
        self.__stocks = {}
        self.__allocated = allocated

    def add_stocks(self, stock, n):
        """
        Adds n stocks of a specific type to the portfolio
        
        Args:
        stock (Stock) : the stock to be added
        n (int) : the amount

        Raises: 
        ValueError if n is negative
        """
        if n < 0:
            raise ValueError("n cannot be negative")
        if stock not in self.__stocks:
            self.__stocks[stock] = 0
        self.__stocks[stock] += n
            

    def remove_stocks(self, stock, n):
        """
        Removes n stocks of a specific type from the portfolio (if possible)
        
        Args:
        stock (Stock) : the stock to be removed
        n (int) : the amount

        Raises:
        ValueError if n is more than the available stocks
        KeyError if stock is not in the portfolio
        """
        if stock not in self.__stocks:
            raise KeyError("stock not in the portfolio")
        if n > self.__stocks[stock]:
            raise ValueError("n cannot be more than available stock")
        self.__stocks[stock] -= n

    def find_balance(self):
        """
        Finds which stocks must be sold and which must be bought to achieve the balance 
        given by __allocated, assuming the same amount of stocks must remain in the end

        Returns:
        array of strs giving the information
        """
        current_amount = sum(self.__stocks.values()) # the current amount of stocks
        current_percent = {k: v*100/current_amount for k, v in self.__stocks.items()} # an array of percentages of each stock

        ans = []

        for i in self.__stocks.keys():
            if i not in self.__allocated:
                ans.append(f"sell all {i.name}\n")
            else:
                dif = current_percent[i] - self.__allocated[i]
                amount = dif*current_amount/100
                print(amount)
                if amount > 0:
                    ans.append(f"sell {amount} {i.name}\n")
                elif amount < 0:
                    ans.append(f"buy {amount*-1} {i.name}\n")
                else:
                    ans.append(f"{i.name} is OK")

        for i in self.__allocated.keys() - self.__stocks.keys():
            amount = self.__allocated[i]*current_amount
            ans.append(f"buy {amount} {i.name}\n")

        return ans
