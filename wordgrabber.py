import Funcs as fs
receivers = ['isaaczucker006@gmail.com', 'mnassi2025@kehillahstudent.org', 'jadelberg2025@kehillahstudent.org', "esobel2025@kehillahstudent.org", "egoldhaberfiebert2025@kehillahstudent.org", "jlipman2025@kehillahstudent.org", "mwasserstein2025@kehillahstudent.org"]
word = fs.wordOfDay()
print("write your password")
password = input()
for i in receivers: 

    fs.emailsend(i, "botpython062@gmail.com", password, "CS 101 NEEDS YOUR HELP!", word)





