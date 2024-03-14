import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import pyttsx3
from youtubevideouploader import uploadvideo
import time
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import webbrowser
import pyautogui
import av
from moviepy.editor import VideoFileClip, AudioFileClip
import os


def keep_alphanumeric(input_string):
    # Use a loop to iterate through each character in the string
    result_string = ''.join(char for char in input_string if char.isalnum())

    return result_string

def create_fade_transition_video(duration, output_file, background_image_path):
    # Set video parameters
    fps = 30  # frames per second
    width, height = 1080, 1920  # video resolution

    # Load the background image
    background_image = cv2.imread(background_image_path)
    background_image = cv2.resize(background_image, (width, height))

    # Create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec (you can use other codecs as well)
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Calculate the total number of frames
    total_frames = int(duration * fps)

    # Create frames with fade transition and write them to the video
    for frame_count in range(total_frames):
        # Calculate the fade factor (linear interpolation between 0 and 1)
        fade_factor = np.interp(frame_count, [0, total_frames // 2, total_frames], [0, 1, 0])

        # Adjust the image using the fade factor
        faded_image = background_image * fade_factor

        # Write the frame to the video
        video_writer.write(faded_image.astype(np.uint8))

    # Release the VideoWriter object
    video_writer.release()
    print("Fade transition video made")


def convert_avif_to_jpeg(input_path, output_path):
    try:
        # Open the AVIF image using pyav
        container = av.open(input_path)
        stream = container.streams.video[0]

        # Read all frames and convert to RGB
        frames = [frame.to_image() for frame in container.decode(video=0)]
        rgb_images = [np.array(frame) for frame in frames]

        # Choose the first frame to save as JPEG
        rgb_image = Image.fromarray(rgb_images[0])

        # Save as JPEG
        rgb_image.save(output_path, "JPEG")
        print(f"Conversion successful: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error converting {input_path}: {str(e)}")


def add_newline_after_4_words(input_text):
    words = input_text.split()
    words_with_newline = [word if (i + 1) % 4 != 0 else word + "\n" for i, word in enumerate(words)]
    formatted_text = ' '.join(words_with_newline)
    return formatted_text


def add_text_to_video(video_path, output_path, text, font_size, text_color=(255, 255, 255),
                      font_path="C:\\Windows\\Fonts\\times.ttf"
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


def get_audio_duration(file_path):
    audio_clip = AudioFileClip(file_path)
    duration_in_seconds = audio_clip.duration
    return duration_in_seconds


def save_image(image_saving_path, link):
    if os.path.exists(f'{image_saving_path}.avif'):
        pass
    else:
        url = link
        webbrowser.open(url)
        pyautogui.sleep(3)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.sleep(1)
        pyautogui.press('backspace')
        pyautogui.sleep(1)
        pyautogui.write(image_saving_path)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        print("SAVED")



def text_to_audio(pathofaudio, text, speed=1.0, voice='english'):
    tts = gTTS(text=text, lang=voice, slow=False)
    tts.save(pathofaudio)

    # Using pyttsx3 for playing the audio with customizable speed and voice
    engine = pyttsx3.init()

    # Setting the speed rate
    engine.setProperty('rate', speed * 150)  # Adjust 150 according to your preference

    # Setting the voice
    found_voice = False
    voices = engine.getProperty('voices')
    for v in voices:
        # Check if 'languages' attribute is present in the voice
        if hasattr(v, 'languages') and v.languages:
            if v.languages[0] == voice:
                engine.setProperty('voice', v.id)
                found_voice = True
                break

    # Check if the specified voice was not found
    if not found_voice:
        print(f"Voice '{voice}' not found. Using the default voice.")

    # Playing the audio
    engine.say(text)
    engine.runAndWait()


def add_audio_to_video(video_file_path, audio_file_path, output_file):
    # Open the video file with moviepy
    video_clip = VideoFileClip(video_file_path)

    # Open the audio file with moviepy
    audio_clip = AudioFileClip(audio_file_path)

    # Set the audio of the video clip to the loaded audio clip
    video_clip = video_clip.set_audio(audio_clip)

    # Write the final video with audio
    video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=video_clip.fps)


if __name__ == '__main__':
    a = 0
    while a < 25:
        try:
            while True:
                Url = "https://www.hindustantimes.com/india-news"

                headerss = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                }
                web = requests.get(Url, headers=headerss)
                if str(web) == "<Response [200]>":
                    print(web)
                    soup = BeautifulSoup(web.content, 'html.parser')
                    newses = soup.find('h3', class_="hdg3")
                    news = newses.find('a')['href']
                    Url2 = f"https://www.hindustantimes.com{news}"
                    new_web = requests.get(Url2, headers=headerss)
                    new_soup = BeautifulSoup(new_web.content, 'html.parser')
                    heading = (new_soup.find('h1', class_='hdg1')).text
                    detail = new_soup.find('h2', class_='sortDec').text
                    picture = new_soup.find('div', class_='storyParagraphFigure').find('picture').find('img')['src']
                    print(heading)
                    print(detail)
                    print(picture)
                    break
                else:
                    print(web)

            filesavepath = keep_alphanumeric(heading)
            pathofaudio = fr'Y:\audio file\{filesavepath}.mp3'
            pathofvideo = fr'Y:\input video\{filesavepath}.mp4'
            text_written_video = fr'Y:\text wrting video\{filesavepath}.mp4'
            output_video = fr'Y:\output video\{filesavepath}.mp4'
            input_image_path = fr'Y:\input image\{filesavepath}.avif'
            output_image_path = fr'Y:\output image\{filesavepath}.jpg'
            saving_image_path = fr'Y:\input image\{filesavepath}'
            if not os.path.exists(output_video):
                text_to_audio(pathofaudio, detail, speed=1, voice='en')
                pyautogui.sleep(3)
                duration = (get_audio_duration(pathofaudio)) + 1
                save_image(saving_image_path, picture)
                pyautogui.sleep(3)
                convert_avif_to_jpeg(input_image_path, output_image_path)
                pyautogui.sleep(3)
                create_fade_transition_video(duration, pathofvideo, output_image_path)
                pyautogui.sleep(3)
                custom_font_size = 60
                custom_text_color = (255, 0, 0)  # RGB color, in this case, red
                add_text_to_video(pathofvideo, text_written_video, add_newline_after_4_words(heading), custom_font_size,
                                  custom_text_color)
                add_audio_to_video(text_written_video, pathofaudio, output_video)
                print("OUTPUT VIDEO COMPILED!!!")
                time.sleep(5)
                username = ''
                password = ''
                heading = heading[0:50]
                try:
                    uploadvideo(heading,output_video,username,password)
                    print("Uploaded Waiting 30 MINS")
                    time.sleep(30 * 60)
                except Exception as error2:
                    print(error2)
                    break
            else:
                print('Waiting 30 mins')
                time.sleep(30*60)
        except Exception as error:
            print(error)
            a = a + 1