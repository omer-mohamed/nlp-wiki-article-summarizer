import json
import wikipedia

data = []

with open("test.txt") as f:
    for title in f:
        title = title.strip()
        page = wikipedia.page(title + " Animal")
        summary = page.summary
        content = page.content.split("== References ==")[0].split("== See also ==")[0].split("== Footnotes ==")[0]

        data.append({
            "title": title,
            "summary": summary,
            "content": content
        })

with open("output.json", "w") as f:
    json.dump(data, f)