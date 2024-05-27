# import re

# # Define the input and output file names
# input_file = 'Jaane Bhi Do Yaaro_SLS.srt'
# output_file = 'subtitles_cleaned.srt'

# # Regular expression pattern to match the timestamp lines
# timestamp_pattern = re.compile(r'^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$')

# # Open the input file for reading
# with open(input_file, 'r', encoding='utf-8') as infile:
#     # Open the output file for writing
#     with open(output_file, 'w', encoding='utf-8') as outfile:
#         # Iterate through each line in the input file
#         for line in infile:
#             # Strip leading and trailing whitespace from the line
#             stripped_line = line.strip()
#             # If the line is not a timestamp line, write it to the output file
#             if not timestamp_pattern.match(stripped_line) and stripped_line:
#                 outfile.write(stripped_line + '\n')


import re

# Define the input and output file names
input_file = 'Sirf Ek Bandaa Kaafi Hai_SLC_24FPS[New].srt'
output_file = 'subtitles_cleaned.srt'

# Regular expression patterns to match the timestamp lines and serial numbers
timestamp_pattern = re.compile(r'^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$')
serial_number_pattern = re.compile(r'^\d+$')

# Open the input file for reading
with open(input_file, 'r', encoding='utf-8') as infile:
    # Open the output file for writing
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through each line in the input file
        for line in infile:
            # Strip leading and trailing whitespace from the line
            stripped_line = line.strip()
            # If the line is not a timestamp line, not a serial number, and not empty, write it to the output file
            if not timestamp_pattern.match(stripped_line) and not serial_number_pattern.match(stripped_line) and stripped_line:
                outfile.write(stripped_line + '\n')

