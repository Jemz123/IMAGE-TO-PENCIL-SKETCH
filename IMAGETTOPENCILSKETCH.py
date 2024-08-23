import cv2
import numpy as np

def image_to_sketch(image_path, output_path):
    # Load the image
    image = cv2.imread(r"C:\Users\Administrator\Pictures\python\WIN_20240528_19_53_41_Pro.jpg")
    
    # Check if the image was loaded successfully
    if image is None:
        raise ValueError("Image not found or unable to load.")
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)
    
    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    
    # Create the pencil sketch by blending the grayscale image with the inverted blurred image
    sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    
    # Save the resulting sketch image
    cv2.imwrite(output_path, sketch_image)
    
    # Optionally, display the result
    cv2.imshow('Pencil Sketch', sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_to_sketch('path_to_your_image.jpg', 'path_to_save_sketch.jpg')
