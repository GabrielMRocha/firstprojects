import mysql.connector
import difflib


con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)



cursor = con.cursor()

word = input("Enter a bloddy word: ")

def dict(w):
    while True:
        w = w.lower()
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(w))
        results = cursor.fetchall()

        if results != []:
            result_list = [i[1] for i in results]
            return result_list

        else:
            query2 = cursor.execute("SELECT * FROM Dictionary")
            results2 = cursor.fetchall()
            results_dict = {}

            for tuple in results2:
                results_dict.setdefault(tuple[0],[]).append(tuple[1])

        if len(difflib.get_close_matches(w, results_dict.keys())) > 0:
             w = difflib.get_close_matches(w, results_dict.keys())[0]
             t = ""

             while (t != "Y" and t != "N"):
                 t = input("Can't you type, you twat?? Do you mean '{}'? Y or N? ".format(w.title())).upper()

                 if t == "Y":
                    print(w.title())
                    return results_dict[w]

                 elif t == "N":
                    w = input("Bollocks, enter a new word, then: ")
        else:
            w = input("That's no fucking word. Enter a new word, you wanker: ")


output = dict(word)

for i in output:
        print(i)


#len(difflib.get_close_matches(w, cursor.execute("SELECT * FROM Dictionary))) > 0:
