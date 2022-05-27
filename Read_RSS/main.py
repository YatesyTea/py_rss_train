import feedparser

# Making connection to the RSS
NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

# Taking a Singular Entry
entry = NewsFeed.entries[1]

# Printing
print(f"{entry.published}\n---\n{entry.summary}\n--\nLink: {entry.link}")
