# Problem:
# Given two lists: genres and plays, make album with 2 most played songs.
# Condition(s):
# 1. Most played genre first.
# 2. Most played song first
# 3. If songs have same number of plays, low index first.

# My Solution:
def solution(genres, plays):
    answer = []
    Dic1 = {}
    Dic2 = {}
    idx = [i for i in range(len(plays))]
    zipped = list(zip(genres, plays, idx))

    for genre, play, idx in zipped:
        if genre not in Dic1.keys():
            Dic1[genre] = 0
            Dic1[genre] = Dic1[genre] + play
        else:
            Dic1[genre] = Dic1[genre] + play
        if genre not in Dic2.keys():
            Dic2[genre] = [[play, idx]]
        else:
            Dic2[genre].extend([[play, idx]])
    Dic1 = sorted(Dic1.items(), key=lambda Dic: Dic[1], reverse=True)
    genreRank = [i[0] for i in Dic1]

    for key in genreRank:
        temp = Dic2[key]
        temp = sorted(temp, key=lambda temp: (-temp[0], temp[1]))
        for i in range(len(temp)):
            if i > 1:
                break
            answer.extend([temp[i][1]])
    return answer

# Learned:
# 1. sorted(temp, key=lambda temp: (-temp[0], temp[1])): multi-key sorting (+- sign means ascendant, descendant).
