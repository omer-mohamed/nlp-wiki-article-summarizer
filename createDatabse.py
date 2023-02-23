import csv
import wikipedia
import re

data = []

def getData():
    with open("animals.txt") as f:
        for title in f:
            title = title.strip()
            print(title)
            try:
                page = wikipedia.page(title + " Animal")
                summary = cleanData(page.summary)
                content = cleanData(
                    page.content.split("== References ==")[0]
                    .split("== See also ==")[0]
                    .split("== Footnotes ==")[0]
                    .split("== Further Readings ==")[0]
                )

                data.append({"title": title, "summary": summary, "content": content})

            except wikipedia.exceptions.PageError as e:
                print(f"Page not found: {title}", e)


def cleanData(data):
    clean_data = re.sub("==\s*[\w\s]*\s*==", "", data)
    clean_data = re.sub(r"\([^)]*\)", "", clean_data)
    clean_data = re.sub("-", " ", clean_data)
    clean_data = re.sub("[^a-zA-Z0-9\s-]", "", clean_data)
    clean_data = re.sub("(\-\s+)", " ", clean_data)
    clean_data = re.sub("(\:\s+)", " ", clean_data)
    clean_data = re.sub("\s+", " ", clean_data).strip()

    return clean_data.lower()

def writeCSV(data):
    with open("output.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "content", "summary"])

        for obj in data:
            writer.writerow([obj["title"], obj["content"], obj["summary"]])

getData()
writeCSV(data)
