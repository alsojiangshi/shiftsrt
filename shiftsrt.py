import sys
import re
from datetime import datetime, timedelta

def shift_timestamp(ts: str, delta: float) -> str:
    t = datetime.strptime(ts, "%H:%M:%S,%f")
    t += timedelta(seconds=delta)
    if t < datetime(1900, 1, 1):
        t = datetime(1900, 1, 1)
    return t.strftime("%H:%M:%S,%f")[:-3]

def shift_srt(input_file, output_file, delta_seconds):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    timestamp_pattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3})")
    new_content = timestamp_pattern.sub(lambda m: shift_timestamp(m.group(1), delta_seconds), content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("用法：python shiftsrt.py 输入文件.srt 输出文件.srt 偏移秒数（可为负）")
    else:
        shift_srt(sys.argv[1], sys.argv[2], float(sys.argv[3]))
