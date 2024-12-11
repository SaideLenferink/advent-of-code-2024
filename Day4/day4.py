import re

class FileHandler: 
    def __init__(self, filename: str):
        self.__filename = filename
        self.__monitoring = []
        
    def get_monitoring_lines(self): 
        with open(self.__filename, "r") as file: 
            for line in file: 
                line = line.replace("\n", "")
                self.__monitoring.append(line)
        file.close()
        return self.__monitoring
    
class MonitoringPart1: 
    def __init__(self, lines: list): 
        self.__lines = lines 
        self.__matches = 0
        
    def matches(self, pattern: str) -> int:
        self.find_pattern(pattern)
        return self.__matches
        
    def find_pattern(self, pattern: str):
        reversed = pattern[::-1]
        self.__matches += self.horizontal_search(pattern, self.__lines) 
        self.__matches += self.horizontal_search(reversed, self.__lines)
        self.__matches += self.vertical_search(pattern)
        self.__matches += self.vertical_search(reversed)
        self.__matches += self.diagonal_search_45(pattern)
        self.__matches += self.diagonal_search_45(reversed)
        self.__matches += self.diagonal_search_135(pattern)
        self.__matches += self.diagonal_search_135(reversed)
        
    def horizontal_search(self, pattern: str, lines: str) -> int: 
        matches = 0
        for line in lines:
            match: list = re.findall(f"(?={pattern})", line)
            matches += len(match)
        return matches
                
    def vertical_search(self, pattern: str) -> int: 
        rotated = ["".join(row) for row in zip(*self.__lines)]
        return self.horizontal_search(pattern, rotated)
    
    def diagonal_search_45(self, pattern: str) -> int: 
        y = len(self.__lines)
        x = len(self.__lines[0])
        diagonals = []
        
        for d in range(y + x - 1): 
            diagonal = [] 
            for i in range(max(0, d - x + 1), min(y, d + 1)): 
                j = d - i 
                diagonal.append(self.__lines[i][j])
            diagonals.append("".join(diagonal))
        # print(diagonals)
        return self.horizontal_search(pattern, diagonals)
        
    def diagonal_search_135(self, pattern: str) -> int: 
        y = len(self.__lines)
        x = len(self.__lines[0])
        diagonals = []
        
        for d in range(-(y - 1), x): 
            diagonal = [] 
            for i in range(max(0, -d), min(y, x - d)): 
                j = i + d
                diagonal.append(self.__lines[i][j])
            diagonals.append("".join(diagonal))
        # print(diagonals)
        return self.horizontal_search(pattern, diagonals)
        
    
    
my_file = FileHandler("input.txt")
monitoring_lines = MonitoringPart1(my_file.get_monitoring_lines())
print(monitoring_lines.matches("XMAS"))
