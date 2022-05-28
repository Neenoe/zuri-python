def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('Once upon a time a psychology professor walked around on a stage while teaching stress management principles to an auditorium filled with students. As she raised a glass of water, everyone expected they would be asked the typical glass half empty or glass half full question. Instead, with a smile on her face, the professor asked, How heavy is this glass of water I am holding?'))