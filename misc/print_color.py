class bcolors:
    '''color sets for print function
    source: https://stackoverflow.com/a/287944
    '''

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_green(string):
    print(bcolors.OKGREEN + string + bcolors.ENDC)


def print_blue(string):
    print(bcolors.OKBLUE + string + bcolors.ENDC)


def print_yellow(string):
    print(bcolors.WARNING + string + bcolors.ENDC)


def print_red(string):
    print(bcolors.FAIL + string + bcolors.ENDC)


