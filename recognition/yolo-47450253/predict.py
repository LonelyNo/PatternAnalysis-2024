import torch
from ultralytics import YOLO

TRAINED_WEIGHTS = "./models/train2/weights/best.pt"
TEST_SET = "./data/images/test"


def predict():
    device = 'cuda' if torch.cuda.is_available() else 'cpu' #default to gpu
    model = YOLO(TRAINED_WEIGHTS).to(device)

    validate = model.val(data=DATA_YML, split='test')

    results = model.predict(source=TEST_SET,
                            imgsz=640,
                            conf=0.5,
                            iou=0.8,
                            save=False)


if __name__ == '__main__':
    predict()