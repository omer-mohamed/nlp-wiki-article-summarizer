import json
import wikipedia


data = []

with open("animals.txt") as f:
    for title in f:
        title = title.strip()
        print(title)
        try:
            page = wikipedia.page(title + " Animal")
            summary = page.summary
            content = page.content.split("== References ==")[0].split("== See also ==")[0].split("== Footnotes ==")[0]
            
            data.append({
                "title": title,
                "summary": summary,
                "content": content
            })
            
        except wikipedia.exceptions.PageError as e:
            print(f"Page not found: {title}")

with open("output.json", "w") as f:
    json.dump(data, f)