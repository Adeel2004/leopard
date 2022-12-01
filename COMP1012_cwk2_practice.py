"""
Please write your name
@author: Adeel Hussain

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv
class Leopard:

    def __init__(self, filepath: str) -> None:
        self.data = [[]]
        self.header = []
        self.row_min = 0
        self.row_max = 0
        self.row_total = 0
        self.row_count = 0
        self.row_mean = 0
        self.first = False
        self.headers_in_use = []


        with open(filepath, 'r') as file:
            if csv.reader(file) == None:
                print("file not found")
            reader = csv.reader(file)

            for first_row in reader:
                if first_row == None:
                    print("empty file")
                self.header.append(first_row)
                break

            for row in reader:
                self.data.append(row)
            self.header = self.header[0]
            self.data = self.data[1:]

    def get_header(self) -> list:
        if self.header != None:
            return self.header
        else:
            return None
    def get_data(self) -> list:
        if self.data != None:
            return self.data
        else:
            return None

    def stats(self) -> dict:
        stats = {}
        for i in range(len(self.data[0])):
            if self.data[0][i].isnumeric() == False:
              continue  
            self.headers_in_use.append(i)

        for x in self.headers_in_use:
            self.row_total = 0
            self.row_count = 0
            self.row_mean = 0
            self.row_min = 0
            self.row_max = 0
            self.first = False
            for y in range(len(self.data)):
                if self.data[y][x] == "NA" or self.data[y][x] == "-" or self.data[y][x] == "":
                    continue
                if self.first == False:
                    self.row_min = int(self.data[y][x])
                    self.first = True
                if self.row_min > int(self.data[y][x]):
                    self.row_min = int(self.data[y][x])
                if self.row_max < int(self.data[y][x]):
                    self.row_max = int(self.data[y][x])
                self.row_count+=1
                self.row_total+=int(self.data[y][x])
            self.row_mean = round((self.row_total/self.row_count), 2)

            stats[self.header[x]] = {}
            stats[self.header[x]]["count"] = self.row_count
            stats[self.header[x]]["mean"] = self.row_mean
            stats[self.header[x]]["min"] = self.row_min
            stats[self.header[x]]["max"] = self.row_max

        return stats

    def html_stats(self, stats: dict, filepath: str) -> None:
        with open(filepath,"w") as html:
            html.write("<html>\n")
            html.write("<head>\n")
            html.write("<meta charset=\"UTF-8\">\n")
            html.write("<style>\n")
            html.write("table, th, td {\n")
            html.write("border: 1px dashed black;\n")
            html.write("border-collapse: collapse;\n")
            html.write("}\n")
            html.write("</style>\n")
            html.write("<title>CSVs</title>\n")
            html.write("</head>\n")
            html.write("<body>\n")
            html.write("<h2>Stats</h2>\n")
            html.write("<table>\n")

            # format the table header 
            html.write("<tr>\n")
            html.write("<th> Column name</th>\n")    
            html.write("<th> Count</th>\n")
            html.write("<th> Mean</th>\n")
            html.write("<th> Minimum</th>\n")
            html.write("<th>Maximum</th>\n")
            html.write("</tr>\n")

            # iterate over the lines in the file printing out formatted html
            for item in stats:
                html.write("<tr>\n")
                html.write("<td>"+ item + "</td>\n")
                for element in stats[item]:
                    html.write("<td>"+ str(stats[item][element]) + "</td>\n")
                html.write("</tr>\n")

            # close all the opened html tags
            html.write("</table>\n")
            html.write("</body>\n")
            html.write("</html>\n")

    def count_instances(self, criteria) -> int:
        """
        Write your docstring to explain how to use this method.
        You are to decide what data type format is criteria or how many
        arguments to this method.
        Delete above and this comment to write your docstring.
        """
        # delete pass and this comment to write your code
        pass


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv")
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    print()

    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    print(test2.get_header())
    print(test.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    print()

    # test student.csv
    test3 = Leopard("student.csv")
    print(test3.get_header())
    print(test.get_data())
    stats3 = test3.stats()
    print(stats3)
    test3.html_stats(stats3, "student.html")

