#day 6
my_file = open("input_2022_d6.txt", "r")
content = my_file.read()
puzzle_input_d6 = content.strip()
my_file.close()

def signal_processor(signal):
    for index, char in enumerate(signal):
        if index < 3:
            pass
        elif index >= 3:
            marker = signal[index-3:index+1]
            check = set(marker)
            if len(check) == 4:
                start_of_packet = len(signal[0:index+1])
                break
    return start_of_packet

def message_processor(signal):
    for index, char in enumerate(signal):
        if index < 13:
            pass
        elif index >= 13:
            marker = signal[index-13:index+1]
            check = set(marker)
            if len(check) == 14:
                start_of_message = len(signal[0:index+1])
                break
    return start_of_message

#pt.1 answer
signal_processor(puzzle_input_d6)

#pt.2 answer
message_processor(puzzle_input_d6)
