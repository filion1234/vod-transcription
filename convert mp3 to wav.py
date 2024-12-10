import os
import subprocess

def convert_mp3_to_wav(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory {directory} does not exist.")
        return
    
    # Loop through all MP3 files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.mp3'):
            mp3_file = os.path.join(directory, filename)
            wav_file = os.path.join(directory, f"{os.path.splitext(filename)[0]}.wav")
            
            try:
                # Convert MP3 to WAV using ffmpeg
                subprocess.run(['ffmpeg', '-i', mp3_file, wav_file], check=True)
                print(f"Converted {mp3_file} to {wav_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {mp3_file}: {e}")
            except FileNotFoundError:
                print("Error: ffmpeg is not installed or not found in PATH.")

if __name__ == "__main__":
    # Replace this path with your directory
    directory = r"E:\nyana bananya"  # Change to your target folder
    convert_mp3_to_wav(directory)
