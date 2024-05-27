# import re

# # Function to extract timezones from a line
# def extract_timezones(line):
#     timezones = re.findall(r'\d+:\d+:\d+(?:,\d+)?', line)
#     if len(timezones) >= 2:
#         return ' --> '.join(timezones)
#     elif len(timezones) == 1:
#         return '0:00 --> ' + timezones[0]

# # Function to count words in a string
# def count_words(text):
#     count = 0
#     for char in text:
#         if char.isspace():
#             count += 1
#     return count + 1

# # Read the SRT file
# with open('Jaane_Bhi_Do_Yaaro_1983.srt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()

# with open('subtitles_cleaned.srt', 'r', encoding='utf-8') as file:
#     strs = ''.join(file.readlines())
# words = strs.split()

# # Initialize a list to store timezones and their word counts
# timezones_with_counts = []

# # Initialize variables to store current timezone and text
# current_timezone = ''
# current_text = ''

# # Iterate through each line and extract timezones and texts
# p = 0
# for line in lines:
#     timezone = extract_timezones(line)
#     if timezone:
#         if current_timezone and current_text:
#             word_count = count_words(current_text)
#             words1 = current_text.split()
#             for i in range(word_count):
#                 if p < len(words):  # Check if index is within range
#                     words1[i] = words[p]
#                     p += 1
#                 else:
#                     break  # Stop if index exceeds words list length
#             timezones_with_counts.append((current_timezone, words1))
#             current_text = ''  # Reset current_text for the next timezone
#         current_timezone = timezone
#     else:
#         current_text += line.strip()  # Append text to current_text

# # Add word count for the last timezone
# if current_timezone and current_text:
#     word_count = count_words(current_text)
#     words1 = current_text.split()
#     for i in range(word_count):
#         if p < len(words):  # Check if index is within range
#             words1[i] = words[p]
#             p += 1
#         else:
#             break  # Stop if index exceeds words list length
#     timezones_with_counts.append((current_timezone, words1))

# # Write timezones with their word counts to a text file
# with open('output.txt', 'w', encoding='utf-8') as output_file:
#     index = 1
#     for timezone, text in timezones_with_counts:
#         output_file.write(f"{index}\n{timezone}\n")
#         word_counter = 0
#         line_counter = 0
#         for word in text:
#             output_file.write(word + " ")
#             word_counter += 1
#             line_counter += 1
#             if word_counter % 3 == 0:  # Print 3 words per line
#                 output_file.write("\n")  # Move to the next line
#                 line_counter = 0
#             elif line_counter % 6 == 0:  # Add an extra line break after every 6 words
#                 output_file.write("\n")  # Move to the next line

#         # Add an empty line between subtitles if the timezone index changes
#         if index < len(timezones_with_counts):
#             next_timezone = timezones_with_counts[index][0]
#             if timezone != next_timezone:
#                 output_file.write("\n")  # Add an empty line between subtitles

#         output_file.write("\n")  # Add an empty line after each entry
#         index += 1



# import re

# # Function to extract timezones from a line
# def extract_timezones(line):
#     timezones = re.findall(r'\d+:\d+:\d+(?:,\d+)?', line)
#     if len(timezones) >= 2:
#         return ' --> '.join(timezones)
#     elif len(timezones) == 1:
#         return '0:00 --> ' + timezones[0]

# # Function to count words in a string
# def count_words(text):
#     count = 0
#     for char in text:
#         if char.isspace():
#             count += 1
#     return count + 1

# # Read the SRT file
# with open('Jaane_Bhi_Do_Yaaro_1983.srt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()

# with open('subtitles_cleaned.srt', 'r', encoding='utf-8') as file:
#     strs = ''.join(file.readlines())
# words = strs.split()

# # Initialize a list to store timezones and their word counts
# timezones_with_counts = []

# # Initialize variables to store current timezone and text
# current_timezone = ''
# current_text = ''

# # Iterate through each line and extract timezones and texts
# p = 0
# for line in lines:
#     timezone = extract_timezones(line)
#     if timezone:
#         if current_timezone and current_text:
#             word_count = count_words(current_text)
#             words1 = current_text.split()
#             for i in range(word_count):
#                 if p < len(words):  # Check if index is within range
#                     words1[i] = words[p]
#                     p += 1
#                 else:
#                     break  # Stop if index exceeds words list length
#             timezones_with_counts.append((current_timezone, words1))
#             current_text = ''  # Reset current_text for the next timezone
#         current_timezone = timezone
#     else:
#         current_text += line.strip()  # Append text to current_text

# # Add word count for the last timezone
# if current_timezone and current_text:
#     word_count = count_words(current_text)
#     words1 = current_text.split()
#     for i in range(word_count):
#         if p < len(words):  # Check if index is within range
#             words1[i] = words[p]
#             p += 1
#         else:
#             break  # Stop if index exceeds words list length
#     timezones_with_counts.append((current_timezone, words1))

# # Write timezones with their word counts to a text file
# with open('output.txt', 'w', encoding='utf-8') as output_file:
#     index = 1
#     for timezone, text in timezones_with_counts:
#         output_file.write(f"{index}\n{timezone}\n")
#         output_file.write(" ".join(text) + "\n\n")  # Write the entire text for the timezone

