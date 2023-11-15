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

def generate_filename():
    import datetime

    # Get the current timestamp with milliseconds
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

    # Create a filename using the timestamp
    filename = f"image_{timestamp}.jpg"
    return filename


