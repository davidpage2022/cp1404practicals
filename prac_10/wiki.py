import wikipedia

query = input("Enter page title or search phrase: ")
while query:
    try:
        page = wikipedia.page(query)  # auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
        # print(wikipedia.summary(query))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    query = input("Enter page title or search phrase: ")
