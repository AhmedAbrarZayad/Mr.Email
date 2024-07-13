import json
import getpass


def take_sender():
    data = {}
    FROM = input("Sender's email: ")
    data['FROM'] = FROM
    PASS = getpass.getpass("Sender's Google App Password: ")
    data['PASS'] = PASS
    with open('senders.json','w') as file:
        json.dump(data, file)
    print("Sender saved in senders.json")

def main():
    take_sender()


if __name__ == '__main__':
    main()