import os
import csv
from datetime import datetime
from emotion_detector import EmotionDetector

class DataManager:
    def __init__(self, detector: EmotionDetector, csv_path='data/csv/results.csv'):
        self.detector = detector
        self.csv_path = csv_path

    def process_data(self, image_path, time_info, menu_item):
        emotion = self.detector.is_student_happy(image_path)
        self.save_to_csv(time_info, menu_item, emotion, image_path)

    def save_to_csv(self, time_info, menu_item, emotion, image_path):
        file_name = os.path.basename(image_path)

        if not os.path.exists(os.path.dirname(self.csv_path)):
            os.makedirs(os.path.dirname(self.csv_path))

        with open(self.csv_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time_info, menu_item, emotion, file_name])

if __name__ == "__main__":
    emotion_detector = EmotionDetector()
    csv_path = 'test/data/csv/results.csv'
    data_manager = DataManager(detector=emotion_detector, csv_path=csv_path)

    image_paths = ['test/data/images/happy_student.png', 'test/data/images/unhappy_student.jpg']
    menu_item = "Test Menu Item" 
    image_paths = []
    for filename in os.listdir('test/data/images'):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_paths.append(os.path.join('test/data/images', filename))

    for image_path in image_paths:
        current_time = datetime.now()
        data_manager.process_data(image_path, current_time, menu_item)

    print(f"Processing complete. Results saved to {csv_path}")