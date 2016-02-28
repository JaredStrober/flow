# moving average cross crossovers                
class Indicators():
    def __init__(self, quotes):
        self.quotes = quotes

    def get_quotes(self, sampling=1):
        return self.quotes[0::sampling]

    def moving_average(self, size, sliced):
        return sum(sliced)/size

    def crossover_indicator(self, x, y):
        q = self.quotes
        if self.moving_average(x, q[-x:]) < self.moving_average(y, q[-y:]):
            if self.moving_average(x, q[-x-1:-1]) > self.moving_average(y, q[-y-1:-1]):
                return 1
        elif self.moving_average(x, q[-x:]) > self.moving_average(y, q[-y:]):
            if self.moving_average(x, q[-x-1:-1]) < self.moving_average(y, q[-y-1:-1]):
                return -1
        return 0

    def print_quotes(self):
        print crossover_indicator(5, 10)
    

    
