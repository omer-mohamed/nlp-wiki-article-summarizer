import json
import wikipedia


data = []

with open("test.txt") as f:
    for title in f:
        title = title.strip()
        try:
            page = wikipedia.page(title + " Animal")
            summary = page.summary
            content = page.content.split("== References ==")[0].split("== See also ==")[0].split("== Footnotes ==")[0]
            
            data = {
                "title": title,
                "summary": summary,
                "content": content
            }

            # Do something with the data
            
        except wikipedia.exceptions.PageError as e:
            print(f"Page not found: {title}")

with open("output.json", "w") as f:
    json.dump(data, f)