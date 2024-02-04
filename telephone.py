import webbrowser
import json

def search_browser():

    #ask for parameters and change spaces to dash
    input_search = input("What do you want to search? ")
    input_search_url = input_search.replace(' ', '-').lower()

    #make a url variable to include search criteria
    search_url = f'https://www.google.com/search?q={input_search_url}'

    #opens the browser with search criteria
    webbrowser.open(search_url)


    #adds search history to a json file
    with open('search_history.json', 'a') as search_object:
        json.dump({'Search': input_search, 'URL': search_url} , search_object)
        search_object.write("\n") 



search_browser()
