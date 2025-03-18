from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st
from streamlit_carousel import carousel

def generate_images(img_description, num_of_images):

    load_dotenv()
    openai_api_key = os.getenv("OPEN_API_KEY")

    client = OpenAI(api_key=openai_api_key)

    single_img = dict(
        title="",
        text="",
        interval=None,
        img="",

    )

    image_gallery=[]
    for i in range(num_of_images):
        image_response = client.images.generate(
            model="dall-e-3",
            prompt="Generate an image of a " + img_description,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = image_response.data[0].url
        new_image=single_img.copy()
        new_image["title"]=f"image {i+1}"
        new_image["text"]=img_description
        new_image["img"]=image_url
        image_gallery.append(new_image)
    return image_gallery

def main():
    st.set_page_config(page_title="Image generation", page_icon=":camera:", layout="centered")

    st.title("Image generation tool :camera:")

    st.subheader("This tool generates images based on the text you provide")
    img_description = st.text_input("Enter the description of the image you want to generate")
    num_of_images = st.number_input("Enter the number of images you want to generate", min_value=1, max_value=5, value=1)


    if st.button("Generate"):
        generate_image = generate_images(img_description, num_of_images) 
        carousel(items=generate_image,width=1)


if __name__ == "__main__":
    main()