from NotificationAlertObserver import NotificationAlertObserver

def EmailObserverImpl(NotificationAlertObserver):

    def __init__(self, user_mail=None, observable=None):
        self.user_mail = user_mail
        self.observable = observable

    def update(self):
        print(f"Alert Sent on email, total count: {self.observable.get_data()}")