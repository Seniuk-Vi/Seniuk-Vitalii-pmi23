class Logger:
    line = 1
    file_name = "logger.txt"

    @staticmethod
    def write_to_file(changes):
        if Logger.line == 1:
            Logger.erase_file()
        f = open(Logger.file_name, 'a')
        f.write(f"{Logger.line} " + str(changes) + '\n')
        f.close()
        Logger.line += 1

    @staticmethod
    def erase_file():
        open(Logger.file_name, 'w').close()
