from Observable.StockObservable import *

class IphoneObservableImpl(StockObservable):

    def __init__(self, stock=0):
        self.observable_list = []
        self.stock = stock 
    
    def add(self, observable):
        self.observable_list.append(observable)
    
    def remove(self, observable):
        self.observable_list.pop(observable)

    def notify(self):
        for observable in self.observable_list:
            observable.update()
    
    def get_data(self):
        return self.stock 
    
    def set_data(self, stock):
        self.stock = stock 
        self.notify()

