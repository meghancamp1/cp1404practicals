import wikipedia
search_input = str(input("Enter a page title or search phrase: "))
while search_input != "":

    try:
        page = wikipedia.page(search_input)
        summary = wikipedia.summary(page)
        print(page.title)
        print(summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Ambiguous page, please specify from the following: ")
        print(e.options)
    search_input = input("Enter a page title or search phrase: ")
