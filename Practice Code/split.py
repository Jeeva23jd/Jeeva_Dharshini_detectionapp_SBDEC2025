import os
import shutil
import random

# -------- CONFIG -------- #
DATASET_DIR = r"J:\projects\infosys_virtual\New Data"
OUTPUT_DIR = r"J:\projects\infosys_virtual\dataset_split"

TRAIN_SPLIT = 0.70
TEST_SPLIT = 0.20
VAL_SPLIT = 0.10
# ------------------------ #

# Create output directory structure
for split in ["train", "test", "val"]:
    for sub in ["images", "labels"]:
        os.makedirs(os.path.join(OUTPUT_DIR, split, sub), exist_ok=True)

# Process each class folder
for class_name in os.listdir(DATASET_DIR):

    class_path = os.path.join(DATASET_DIR, class_name)

    if not os.path.isdir(class_path):
        continue

    print(f"Processing class: {class_name}")

    images_path = os.path.join(class_path, "images")
    labels_path = os.path.join(class_path, "labels")

    # Get image list (assume .jpg/.png etc.)
    image_files = sorted([
        f for f in os.listdir(images_path)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ])

    # Shuffle for unbiased split
    random.shuffle(image_files)

    total = len(image_files)

    train_count = int(total * TRAIN_SPLIT)
    test_count = int(total * TEST_SPLIT)
    val_count = total - train_count - test_count  # To avoid rounding issues

    train_files = image_files[:train_count]
    test_files = image_files[train_count:train_count + test_count]
    val_files = image_files[train_count + test_count:]

    # Function to copy images + labels together
    def copy_pairs(file_list, split_name):
        for img in file_list:
            img_src = os.path.join(images_path, img)
            label_src = os.path.join(labels_path, os.path.splitext(img)[0] + ".txt")

            img_dst = os.path.join(OUTPUT_DIR, split_name, "images", img)
            label_dst = os.path.join(OUTPUT_DIR, split_name, "labels",
                                     os.path.splitext(img)[0] + ".txt")

            shutil.copy(img_src, img_dst)

            if os.path.exists(label_src):
                shutil.copy(label_src, label_dst)
            else:
                print(f"⚠ WARNING: No label for {img}")

    # Copy to train/test/val
    copy_pairs(train_files, "train")
    copy_pairs(test_files, "test")
    copy_pairs(val_files, "val")

print("\n✅ Dataset split completed successfully!")