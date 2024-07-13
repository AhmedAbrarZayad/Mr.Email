import json
import getpass
TO = []
def take_receivers():
    number_of_receivers = int(input("Number_of_receivers: "))
    for i in range(number_of_receivers):
        tmp = input("Receiver's email: ")
        TO.append(tmp)
    with open('receivers.json', 'a') as file:
        json.dump(TO, file)
    print("Receivers saved in receivers.json")
def main():
    take_receivers()
if __name__ == '__main__':
    main()