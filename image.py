import os
import json
import datetime
from PIL import Image, ImageOps

gallery_folder = 'gallery'
json_file = 'images.json'
JPEG_QUALITY = 70

def load_existing_json():
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as infile:
            try:
                data = json.load(infile)
                if isinstance(data, list):
                    return data
            except json.JSONDecodeError:
                print("Warning: Could not decode JSON from", json_file)
    return []

def save_json(data):
    with open(json_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)
    print(f"{json_file} updated.")

def compress_image(image_path):
    try:
        with Image.open(image_path) as img:
            img = ImageOps.exif_transpose(img)

            save_params = {}
            save_params['quality'] = JPEG_QUALITY
            save_params['optimize'] = True
            
            img.save(image_path, **save_params)
            print(f"Compressed: {image_path}")
    except Exception as e:
        print(f"Error compressing {image_path}: {e}")

def main():
    images_data = load_existing_json()
    registered_files = {item.get("filename") for item in images_data if "filename" in item}
    
    for item in images_data:
        full_path = os.path.join(gallery_folder, item.get("filename"))
        if not os.path.isfile(full_path):
            images_data.remove(item)
            print('removed', item.get("filename"))

    all_files = os.listdir(gallery_folder)
    for file in all_files:
        if file.lower().endswith('.jpg'):
            full_path = os.path.join(gallery_folder, file)
            if os.path.isfile(full_path):
                if file not in registered_files:
                    compress_image(full_path)
                    images_data.append({
                        "filename": file,
                    })
                
    save_json(images_data)

if __name__ == '__main__':
    main()
