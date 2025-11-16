import requests

def fetch_posts(limit=50):
    url = "https://hacker-news.firebaseio.com/v0/topstories.json" # This is the url of the top stories in Hacker News for fetching purposes.
    ids = requests.get(url).json() # This is the json response of the top stories.

    cs_stories = [] # Empty list to store the CS Stories.

    for pid in ids[:limit]: # Loop through the top stories and store the CS stories in the cs_stories list.
        item = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{pid}.json").json() # This line fetches each individual story by its ID and stores it in the item variable.
        if item and "title" in item: # This checks if the item exists and has a title.
            title = item["title"].lower() # This converts the title to lowercase for easier keyword matching.

            if "research" in title or "ai" in title or "computer" in title or "machine" in title or "learning" in title or "deep" in title: # This filters the posts by having keywords.
                cs_stories.append(item) # This appends the story to the cs_stories list.

    return cs_stories # Returns the list of CS stories.

# This block runs only if the file is executed directly (not imported as a module)
if __name__ == "__main__":

    # Fetch the top 100 stories and filter them for CS-related content
    stories = fetch_posts(100)

    # Print the title of each CS-related story
    for s in stories:
        print(s["title"])

