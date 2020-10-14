import os
#
# print(os.path.join("users",
#                    "python",
#                    "desktop",
#                    "text.odt"))
#
# st = open("tekst.odt", "w")
# st.write("napisalem to w pythonie! a teraz to zmienilem!")
# st.close()
#
# with open("tekst_with.odt", "w") as f:
#     f.write("teraz python napisal to sam!")

# with open("tekst.odt", "r") as f:
#     print (f.read())

my_list = list()

with open("tekst.odt", "r") as f:
    my_list.append(f.read())

print(my_list)
