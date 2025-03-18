# DALL-E 3 Image Generator

This Streamlit application allows users to generate images using OpenAI's DALL-E 3 model directly from text prompts.

## Features

* **Text-to-Image Generation:** Enter a text description, and the app will generate a corresponding image using DALL-E 3.
* **User-Friendly Interface:** Built with Streamlit for a simple and intuitive user experience.
* **Error Handling:** Provides clear error messages for API key issues and other potential problems.
* **Loading Indicator:** Displays a spinner while the image is being generated.
* **Image Display:** Shows the generated image with the prompt as the caption.
* **Tips for Better Images:** Offers guidance on writing effective prompts.

## Prerequisites

* Python 3.6+
* `pip` (Python package installer)
* OpenAI API key (with access to DALL-E 3)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install streamlit openai python-dotenv
    ```

4.  **Create a `.env` file:**

    * In the root directory of the project, create a file named `.env`.
    * Add your OpenAI API key to the `.env` file:

        ```
        OPEN_API_KEY=your_openai_api_key_here
        ```

    * **Important:** Never commit your `.env` file to version control. Add `.env` to your `.gitignore` file.

## Usage

1.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

    (Replace `app.py` with the name of your Python script.)

2.  **Enter a text description:**

    * In the Streamlit app, enter the description of the image you want to generate in the text area.

3.  **Generate the image:**

    * Click the "Generate Image" button.
    * The app will display the generated image below the button.

## Code Explanation

* **`generate_images(img_description)`:**
    * Loads the OpenAI API key from the `.env` file.
    * Uses the OpenAI client to generate an image using DALL-E 3.
    * Returns the URL of the generated image.
* **`main()`:**
    * Configures the Streamlit page.
    * Creates a text area for user input.
    * Handles the button click event and calls `generate_images()`.
    * Displays the generated image.
    * Adds tips for better image results.
 
## Result

![Image](https://github.com/user-attachments/assets/422ea1f7-1ce5-4fb1-96d7-70f7400d8eeb)

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## Author

[Your Name/GitHub Username]
