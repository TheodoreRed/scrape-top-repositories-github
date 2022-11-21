import random
import time
import webbrowser
import os


data_dict = {}
list_topic = []
list_stars = []
list_repos = []
list_username = []
list_urls = []


def open_data_create_dict():
    with open("data_about_repos.csv", "r", encoding="utf-8") as f:
        data = f.read()
        data = data.split("\n")

    for x in range(len(data) - 1):
        list1 = data[x].split(",")
        data_dict[x] = list1

    for x in range(len(data_dict)):
        list_topic.append(data_dict[x][0])
        list_stars.append(data_dict[x][1])
        list_repos.append(data_dict[x][2])
        list_username.append(data_dict[x][3])
        list_urls.append(data_dict[x][4])


def get_random_url():
    rand_num = random.randint(0, len(data_dict))
    print(data_dict[rand_num][4])


def open_random_repo():
    rand_num = random.randint(0, len(data_dict))
    url = data_dict[rand_num][4]
    print("Opening a random repository...")
    time.sleep(1)
    webbrowser.open(url)


def get_top_repo():

    # star_url_dict = {"star": list_stars, "url": list_urls}
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


def search_everything(usr_input):
    for idx, x in enumerate(list_urls):
        if x.__contains__(usr_input.lower()):
            print(list_urls[idx] + " Topic: " + list_topic[idx])


def clear_command_line():
    os.system("cls")


def topic_name_data():
    print("Enter topic name:")
    usr_input = input().upper()
    for idx, x in enumerate(list_topic):
        if x.upper() == usr_input:
            print(list_urls[idx], "has", list_stars[idx], "stars")


def use_the_data():

    while True:
        print(
            "Enter: 'r' for random repo - 'open r' to open a random repo - '1' prints top repo - 'by topic' follow-up search by topic name - 'clear' to clear command line - 'q' to quit"
        )
        print("Or search for anything by name:")
        usr_input = input()
        if usr_input == "r":
            get_random_url()
        elif usr_input == "open r":
            open_random_repo()
        elif usr_input == "1":
            get_top_repo()
        elif usr_input == "by topic":
            topic_name_data()
        elif usr_input == "clear":
            clear_command_line()
        elif usr_input == "q":
            break
        else:
            search_everything(usr_input)
        time.sleep(0.5)


def main():
    open_data_create_dict()
    use_the_data()


if __name__ == "__main__":
    main()
