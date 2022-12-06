
LEN_OF_START_PACKET = 4
LEN_OF_MESSAGE_PACKET = 14


def determine_end_of_packet_marker(message):
    return determine_end_of_marker(message, LEN_OF_START_PACKET)


def determine_end_of_message_marker(message):
    return determine_end_of_marker(message, LEN_OF_MESSAGE_PACKET)


def determine_end_of_marker(message, len_of_marker):
    for i in range(len(message)):
        variant_end = i + len_of_marker
        variant = message[i:variant_end]
        is_start_of_packet = len(set(variant)) == len_of_marker
        if is_start_of_packet:
            last_position = variant_end
            break
    return last_position


def assert_packet_marker(str_input, result):
    assert determine_end_of_packet_marker(str_input) == result


def assert_message_marker(str_input, result):
    assert determine_end_of_message_marker(str_input) == result


def test_it():
    assert_packet_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 5)
    assert_packet_marker('nppdvjthqldpwncqszvftbrmjlhg', 6)
    assert_packet_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10)
    assert_packet_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)

    assert_message_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19)
    assert_message_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 23)
    assert_message_marker('nppdvjthqldpwncqszvftbrmjlhg', 23)
    assert_message_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)


test_it()
str_input = open("day6-input.txt", "r").read()
print(f"{determine_end_of_packet_marker(str_input)=}")
print(f"{determine_end_of_message_marker(str_input)=}")
