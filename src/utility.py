import os
import shutil
import datetime
from datetime import datetime
import json

def delete_all_images(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def generate_filename():
    import datetime

    # Get the current timestamp with milliseconds
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

    # Create a filename using the timestamp
    filename = f"image_{timestamp}.jpg"
    return filename

def get_menu_items():
        # Get the current date and time
    now = datetime.now()
    month = now.strftime("%B").lower()  # e.g., "december"
    day_of_month = now.day  # e.g., 3

    # Determine the meal type based on the current time
    current_hour = now.hour + now.minute / 60  # Convert to hours
    if 0 <= current_hour < 11.5:
        meal = "breakfast"
    elif 11.5 <= current_hour < 17:
        meal = "lunch"
    else:
        meal = "dinner"

    # Construct the file path
    file_name = f"{month}_{meal}.json"
    file_path = os.path.join('src/val_menu/', file_name)

    # Load the JSON file
    try:
        with open(file_path, 'r') as file:
            menu_data = json.load(file)
            # Get the menu for the specific day
            daily_menu = menu_data.get(str(day_of_month), [])
            return daily_menu
    except FileNotFoundError:
        return f"Menu file not found: {file_path}"
    
if __name__ == '__main__':
    print(get_menu_items())