# Lesson 1 — Fetching data from an API

This lesson covers the basics of fetching data from a public API and filtering results in Python. The example uses the Hacker News API (maintained by Y Combinator) which does not require authentication for the endpoints we use.

API used

- Top stories endpoint: https://hacker-news.firebaseio.com/v0/topstories.json
- Item endpoint (per story): https://hacker-news.firebaseio.com/v0/item/<id>.json

About the project (fetch_posts.py)

This lesson includes a small utility script, `fetch_posts.py`, which demonstrates a minimal real-world pattern:

- Fetch a list of top story IDs from Hacker News.
- Request each story's full item data by ID.
- Filter stories for CS-related content by matching keywords in the title.
- Return a list of matching story objects.

Quick summary (contract)

- Inputs: `limit` (int, optional) — number of top stories to examine (default: 50).
- Output: `List[dict]` — list of Hacker News item objects (as returned by the API) that matched the keyword filter.
- Error modes: network failures (requests.exceptions), malformed responses (None or missing keys). The script does not currently retry or persist failures.

How it works (implementation notes)

- The script hits the top stories endpoint to obtain an array of story IDs.
- For the first `limit` IDs it fetches each item and checks `item["title"]`.
- Title matching is done by converting to lowercase and checking for keywords such as "research", "ai", "computer", "machine", "learning", and "deep".

Dependencies

- Python 3.7+
- requests (install with `pip install requests`)

Usage

- From the command line (quick run):

  python fetch_posts.py

  This runs the script as a program which prints matching story titles to stdout.

- As a module (programmatic):

  from fetch_posts import fetch_posts
  stories = fetch_posts(limit=100)

  `stories` will be a list of dictionaries (Hacker News items). Each item can contain fields such as `id`, `title`, `by`, `url`, `score`, and `time` depending on the story.

Example output (titles only)

- The script prints one title per line when executed directly. Example (truncated):

  Deep Learning for X: an overview
  New research shows ...
  The future of machine learning in Y

Edge cases and notes

- Rate limiting: the script does many requests (one per story ID). For larger `limit` values this can be slow and may stress the API. Consider batching, sleeping between requests, or using a single thread pool for concurrency.
- Missing fields: some items might be deleted or missing `title`. The script currently ignores such items.
- Network errors: the script will raise exceptions from `requests` if the network is down. You may want to add try/except and retries for robustness.
- Keyword filtering: currently uses a small static keyword list. You can improve it via regular expressions, stemming, or a more advanced classifier.



What's next

- Storing the data into an actual database.
- 
- 
- 

(Leave this section empty for you to fill with tasks, reminders, or learning goals.)
