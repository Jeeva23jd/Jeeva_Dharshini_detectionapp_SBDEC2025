import os

image_dir = r"J:\projects\infosys_virtual\Datasets\heritage sites\images"
label_dir = r"J:\projects\infosys_virtual\Datasets\heritage sites\labels"
backup_log = os.path.join(image_dir, "rename_log.txt")
prefix = "image_"
image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]

# === Get image files ===
images = sorted(
    [f for f in os.listdir(image_dir) if os.path.splitext(f)[1].lower() in image_extensions]
)

# === Find last existing index ===
existing = [
    int(f.replace(prefix, "").split(".")[0]) 
    for f in images if f.startswith(prefix)
]
start_index = max(existing) + 1 if existing else 1  # continue numbering
print(f"Starting from index: {start_index}")

# === Rename and log ===
with open(backup_log, "a", encoding="utf-8") as log:
    log.write("\n--- New Renaming Session ---\nOldName\tNewName\n")

    for idx, old_image in enumerate(images, start=start_index):
        name, ext = os.path.splitext(old_image)
        if name.startswith(prefix):  # Skip already renamed files
            continue

        new_name = f"{prefix}{idx:04d}{ext.lower()}"
        old_image_path = os.path.join(image_dir, old_image)
        new_image_path = os.path.join(image_dir, new_name)

        # Check if target exists
        if os.path.exists(new_image_path):
            print(f"⚠️ Skipped (already exists): {new_name}")
            continue

        os.rename(old_image_path, new_image_path)

        # Update label name if exists
        old_label = os.path.join(label_dir, f"{name}.txt")
        new_label = os.path.join(label_dir, f"{prefix}{idx:04d}.txt")
        if os.path.exists(old_label):
            os.rename(old_label, new_label)

        # Log
        log.write(f"{old_image}\t{new_name}\n")
        print(f"✅ {old_image} → {new_name}")

print("\n🎉 Renaming complete without errors!")
print(f"Log updated at: {backup_log}")
