import os
from PIL import Image
# from dotenv import load_dotenv
from lastfmcollagegenerator.collage_generator import CollageGenerator

# load_dotenv()

API_KEY = os.environ.get("LAST_FM_API_KEY")
API_SECRET = os.environ.get("LAST_FM_API_SECRET")


try:
    collage_generator = CollageGenerator(lastfm_api_key=API_KEY, lastfm_api_secret=API_SECRET)
    image = collage_generator.generate(entity="album", username="berbardo8", cols=4, rows=4, period="1month")

    image = image.resize((900,900), Image.LANCZOS)
    image.save("img/collage.webp", optimize=True)

    print("Successfully saved collage!")

except:
    print("Couldn't save collage, using old image!")
