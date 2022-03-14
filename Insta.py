from instagrapi import Client
import time
import random

comments = ["examplecomment1",
            "examplecomment2",
            "examplecomment3"]

print("Logging in....")
cl = Client()
cl.login("YourUsername", "YourPassword")

while True:
    print("Getting posts")
    medias = cl.hashtag_medias_recent_v1("ChooseAtag", amount=50)
    for media in medias:
        print("Liking...")
        cl.media_like(media.dict()['pk'])
        print("Commenting...")
        cl.media_comment(media.dict()["pk"], random.choice(comments))
        time.sleep(20)




















