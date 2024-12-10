class fileHandler: 
    def __init__(self, file: str): 
        self.__filename = file
        self.__list1 = []
        self.__list2 = []
        
    def process_lists(self): 
        with open(self.__filename, "r") as file: 
            for line in file: 
                line = line.replace("\n", "")
                parts = line.split("   ")
                # print(parts)
                self.__list1.append(int(parts[0]))
                self.__list2.append(int(parts[1]))
            file.close()
            
    def compare_lists(self): 
        self.__list1.sort()
        self.__list2.sort()
        distances = []
        for i in range(len(self.__list1)):
            number1 = self.__list1[i]
            number2 = self.__list2[i]
            distances.append(abs(number1 - number2))
        return distances 
        
    def total_distance(self): 
        distances = self.compare_lists()
        return sum(distances)

    def total_similarity(self): 
        similarities = self.get_similarity()
        return sum(similarities)

    def get_similarity(self): 
        list2_dict = {}
        for number in self.__list2: 
            if number not in list2_dict: 
                list2_dict[number] = 1 
            else: 
                list2_dict[number] += 1
        # print(list2_dict)
        similarities = [number * list2_dict.get(number, 0) for number in self.__list1]
        # print(similarities)
        return similarities

my_file = fileHandler("day1.txt")
my_file.process_lists()
print(my_file.total_distance())
print(my_file.total_similarity())
