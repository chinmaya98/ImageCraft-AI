import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

def generate_images(img_description):
    """Generates an image using DALL-E 3 based on the provided description."""
    load_dotenv()
    openai_api_key = os.getenv("OPEN_API_KEY")

    if not openai_api_key:
        st.error("OpenAI API key not found. Please set the OPEN_API_KEY environment variable.")
        return None

    client = OpenAI(api_key=openai_api_key)

    try:
        image_response = client.images.generate(
            model="dall-e-3",
            prompt="Generate an image of a " + img_description,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = image_response.data[0].url
        return image_url
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.set_page_config(
        page_title="Image Generator",
        page_icon=":art:",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.title("🎨 DALL-E 3 Image Generator")
    st.markdown(
        """
        **Create stunning images from your text descriptions!**
        Simply enter your desired image description below, and let DALL-E 3 bring it to life.
        """
    )

    img_description = st.text_input(
        "Enter your image description:",
        placeholder="A futuristic cityscape at sunset",
    )

    if st.button("Generate Image"):
        if img_description:
            with st.spinner("Generating image..."):
                image_url = generate_images(img_description)

            if image_url:
                st.image(image_url, caption=img_description)
                st.success("Image generated successfully!")
            else:
                st.error("Image generation failed. Please check your API key and description.")
        else:
            st.warning("Please enter an image description.")
   

if __name__ == "__main__":
    main()