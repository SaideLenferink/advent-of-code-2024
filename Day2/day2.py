class FileHandler:
    def __init__(self, filename: str):
        self.__filename = filename

    def process_file(self) -> list:
        my_file = []
        with open(self.__filename, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                my_file.append(line)
            file.close()
        return my_file


class Reports:
    def __init__(self, reports: list):
        self.__reports = reports

    def check_safety(self, dampener: bool):
        safe = 0
        for report in self.__reports:
            if dampener:
                if self.is_safe_with_removal(report):
                    safe += 1
            else:
                if self.is_safe(report):
                    safe += 1
        return safe

    def is_safe(self, report: str):
        levels = report.split(" ")
        levels = [int(level) for level in levels]
        diff = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
        if not all(d in [-3, -2, -1, 1, 2, 3] for d in diff):
            return False
        if all(d in [-3, -2, -1] for d in diff) or all(d in [1, 2, 3] for d in diff):
            return True
        return False

    def is_safe_with_removal(self, report: str):
        levels = report.split(" ")
        levels = [int(level) for level in levels]

        if self.is_safe(report):
            return True

        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i + 1 :]
            new_report = " ".join(map(str, new_levels))
            if self.is_safe(new_report):
                return True

        return False


input = FileHandler("input.txt")
reports = Reports(input.process_file())
print(reports.check_safety(False))
print(reports.check_safety(True))
