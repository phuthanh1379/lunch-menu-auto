from encodings import utf_8
import camelot
import sys

file = str(sys.argv[1])

tables = camelot.read_pdf(file)

def get_menu(index):
    res = []
    day = "- thứ " + str(index + 1) + " -"
    res.append('/poll "Trưa nay ' + day + ' ăn gì" ')

    for i, item in enumerate(tables[0].df[index]):
        if i > 0 and i < 11:
            res.append('"' + item + '", ')
    
    filename = "menu-thu-" + str(index + 1) + ".txt"
    out = open(filename, "w+", encoding="utf_8")
    for line in res:
        out.write(line)
    out.close()

# Monday
get_menu(1)

# Tuesday
get_menu(2)

# Wednesday
get_menu(3)

# Thursday
get_menu(4)

# Friday
get_menu(5)