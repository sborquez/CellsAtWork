import sys
import os
import os.path as path
import csv
from math import floor
import xml.etree.ElementTree as ET
from tqdm import tqdm

# testing images portion
TESTING_SPLIT = 0.1

if len(sys.argv) != 2:
    print("Usa: python prepare_data.py ruta/a/la/carpeta/BCCD")
    exit(1)
elif (not path.exists(sys.argv[1])):
    print(f"No se encontró el directorio: {sys.argv[1]}")
    exit(1)

bccd_folder = sys.argv[1]
if ("BCCD" in os.listdir(bccd_folder)):
    bccd_folder = path.join(bccd_folder, "BCCD")

if (os.listdir(bccd_folder) != ['Annotations', 'ImageSets', 'JPEGImages']):
    print(f"Directorio invalido: {bccd_folder}")
    exit(1)

if not path.exists("dataset"):
    os.mkdir("dataset")

train_file = open(path.join("dataset","train.csv"), 'w', newline="")
test_file = open(path.join("dataset","test.csv"), 'w', newline="")
fieldnames = ["image", "xmin", "ymin", "xmax", "ymax", "name"]
train_writer = csv.DictWriter(train_file, fieldnames=fieldnames)
test_writer = csv.DictWriter(test_file, fieldnames=fieldnames)

_splitter = int(1 // TESTING_SPLIT)
_images = os.listdir(path.join(bccd_folder, "Annotations"))

for i, image_annotation  in tqdm(enumerate(_images), total=len(_images)):
    tree = ET.parse(path.join(bccd_folder, "Annotations", image_annotation))
    root = tree.getroot()
    image = path.join(bccd_folder, "JPEGImages", root.find("filename").text)
    if path.splitext(image)[1] == "":
        image += ".jpg"
    for cell in root.iter("object"):
        name = cell.find("name").text
        box = {i.tag:int(i.text) for i in cell.find("bndbox").iter() if i.tag != "bndbox"}
        if box["xmin"] == box["xmax"] or box["ymin"] == box["ymax"]:
            continue
        elif i%_splitter:
            train_writer.writerow({"image": image, "name":name, **box})
        else:
            test_writer.writerow({"image": image, "name":name, **box})

train_file.close()
test_file.close()

with open(path.join("dataset","class_map.csv"), 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows([("RBC", 0),("WBC", 1),("Platelets", 2)])