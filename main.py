from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

L = instaloader.Instaloader()

posts = instaloader.Profile.from_username(L.context, "danaherjohn").get_posts()

SINCE = datetime(2022, 5, 1)
UNTIL = datetime(2022, 3, 1)

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    L.download_post(post, "instagram")

# instaloader --login azuretaol546 --password death34server --no-pictures --no-videos --no-metadata-json danaherjohn