# AI generated. 
# I just needed a util to easily see which hitobjects in the .osu file correspond to

import sys

def ms_to_human_time(ms: int) -> str:
    minutes = ms // 60000
    seconds = (ms % 60000) // 1000
    milliseconds = ms % 1000

    return f"{minutes}:{seconds:02d}.{milliseconds:03d}"

def parse_osu_file(filename: str):
    hitobjects = []

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    hitobjects_section = False
    line_number = 0

    for line in lines:
        line_number += 1
        line = line.strip()

        if line.startswith("[HitObjects]"):
            hitobjects_section = True
            continue

        if hitobjects_section:
            if line == "":
                break  # end of hitobjects section

            parts = line.split(",")
            if len(parts) >= 3:
                try:
                    time_ms = int(parts[2])
                    hitobjects.append((line_number, time_ms))
                except ValueError:
                    continue

    return hitobjects

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python osu_times.py <file.osu>")
        sys.exit(1)

    filename = sys.argv[1]
    hitobjects = parse_osu_file(filename)

    print("Line Number | Hitobject Time")
    print("-" * 20)

    for line_num, ms in hitobjects:
        print(f"{line_num:>10} | {ms_to_human_time(ms)}")
