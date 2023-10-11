from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')

results = model.train(data='C:\\Users\\admin\\Pictures\\dataset_proccessing\\output', epochs=150, imgsz=640)