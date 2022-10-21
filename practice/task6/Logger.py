class Logger:
    line = 0

    @staticmethod
    def write_to_file(my_list, file_name="logs.txt"):
        if Logger.line == 0:
            Logger.erase_file(file_name)
        f = open(file_name, 'a')
        f.write(str(Logger.line) + " " + str(my_list) + '\n')
        f.close()
        Logger.line += 1

    @staticmethod
    def erase_file(file_name):
        open(file_name, 'w').close()
