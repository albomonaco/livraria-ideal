import requests

def get_book_information(isbn_list:list):
    dict_isbn = {}
    for isbn in isbn_list:
        response = requests.get("https://openlibrary.org/isbn/{}.json".format(str(isbn)))
        if "<!DOCTYPE html>" in response.text:
            dict_isbn[str(isbn)] = "Cadastrar na mão"
        else:
            dict_isbn[str(isbn)] = response.text
    return dict_isbn


if __name__ == "__main__":
    print(get_book_information([9788530805098, 9788574903163,9788530807436]))
