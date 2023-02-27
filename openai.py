import openai
import requests

openai.api_key = "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"

def generate_image(prompt):
    # Generate an image from the DALL-E model using OpenAI's API
    response = openai.Completion.create(
        engine="image-alpha-001",
        prompt=prompt,
        max_tokens=256,
        nft_model="image-alpha-001",
        temperature=0.7,
    )

    # Retrieve the image url from the API response
    image_url = response.choices[0].text

    # Download the image from the url
    image_bytes = requests.get(image_url).content

    return image_bytes
