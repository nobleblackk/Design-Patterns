from Observable.IphoneObservableImpl import IphoneObservableImpl
from Observer.PhoneObserverImpl import PhoneObserverImpl
from Observable.StockObservable import StockObservable





iphoneObservable = IphoneObservableImpl()

iphoneObserver_1 = PhoneObserverImpl(user_name="Abhishek", observable=iphoneObservable)

iphoneObservable.add(iphoneObserver_1)

iphoneObservable.set_data(5)