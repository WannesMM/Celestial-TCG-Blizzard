import os

def get_card_image_filepath(card_name):
    base_directory = r'C:\Users\wanne\OneDrive\Bureaublad\Celestial Mobile\images'
    image_filename = f"{card_name}.png"
    image_filepath = os.path.join(base_directory, image_filename)
    
    print(f"Checking for image at: {image_filepath}")  # Debug print
    
    if os.path.exists(image_filepath):
        print(f"Image found: {image_filepath}")  # Debug print
        return image_filepath
    else:
        print(f"IMAGE NIET GEVONDEN: {image_filepath}")
        return r"C:\Users\wanne\OneDrive\Bureaublad\Celestial Mobile\images\image not found.png"