#         # Add an empty line between subtitles if the timezone index changes
#         if index < len(timezones_with_counts):
#             next_timezone = timezones_with_counts[index][0]
#             if timezone != next_timezone:
#                 output_file.write("\n")  # Add an empty line between subtitles

#         index += 1
# import re

# # Function to extract timezones from a line
# def extract_timezones(line):
#     timezones = re.findall(r'\d+:\d+:\d+(?:,\d+)?', line)
#     if len(timezones) >= 2:
#         return ' --> '.join(timezones)
#     elif len(timezones) == 1:
#         return '0:00 --> ' + timezones[0]

# # Function to count words in a string
# def count_words(text):
#     count = 0
#     for char in text:
#         if char.isspace():
#             count += 1
#     return count + 1

# # Read the SRT file
# with open('U ME AUR GHAR [Digital]-1080p_1.mp4.srt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()

# with open('subtitles_cleaned.srt', 'r', encoding='utf-8') as file:
#     strs = ''.join(file.readlines())
# words = strs.split()

# # Initialize a list to store timezones and their word counts
# timezones_with_counts = []

# # Initialize variables to store current timezone and text
# current_timezone = ''
# current_text = ''

# # Iterate through each line and extract timezones and texts
# p = 0
# for line in lines:
#     timezone = extract_timezones(line)
#     if timezone:
#         if current_timezone and current_text:
#             word_count = count_words(current_text)
#             words1 = current_text.split()
#             for i in range(word_count):
#                 if p < len(words):  # Check if index is within range
#                     words1[i] = words[p]
#                     p += 1
#                 else:
#                     break  # Stop if index exceeds words list length
#             timezones_with_counts.append((current_timezone, words1))
#             current_text = ''  # Reset current_text for the next timezone
#         current_timezone = timezone
#     else:
#         current_text += line.strip()  # Append text to current_text

# # Add word count for the last timezone
# if current_timezone and current_text:
#     word_count = count_words(current_text)
#     words1 = current_text.split()
#     for i in range(word_count):
#         if p < len(words):  # Check if index is within range
#             words1[i] = words[p]
#             p += 1
#         else:
#             break  # Stop if index exceeds words list length
#     timezones_with_counts.append((current_timezone, words1))

# # Write timezones with their word counts to a text file
# with open('output.txt', 'w', encoding='utf-8') as output_file:
#     index = 1
#     for timezone, text in timezones_with_counts:
#         output_file.write(f"{index}\n{timezone}\n")
#         for word in text:
#             output_file.write(word + " ")
#             if '।' in word:
#                 output_file.write("\n")
#         output_file.write("\n\n")  # Add an empty line after each entry

#         # Add an empty line between subtitles if the timezone index changes
#         if index < len(timezones_with_counts):
#             next_timezone = timezones_with_counts[index][0]
#             if timezone != next_timezone:
#                 output_file.write("\n")  # Add an empty line between subtitles

#         index += 1
import re

# Function to extract timezones from a line
def extract_timezones(line):
    timezones = re.findall(r'\d+:\d+:\d+(?:,\d+)?', line)
    if len(timezones) >= 2:
        return ' --> '.join(timezones)
    elif len(timezones) == 1:
        return '0:00 --> ' + timezones[0]

# Function to count words in a string
def count_words(text):
    count = 0
    for char in text:
        if char.isspace():
            count += 1
    return count + 1

# Read the SRT file
with open('music.srt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open('subtitles_cleaned.srt', 'r', encoding='utf-8') as file:
    strs = ''.join(file.readlines())
words = strs.split()

# Initialize a list to store timezones and their word counts
timezones_with_counts = []

# Initialize variables to store current timezone and text
current_timezone = ''
current_text = ''

# Punctuation characters that trigger a line break
punctuation_marks = ['।', '?', '!', ',', ';', ':']

# Iterate through each line and extract timezones and texts
p = 0
for line in lines:
    timezone = extract_timezones(line)
    if timezone:
        if current_timezone and current_text:
            word_count = count_words(current_text)
            words1 = current_text.split()
            for i in range(word_count):
                if p < len(words):  # Check if index is within range
                    words1[i] = words[p]
                    p += 1
                else:
                    break  # Stop if index exceeds words list length
            timezones_with_counts.append((current_timezone, words1))
            current_text = ''  # Reset current_text for the next timezone
        current_timezone = timezone
    else:
        current_text += line.strip()  # Append text to current_text

# Add word count for the last timezone
if current_timezone and current_text:
    word_count = count_words(current_text)
    words1 = current_text.split()
    for i in range(word_count):
        if p < len(words):  # Check if index is within range
            words1[i] = words[p]
            p += 1
        else:
            break  # Stop if index exceeds words list length
    timezones_with_counts.append((current_timezone, words1))

# Write timezones with their word counts to a text file
with open('output.txt', 'w', encoding='utf-8') as output_file:
    index = 1
    for timezone, text in timezones_with_counts:
        output_file.write(f"{index}\n{timezone}\n")
        for word in text:
            output_file.write(word + " ")
            if any(punct in word for punct in punctuation_marks):
                output_file.write("\n")
        output_file.write("\n\n")  # Add an empty line after each entry

        # Add an empty line between subtitles if the timezone index changes
        if index < len(timezones_with_counts):
            next_timezone = timezones_with_counts[index][0]
            if timezone != next_timezone:
                output_file.write("\n")  # Add an empty line between subtitles

        index += 1
