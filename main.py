from src.emotion_detector import EmotionDetector
from src.data_manager import DataManager


csv_path = 'data/csv'
test_csv_path = 'test/' + csv_path
detector = EmotionDetector()
data_manager = DataManager(detector=detector, csv_path=csv_path)
