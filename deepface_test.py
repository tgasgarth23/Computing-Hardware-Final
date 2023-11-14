from deepface import DeepFace

face_analysis = DeepFace.analyze(img_path = "images/test_image.png")
print(face_analysis)