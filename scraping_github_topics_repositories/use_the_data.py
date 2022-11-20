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


def get_top_repo():
    list_stars = []
    list_urls = []
    for x in range(len(data_dict)):
        list_stars.append(data_dict[x][1])
        list_urls.append(data_dict[x][4])

    star_url_dict = {"star": list_stars, "url": list_urls}
    bigNum = 0
    for idx, num in enumerate(list_stars):
        if int(num) > bigNum:
            bigNum = int(num)
            bigNumid = idx
    print(
        "With "
        + str(bigNum)
        + " stars, the most popular repository on Github is "
        + list_urls[bigNumid]
    )


def get_top_10_topics():
    pass


def use_the_data():
    while True:
        print(
            "Enter 'r' to get a random URL or '1' to get top repository in the top 3600 repositories on Github:"
        )
        usr_input = input()
        if usr_input == "r":
            get_random_url()
        elif usr_input == "1":
            get_top_repo()
        elif usr_input == "q":
            break


def main():
    open_data_create_dict()
    use_the_data()


if __name__ == "__main__":
    main()
