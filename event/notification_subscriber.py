
class NotificationSubscriber:
     
     def handle_event(self, event_type, data=None):
        if event_type == 'stream':
            print(data)
