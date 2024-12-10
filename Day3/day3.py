class SearchFile:
    def __init__(self, filename: str):
        self.__filename = filename
        self.__computer_output = self.open_file()

    def open_file(self) -> str:
        computer_output = ""
        with open(self.__filename, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                computer_output += line
            file.close()
        return computer_output

    def find_operations(self) -> int:
        # Find and check possible operations
        start_statement = "mul("
        my_string = self.__computer_output
        total = 0
        enabled = True

        # Only continue if the substring can still be found in remaining string
        while start_statement in my_string:
            # Check if enabled. Search for new enable point if disabled.
            if not enabled:
                start_enable = my_string.find("do()")
                if start_enable == -1:  # Failsafe in case there is no more enable point
                    break
                my_string = my_string[start_enable:]
                enabled = True

            start_disable = my_string.find("don't()")
            start_index = my_string.find(start_statement)
            end_index = my_string.find(")", start_index)
            # Check if there is a disable statement
            if start_disable != -1 and start_disable < start_index:
                enabled = False
                continue
            # Isolate the, supposidly, operation between ( and )
            possible_operation = my_string[start_index + 4 : end_index]

            # Check if the closing bracket found incapsulates the operation matching the start_index
            # or that one of the next operation
            if start_statement in possible_operation:
                start_index = my_string.find(start_statement, start_index + 4)
                possible_operation = my_string[start_index + 4 : end_index]

            total += self.check_and_execute_operation(possible_operation)

            # Shorten the new_string to look for the next occurance
            my_string = my_string[end_index + 1 :]
        return total

    def check_and_execute_operation(self, text: str) -> int:
        if all(char in "0123456789," for char in text):
            values = text.split(",")
            if len(values) == 2:
                return int(values[0]) * int(values[1])
        return 0


my_file = SearchFile("input.txt")
print(my_file.find_operations())
