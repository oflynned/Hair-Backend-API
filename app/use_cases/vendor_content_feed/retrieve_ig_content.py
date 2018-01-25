import requests

from app.use_cases.vendor_content_feed.remote_fetch_exception import RemoteFetchException


class VendorContentFeed:
    @staticmethod
    def get_raw_feed_data():
        url = "https://api.instagram.com/v1/users/1356989103/media/recent?" \
              "client_id=c446f33c3310412887da3479c55e962a&access_token=1356989103.c446f33.f7292ad4733442399c63488d5deda176"

        try:
            raw_data = requests.get(url).json()
        except requests.RequestException:
            raise RemoteFetchException("Instagram request failed", 500)

        return raw_data

    @staticmethod
    def groom_ig_input_data(raw_data):
        output = []

        for item in raw_data["data"]:
            image_data = item["images"]
            caption = item["caption"]["text"]
            tags = item["tags"]
            ig_photo_link = item["link"]

            creation_time = int(item["created_time"])
            ig_username = item["caption"]["from"]["username"]

            output.append({
                "image_data": image_data,
                "caption": VendorContentFeed.remove_hash_tags(caption),
                "tags": tags,
                "creation_time": creation_time,
                "ig_username": ig_username,
                "ig_photo_link": ig_photo_link
            })

        return output

    @staticmethod
    def remove_hash_tags(hashtagged_input):
        output = []
        input = str(hashtagged_input).split(" ")

        for word in input:
            if word[:1] is not "#":
                output.append(word)

        return " ".join(output)
