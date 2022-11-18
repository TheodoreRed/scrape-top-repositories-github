import os


def read_text_file(file_path):
    with open(file_path, "r") as f:
        csv_file = f.read()
        return csv_file


def create_list_paths():
    path = "/Users/19063/OneDrive/Desktop/Jovian/Python_Web_Scraper/data"
    os.chdir(path)

    csv_file_path_list = []
    for file in os.listdir():
        if file.endswith(".csv"):
            csv_file_path = f"{path}/{file}"
            csv_file_path_list.append(csv_file_path)
    return csv_file_path_list


csv_file_path_list = create_list_paths()
print(read_text_file(csv_file_path_list[1]))

# TODO: returns a random topics URL
def get_random_topic_url():
    pass
