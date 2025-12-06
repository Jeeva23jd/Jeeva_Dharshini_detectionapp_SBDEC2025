import os
import xml.etree.ElementTree as ET

# 🔹 Set your input and output paths
input_dir = r"J:\projects\infosys_virtual\label image"
output_dir = r"J:\projects\infosys_virtual\label image-yolo"

# Create output folder if it doesn’t exist
os.makedirs(output_dir, exist_ok=True)

# 🔹 Define your class names (same as used for model training)
classes = ["stc_cl", "cropfarmlands", "non_archeological_surfaces", "heritage_sites"]

# 🔹 Loop through all XML files in the input directory
for xml_file in os.listdir(input_dir):
    if not xml_file.endswith(".xml"):
        continue

    xml_path = os.path.join(input_dir, xml_file)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # 🔹 Get image size
    size = root.find("size")
    img_w = int(size.find("width").text)
    img_h = int(size.find("height").text)

    # 🔹 Create YOLO format text file
    txt_file = os.path.join(output_dir, xml_file.replace(".xml", ".txt"))
    with open(txt_file, "w") as f:
        for obj in root.findall("object"):
            cls = obj.find("name").text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)

            xml_box = obj.find("bndbox")
            xmin = float(xml_box.find("xmin").text)
            ymin = float(xml_box.find("ymin").text)
            xmax = float(xml_box.find("xmax").text)
            ymax = float(xml_box.find("ymax").text)

            # 🔹 Convert to YOLO format (normalized values)
            x_center = ((xmin + xmax) / 2) / img_w
            y_center = ((ymin + ymax) / 2) / img_h
            width = (xmax - xmin) / img_w
            height = (ymax - ymin) / img_h

            # 🔹 Write to YOLO .txt file
            f.write(f"{cls_id} {x_center} {y_center} {width} {height}\n")

print("✅ Conversion complete! YOLO labels saved in:", output_dir)
