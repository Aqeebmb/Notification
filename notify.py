import time
from plyer import notification

# setting condition
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "take a break it has been an hour",
            timeout =10

        )
        time.sleep(3600)
