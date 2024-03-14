import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def add_newline_after_4_words(input_text):
    words = input_text.split()
    words_with_newline = [word if (i + 1) % 4 != 0 else word + "\n" for i, word in enumerate(words)]
    formatted_text = ' '.join(words_with_newline)
    return formatted_text

def add_text_to_video(video_path, output_path, text, font_size, text_color=(255, 255, 255), font_path = "C:\\Windows\\Fonts\\times.ttf"
):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get video details
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(5)

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Load a font
    font = ImageFont.truetype(font_path, font_size)

    # Process each frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to a PIL Image
        pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_image)

        # Define text position (adjust as needed)
        text_position = (100, 100)

        # Add multiline text to the image
        draw.multiline_text(text_position, text, font=font, fill=text_color)

        # Convert the image back to OpenCV format
        frame_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

        # Write the frame to the output video
        out.write(frame_with_text)

        # Display the frame (optional, comment out if not needed)
        cv2.imshow('Frame', frame_with_text)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture and writer objects
    cap.release()
    out.release()

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()

# Example usage
video_path = 'fade_transition_video_with_audio.mp4'
output_path = 'output_video_with_text.avi'
text_to_add = ("Casey Anthony’s parents are appearing in a true "
               "crime reality show on A&E. Here, they will both "
               "be seen taking lie detector tests on camera."
               "Casey Anthony’s parents are appearing in a true "
               "crime reality show on A&E. Here, they will both "
               "be seen taking lie detector tests on camera."
               )
custom_font_size = 50
custom_text_color = (255, 0, 0)  # RGB color, in this case, red

add_text_to_video(video_path, output_path, add_newline_after_4_words(text_to_add), custom_font_size, custom_text_color)
