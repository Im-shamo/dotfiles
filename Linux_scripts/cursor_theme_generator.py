import os 
import shutil

output_path = "/home/shamokwok/Pictures/silver_wolf_cursors/SilverWolfCursor/cursors"
linux_cursor_path = "/usr/share/icons/breeze_cursors/cursors"
window_cursor_path = "/home/shamokwok/Pictures/silver_wolf_cursors/output"
cursor_csv_path = "/home/shamokwok/Linux_scripts/cursor.csv"

linux_cursors = [file for file in os.listdir(linux_cursor_path) if os.path.isfile(os.path.join(linux_cursor_path,file))]
window_cursors = [file for file in os.listdir(window_cursor_path) if os.path.isfile(os.path.join(window_cursor_path, file))]
parsed_csv = []
with open(cursor_csv_path, "r") as cursor_csv:
    lines = cursor_csv.readlines()[1:]
    for line in lines:
        splited = line.split(",")
        parsed_csv.append((splited[0], splited[1]))

# print(parsed_csv)

for win_cur, linux_cur in parsed_csv:
    if win_cur == "":
        src = os.path.join(linux_cursor_path, linux_cur)
        dst = os.path.join(output_path, linux_cur)
    else:
        src = os.path.join(window_cursor_path, win_cur)
        dst = os.path.join(output_path, linux_cur)
    print(f"Copied {src} to {dst}")
    shutil.copy(src, dst)

