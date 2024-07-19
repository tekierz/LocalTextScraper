import os
import gradio as gr
from datetime import datetime

def scrape_text(input_directory, file_extension, output_directory):
    # If no output directory is provided, use the default
    if not output_directory:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Set the default output directory
        output_directory = os.path.join(script_dir, "Outputs")

    # Initialize an empty string to hold the contents of all files
    all_contents = ""

    # Walk through the directory
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    all_contents += f.read() + "\n"

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Generate timestamp for the output file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Write the collected contents to a single plain text file with timestamp
    output_file = os.path.join(output_directory, f"combined_output_{timestamp}.txt")
    with open(output_file, 'w') as f:
        f.write(all_contents)

    return f"All contents have been written to {output_file}"

# Gradio interface
iface = gr.Interface(
    fn=scrape_text,
    inputs=[
        gr.Textbox(label="Input Directory"),
        gr.Textbox(label="File Extension (e.g., .txt)"),
        gr.Textbox(label="Output Directory (optional, press Enter for default)")
    ],
    outputs=gr.Textbox(label="Result"),
    title="Local Text Scraper",
    description="Scrape text from files in a directory and combine them into a single file."
)

if __name__ == "__main__":
    iface.launch()