# Local Text Scraper

Local Text Scraper is a Python application that allows you to scrape text from files in a specified directory and combine them into a single output file. It features a user-friendly Gradio interface for easy interaction.

## Features

- Scrape text from files with a specific extension in a given directory
- Combine all scraped text into a single output file
- User-friendly Gradio interface for easy interaction
- Option to specify custom output directory or use default

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/tekierz/LocalTextScraper.git
   ```

2. Navigate to the project directory:
   ```
   cd LocalTextScraper
   ```

3. Install the required dependencies:
   ```
   pip install gradio
   ```

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. The Gradio interface will launch in your default web browser.

3. Enter the following information in the interface:
   - Input Directory: The directory containing the files you want to scrape
   - File Extension: The extension of the files you want to scrape (e.g., .txt)
   - Output Directory (optional): The directory where you want to save the combined output file. If left blank, it will use a default "Outputs" folder in the same directory as the script.

4. Click "Submit" to start the scraping process.

5. The script will display a message indicating where the combined output file has been saved.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.