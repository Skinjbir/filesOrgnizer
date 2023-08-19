import os
import shutil

# Dictionary containing categories and their respective file extensions
file_extensions = {
    "PDF": [".pdf"],  # Category for PDF files

    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],  # Category for archive file formats

    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff"],  # Category for image file formats

    "Setup Files": [".exe", ".msi", ".dmg", ".pkg"],  # Category for executable and installer formats

    "Office Files": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp"]
    # Category for common office file formats
}


# Function to extract the file extension from a filename
def getFileExtension(filename):
    return os.path.splitext(filename)[1]


# Function to create a directory. If the directory already exists, it simply prints a message.
def createFolder(directory, folderName):
    folder_path = os.path.join(directory, folderName)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"The '{folderName}' is created successfully")
    else:
        print(f"The '{folderName}' already exists")


# Create a mapping of extensions to their categories for efficient lookups
extension_to_category = {}
for category, extensions in file_extensions.items():
    for ext in extensions:
        extension_to_category[ext] = category

# Define the directory where files are to be organized
workingDirectory = "" # ADD YOUR DIRECTORY
items = os.listdir(workingDirectory)

# Create directories for each category
for dir_name in file_extensions.keys():
    createFolder(workingDirectory, dir_name)
createFolder(workingDirectory, "Others")  # Create a directory for uncategorized files

# Organize files into the created directories
for item in items:
    item_path = os.path.join(workingDirectory, item)

    # Skip if it's a directory
    if os.path.isdir(item_path):
        continue

    # Determine the category of the item based on its file extension
    category = extension_to_category.get(getFileExtension(item), "Others")
    destination_path = os.path.join(workingDirectory, category, item)

    # Copy the file to its respective category directory
    shutil.copy(item_path, destination_path)

    print(item + "is being copied to " + category)
