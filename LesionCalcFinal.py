from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
import tkinter as tk


root = Tk()
root.title('WHITE LESION CALCULATOR')
root.geometry("800x600")


def process_image():
    # Ask the user to select an option
    option = messagebox.askquestion("Image Source", "Use Default Camera?")

    if option == "yes":
        # Open the default camera
        camera = cv2.VideoCapture(0)
        while True:
            # Capture an image from the camera
            return_value, image = camera.read()

            # Display the captured image
            cv2.imshow("CAPTURED IMAGE", image)

            # Check if the user has clicked a key
            key = cv2.waitKey(1)
            if key == ord("s"):
                # Save the captured image
                cv2.imwrite("captured_image.jpg", image)
                break
            elif key == ord("q"):
                break

        # Release the camera
        camera.release()

        # Destroy all windows
        cv2.destroyAllWindows()

        # Read the saved image
        image = cv2.imread("captured_image.jpg")
    else:
        # Ask the user to select an image file
        filepath = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        # Read the image file
        image = cv2.imread(filepath)

    # Check if an image was selected
    if image is None:
        messagebox.showerror("Error", "No image selected")
        return

    cv2.imshow("ORIGINAL IMAGE", image)

    # Convert the image to grayscale
    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

    # Threshold the image to separate the lesion from the background
    im_thresholded = cv2.threshold(im_gray, 100, 150, cv2.THRESH_BINARY_INV)[1]

    # Check if the contours are being detected correctly
    cv2.imshow("THRESHOLDED IMAGE", im_thresholded)

    # Find the contours in the image
    contours, hierarchy = cv2.findContours(im_thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original image
    cv2.drawContours(image, contours, -3, (0, 150, 0), 2)

    # Calculate the percentage of white pixels
    white_pixels = np.sum(im_thresholded == 150)
    total_pixels = im_thresholded.shape[0] * im_thresholded.shape[1]
    white_percentage = round((white_pixels / total_pixels) * 100, 2)

    # Create a new window and resize the window
    height, width, _ = image.shape
    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Result", width, height)

    

    # Set the window properties to show a blue background
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("Result", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_FREERATIO)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Result", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

    # Display the result
    cv2.putText(image, f"White pixels: {white_pixels}", (1, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.9, (0, 220, 0), 1)
    cv2.putText(image, f"Total pixels: {total_pixels}", (1, 100), cv2.FONT_HERSHEY_TRIPLEX, 0.9, (0, 220, 0), 1)
    cv2.putText(image, f"Percentage: {white_percentage}%", (1, 150), cv2.FONT_HERSHEY_TRIPLEX, 0.9, (0, 220, 0), 1)
    cv2.imshow("Result", image)
    cv2.waitKey(0)


button = Button(root, text="Load Image", command=process_image)
button.pack(pady=20)
cv2.destroyAllWindows()

root.mainloop()