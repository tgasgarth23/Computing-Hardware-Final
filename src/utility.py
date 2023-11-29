import os
import shutil
import datetime

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

def generate_filename(timestamp):
    import datetime

    # Create a filename using the timestamp
    filename = f"image_{timestamp}.jpg"
    return filename

def get_menu():
    # fill out later
    return ['Grilled Chicken', 'White Rice', 'Brown Rice', 'Pasta', 'Alfredo Sauce', 'Marinara Sauce']

