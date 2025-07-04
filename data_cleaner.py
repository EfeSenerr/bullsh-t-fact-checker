import os
from docling.document_converter import DocumentConverter

# Define paths
source_dir = "/content/data"
output_dir = "/content/drive/MyDrive/data_converted_hackathon/"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize converter once (no need to recreate it each iteration)
converter = DocumentConverter()

# Get all files in source directory
for filename in os.listdir(source_dir):
    # Skip directories if any
    if os.path.isdir(os.path.join(source_dir, filename)):
        continue
        
    # Create full source path
    source_path = os.path.join(source_dir, filename)
    
    # Convert document
    result = converter.convert(source_path)
    
    # Create output filename (preserve original name but change extension)
    base_name = os.path.splitext(filename)[0]  # removes original extension
    output_filename = f"{base_name}_converted.md"
    output_path = os.path.join(output_dir, output_filename)
    
    # Save with unique name
    with open(output_path, 'w') as f:
        f.write(result.document.export_to_markdown())
    
    print(f"Converted {filename} to {output_filename}")