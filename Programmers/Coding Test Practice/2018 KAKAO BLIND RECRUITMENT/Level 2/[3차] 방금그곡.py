# Problem:
# Given a melody sequence and similar songs, return exactly what song it is.

# My Solution:
def solution(m, musicinfos):
    m = m.replace('A#', 'a')
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    result = None
    dic = dict()
    for info in musicinfos:
        start, end, title, sound = info.split(',')
        hour1, min1 = start.split(':')
        hour2, min2 = end.split(':')
        time = (int(hour2) - int(hour1)) * 60 + int(min2) - int(min1)
        sound = sound.replace('A#', 'a')
        sound = sound.replace('C#', 'c')
        sound = sound.replace('D#', 'd')
        sound = sound.replace('F#', 'f')
        sound = sound.replace('G#', 'g')
        sound = sound * (time // len(sound)) + sound[0:time % len(sound)]
        dic[sound] = title
    for song in dic.keys():
        if m in song:
            if result is None:
                result = song
            else:
                if len(result) < len(song):
                    result = song

    if result is not None:
        return dic[result]
    else:
        return "(None)"
