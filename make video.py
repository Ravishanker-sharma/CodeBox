import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, clips_array

def create_fade_transition_video_with_audio(duration, output_file, background_image_path, audio_file_path):
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

    # Open the video file with moviepy
    video_clip = VideoFileClip(output_file)

    # Open the audio file with moviepy
    audio_clip = AudioFileClip(audio_file_path)

    # Set the audio of the video clip to the loaded audio clip
    video_clip = video_clip.set_audio(audio_clip)

    # Write the final video with audio
    video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=fps)

# Example: Create a video with a fade transition and add audio
create_fade_transition_video_with_audio(duration=11.02, output_file='fade_transition_video_with_audio.mp4', background_image_path=R'C:\Users\ravis\OneDrive\Pictures\eee.png', audio_file_path=r'Y:\audio file\IthinkshemighthaveNikkiHaleyseeksmentalhealthreformafterIowaschoolshootingVivekRamaswamytakesjibe.mp3')
