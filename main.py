from moviepy.editor import VideoFileClip
from pathlib import Path

WIDTH = 600

input_path_str = input("mp4 path? :")
input_path = Path(input_path_str)
output_dir = Path("outputs")
output_path = output_dir/f"{input_path.stem}.gif"

if not input_path.exists():
    print("file not found")
    exit()

clip = VideoFileClip(str(input_path))
clip = clip.resize(width=WIDTH)
clip.write_gif(output_path, fps=6)
clip.close()