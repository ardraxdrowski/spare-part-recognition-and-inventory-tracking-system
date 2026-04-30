import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from ultralytics import YOLO
import yaml

model = YOLO("../../models/machineparts.pt")

DATASETS = "../generated_datasets"

for dataset in os.listdir(DATASETS):

    dataset_path = os.path.join(DATASETS, dataset)

    print("Testing:", dataset)

    temp_yaml = {
        "path": dataset_path,
        "train": "images",
        "val": "images",
        "names": {
            0: "Digital Temperature Controller Module",
            1: "Permanent Magnetic DC Motor",
            2: "Hand Sealer Controller Module w/o CT",
            3: "PCB Assembly 230V HM",
            4: "Control Board CS Smart 90V"
        }
    }

    yaml_file = "temp_dataset.yaml"

    with open(yaml_file, "w") as f:
        yaml.dump(temp_yaml, f)

    results = model.val(
        data=yaml_file,
        imgsz=640,
        conf=0.6,
        project="../results",
        name=dataset,
        exist_ok=True
    )