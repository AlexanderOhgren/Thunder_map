from twilio.rest import Client
import time
import dependencies.keys as keys, dependencies.my_data as my_data

client = Client(keys.ACCOUNT_SID, keys.AUTH_TOKEN)

def create_message(key, value):
    message = client.messages.create(
        body=f"the risk for thunder is: {value}% on this day: {key}",
        from_= keys.TWILIO_NUMBER,
        to= keys.TARGET_NUMBER
    )
    print (message.body)

def check_data():
    while True:
        data = my_data.get_thunder_data()
        for key, value in data.items():
            if value[0] >= 4:
                create_message(key, value[0])
        time.sleep(14400)

if __name__ == "__main__":
    check_data()