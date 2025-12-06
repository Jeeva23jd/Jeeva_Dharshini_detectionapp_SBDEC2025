import os
import shutil

# ==========================
# 🔁 UPDATE THESE PATHS
# ==========================
images_dir = r"J:\projects\infosys_virtual\New Data\stc_cl\images"
labels_dir = r"J:\projects\infosys_virtual\New Data\stc_cl\labels"

matched_images_dir = r"J:\projects\infosys_virtual\New Data\stc_cl\matched\images"
matched_labels_dir = r"J:\projects\infosys_virtual\New Data\stc_cl\matched\labels"
unmatched_dir = r"J:\projects\infosys_virtual\New Data\stc_cl\unmatched_files"

# ==========================
# 📂 CREATE OUTPUT FOLDERS
# ==========================
os.makedirs(matched_images_dir, exist_ok=True)
os.makedirs(matched_labels_dir, exist_ok=True)
os.makedirs(unmatched_dir, exist_ok=True)

# What we consider as images / labels
image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff",".webp"]
label_extension = ".txt"

# ==========================
# 📜 GET FILE LISTS
# ==========================
image_files = [
    f for f in os.listdir(images_dir)
    if os.path.splitext(f)[1].lower() in image_extensions
]

label_files = [
    f for f in os.listdir(labels_dir)
    if os.path.splitext(f)[1].lower() == label_extension
]

# Maps: basename → full filename
image_basenames = {os.path.splitext(f)[0]: f for f in image_files}
label_basenames = {os.path.splitext(f)[0]: f for f in label_files}

matched = 0
unmatched = 0

# ==========================
# ✅ PROCESS MATCHED FILES
# ==========================
for name, img_file in image_basenames.items():
    if name in label_basenames:
        lbl_file = label_basenames[name]

        img_src = os.path.join(images_dir, img_file)
        lbl_src = os.path.join(labels_dir, lbl_file)

        img_dst = os.path.join(matched_images_dir, img_file)
        lbl_dst = os.path.join(matched_labels_dir, lbl_file)

        shutil.copy(img_src, img_dst)
        shutil.copy(lbl_src, lbl_dst)

        matched += 1
    else:
        # Image without label → move to unmatched
        img_src = os.path.join(images_dir, img_file)
        img_dst = os.path.join(unmatched_dir, img_file)

        shutil.move(img_src, img_dst)
        unmatched += 1

# ==========================
# 🚨 PROCESS UNMATCHED LABELS
# ==========================
for name, lbl_file in label_basenames.items():
    if name not in image_basenames:
        lbl_src = os.path.join(labels_dir, lbl_file)
        lbl_dst = os.path.join(unmatched_dir, lbl_file)

        shutil.move(lbl_src, lbl_dst)
        unmatched += 1

# ==========================
# 📊 SUMMARY
# ==========================
print("\n✅ Matching Completed!")
print(f"✔ Matched Pairs: {matched}")
print(f"⚠ Unmatched Files Moved: {unmatched}")
print(f"📁 Unmatched files saved in: {unmatched_dir}")