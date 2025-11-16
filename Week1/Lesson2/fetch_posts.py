import requests
import json
import re

KEYWORDS = ["research", "ai", "computer", "machine", "learning", "deep", "neural", "algorithm", "data", "network", "model"]


def fetch_posts(limit=50):
    url = "https://hacker-news.firebaseio.com/v0/topstories.json" # This is the url of the top stories in Hacker News for fetching purposes.
    ids = requests.get(url).json() # This is the json response of the top stories.

    cs_stories = [] # Empty list to store the CS Stories.

    for pid in ids[:limit]: # Loop through the top stories and store the CS stories in the cs_stories list.
        item = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{pid}.json").json() # This line fetches each individual story by its ID and stores it in the item variable.
        if item and "title" in item: # This checks if the item exists and has a title.
            title = item["title"].lower() # This converts the title to lowercase for easier keyword matching.

            if any(re.search(rf"\b{keyword}\b", title) for keyword in KEYWORDS): # This filters the posts by having keywords and making sure there are no false positives.
                cs_stories.append(item) # This appends the story to the cs_stories list.

    return cs_stories # Returns the list of CS stories.

def save_to_json(data, filename="stories.json"):
    with open(filename, "w") as f: # Opens the file in write mode.
        json.dump(data, f, indent=4) # Dumps the data to the file in JSON format with indentation for readability.
    print(f"Saved {len(data)} items to {filename}") # Prints a message indicating how many items were saved and to which file.

def load_from_json(filename="stories.json"): # Loads data from a JSON file.
    with open(filename, "r") as f: # Opens the file in read mode.
        return json.load(f) # Loads the data from the file.


# This block runs only if the file is executed directly (not imported as a module)
if __name__ == "__main__":
    USE_CACHE = False  # Set to True to load from cache, False to fetch fresh data
    if USE_CACHE:
        stories = load_from_json()
        print(f"Loaded {len(stories)} items from cache")
    else:
        stories = fetch_posts(100)
        save_to_json(stories)
    # Fetch the top 100 stories and filter them for CS-related content

    # Print the title of each CS-related story
    for s in stories:
        print(s["title"])



