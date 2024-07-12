from openai import OpenAI
import openai
import os
os.environ["OPENAI_API_KEY"] = ""
client = OpenAI()
from openai import OpenAI
import os
import openai
def genimage(img):
    os.environ["OPENAI_API_KEY"] = ""
    client = OpenAI()
    response = client.images.generate(
    model="dall-e-3",
    prompt=img,
    size="1792x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    print(image_url)
    return image_url