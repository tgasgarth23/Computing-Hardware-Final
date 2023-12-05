import os
import csv
from datetime import datetime
from .emotion_detector import EmotionDetector

class DataManager:
    def __init__(self, csv_path='data/csv/results.csv'):
        self.csv_path = csv_path

    def save_to_csv(self, emotions, menu_item):

        if not os.path.exists(os.path.dirname(self.csv_path)):
            os.makedirs(os.path.dirname(self.csv_path))

        with open(self.csv_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), menu_item, emotions])

