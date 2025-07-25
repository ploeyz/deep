import cv2

def convert_to_grayscale(image_path):
    return cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def main():
    img = cv2.imread('photo/Chelsea.jpg')
    gray = convert_to_grayscale(img)
    resized_img = resize_image(gray, 500, 300)
    cv2.imshow('Image', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()
    