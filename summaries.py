def main():
    input_path = input("Enter the path to a video file or directory: ").strip()

    # Remove quotes if included
    input_path = input_path.strip('"').strip("'")

    if os.path.isfile(input_path):
        if input_path.lower().endswith(('.mp4', '.avi', '.mkv')):
            timestamps = get_timestamps()
            if timestamps:
                play_video_at_timestamps(input_path, timestamps)
            else:
                print("No timestamps provided. Exiting.")
        else:
            print("The file is not a supported video format.")
    elif os.path.isdir(input_path):
        process_directory(input_path)
    else:
        print("Error: The specified path does not exist or is not valid.")
