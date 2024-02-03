import os
# from dotenv import load_dotenv
from lastfmcollagegenerator.collage_generator import CollageGenerator

# load_dotenv()

API_KEY = os.environ.get("LAST_FM_API_KEY")
API_SECRET = os.environ.get("LAST_FM_API_SECRET")

collage_generator = CollageGenerator(lastfm_api_key=API_KEY, lastfm_api_secret=API_SECRET)

image = collage_generator.generate(entity="album", username="berbardo8", cols=4, rows=4, period="1month")
image.save("img/collage.png", "png")

print("Successfully saved collage!")