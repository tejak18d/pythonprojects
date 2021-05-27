"""
This script is helpful if you have a lot of bookmark folders in chrome and often have a tough time finding a URL in all the folders.
This search is case insensitive.
To run this script, please do 'pip install chrome-bookmarks' (without the quotes) on the terminal in PyCharm.
Search for a bookmark name, even if you know only a part of the name and it will give you all corresponding URLs associated with the bookmark name.
"""
import chrome_bookmarks

def chrome_bookmark_finder(keyword):
    bookmarks_dict = {}

    # Getting all the bookmark names and URLs and storing them in a dictionary
    for url in chrome_bookmarks.urls:
        bookmarks_dict.update({url.name:url.url})

    print("The list of bookmarks are: " + str(bookmarks_dict))

    # Searching (case insensitive) for the keyword (bookmark name) in the dictionary (bookmarks)
    res = [val for key, val in bookmarks_dict.items() if keyword.lower() in key.lower()]

    # Printing URLs that match with the search keyword
    print(f'URLs that match with {keyword.upper()} are : {str(res)}')

def main():
    keyword = input("Search for a bookmarked URL with a keyword: ")
    chrome_bookmark_finder(keyword)

if __name__ == '__main__':
    main()