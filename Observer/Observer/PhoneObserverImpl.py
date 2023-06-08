from Observer.NotificationAlertObserver import *

class PhoneObserverImpl(NotificationAlertObserver):

    def __init__(self, user_name=None, observable=None):
        self.user_name = user_name
        self.observable = observable

    def update(self):
        print(f"Alert Sent on mobile, total count: {self.observable.get_data()}")