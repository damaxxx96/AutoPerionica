import datetime

class Logger:
    def log(self, poruka):
        f = open("log.txt", "a")
        f.write("--------------------------\n")
        f.write(poruka + '\n')
        f.write("Datuma " + str(datetime.datetime.now()) + '\n')
        f.write("--------------------------\n")
        f.close()
