import random

data_dict = {}


def open_data_create_dict():
    with open("all_data.csv", "r", encoding="utf-8") as f:
        data = f.read()
        data = data.split("\n")

    for x in range(len(data) - 1):
        list1 = data[x].split(",")
        data_dict[x] = list1


def get_random_url():
    rand_num = random.randint(0, len(data_dict))
    print(data_dict[rand_num][4])


def main():
    open_data_create_dict()
    while True:
        print("Enter 'r' to get a random URL in the top 3600 repositories on Github:")
        usr_input = input()
        if usr_input == "r":
            get_random_url()
        elif usr_input == "q":
            break


if __name__ == "__main__":
    main()
