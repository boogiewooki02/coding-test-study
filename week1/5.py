def toSecond(time):
    minutes, seconds = map(int, time.split(":"))
    return minutes * 60 + seconds

def toTime(sec):
    m = sec // 60
    s = sec % 60
    return f"{m:02}:{s:02}"

def solution(video_len, pos, op_start, op_end, commands):
    video_sec = toSecond(video_len)
    pos_sec = toSecond(pos)
    start_sec = toSecond(op_start)
    end_sec = toSecond(op_end)
    
    for command in commands:
        if command == "prev":
            pos_sec = max(0, pos_sec - 10)
        elif command == "next":
            if start_sec <= pos_sec <= end_sec:
                pos_sec = end_sec
            pos_sec = min(video_sec, pos_sec + 10)
        
        if start_sec <= pos_sec <= end_sec:
            pos_sec = end_sec

    return toTime(pos_sec)