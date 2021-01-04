# Import required packages 
import cv2 
import numpy as np
import pytesseract 
  
# Mention the installed location of Tesseract-OCR in your system 
pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/3.05.02/bin/tesseract'

def save_photo_text():
    # Read image from which text needs to be extracted 
    # convert to array of ints
    path = 'noisy_image.jpg'
    img = cv2.imread(path)
    # nparr = np.frombuffer(photo, np.uint8)
    # convert to image array
    # img = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
    # Preprocessing the image starts 
    
    # Convert the image to gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    # Performing OTSU threshold 
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
    
    # Specify structure shape and kernel size.  
    # Kernel size increases or decreases the area  
    # of the rectangle of pixels to be detected. 
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6)) 
    
    # Appplying dilation on the threshold image 
    dilation = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, rect_kernel)
    # dilation = cv2.dilate(closing, rect_kernel, iterations = 1) 

    # Finding contours 
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                    cv2.CHAIN_APPROX_NONE) 
    # print("contours", contours)
    # Creating a copy of image 
    im2 = img.copy() 
    
    # A text file is created and flushed 
    file = open("recognized.txt", "w+") 
    file.write("") 
    file.close() 
    
    # Looping through the identified contours 
    # Then bounding rectangle is cropped and passed on 
    # to pytesseract for extracting text from it 
    # Extracted text is then written into the text file 
    for cnt in contours: 
        x, y, w, h = cv2.boundingRect(cnt) 
        
        # Drawing a rectangle on copied image 
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        
        # Cropping the text block for giving input to OCR 
        cropped = im2[y:y + h, x:x + w] 
        
        # Open the file in append mode 
        file = open("recognized.txt", "a") 
        
        # Apply OCR on the cropped image 
        text = pytesseract.image_to_string(cropped, lang='eng') 
        
        # Appending the text into file 
        file.write(text) 
        file.write("\n") 
        
        # Close the file 
        file.close 
    
    # cv2.imwrite("dilated_noisy_5.png", dilation)
    # cv2.imwrite("image_rectangles_dilation_5.png", rect)

    cv2.imshow("Image with contours", rect)
    cv2.imshow("Dilated Image", dilation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

save_photo_text()
