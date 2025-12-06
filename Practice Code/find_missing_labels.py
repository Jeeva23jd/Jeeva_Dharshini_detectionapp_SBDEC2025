import os

# Paths
image_dir = r"J:\projects\infosys_virtual\EXPLORED-SET\EXPLORED-SET\heritage_sites\images"
label_dir = r"J:\projects\infosys_virtual\EXPLORED-SET\EXPLORED-SET\heritage_sites\labels"

# Valid image extensions
image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]

# Get all image base names (without extension)
image_basenames = set(
    os.path.splitext(f)[0]
    for f in os.listdir(image_dir)
    if os.path.splitext(f)[1].lower() in image_extensions
)

# Get all label base names (without extension)
label_basenames = set(
    os.path.splitext(f)[0]
    for f in os.listdir(label_dir)
    if f.endswith(".txt")
)

# Findings
missing_labels = sorted(list(image_basenames - label_basenames))  # images with no label
extra_labels = sorted(list(label_basenames - image_basenames))    # labels with no image

# Display results
print(f"🧾 Total Images: {len(image_basenames)}")
print(f"🏷️ Total Labels: {len(label_basenames)}")
print(f"⚠️ Images without labels: {len(missing_labels)}")
print(f"⚠️ Labels without images (EXTRA): {len(extra_labels)}\n")

if missing_labels:
    print("❌ Images missing YOLO labels:")
    for name in missing_labels:
        print(" -", name)
else:
    print("✅ All images have labels.")

print("\n-----------------------------------------\n")

if extra_labels:
    print("⚠️ ⚠️ EXTRA LABEL FILES (NO IMAGES FOUND):")
    for name in extra_labels:
        print(" -", name + ".txt")
else:
    print("🎉 No extra labels found. Dataset is clean!")
