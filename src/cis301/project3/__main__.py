import sys
from cis301.projects.file_io import Util
from cis301.projects.phonebook import Person, Phonebook


def main(args=None):
    """
     This program that parses the command line, creates a
     Student, and prints a description of the student to
     standard out by invoking its toString method.
     """
    if args is None:
        args = sys.argv[1:]
    print(args)
    parse_cli_argv(args)

    print(f">>> Project3. Missing command line arguments")


def parse_cli_argv(argv):
    # check for options
    ##check for -README
    if "-README" in argv and argv.index("-README") < 2:
        # poistion of Readme
        print(usage())
        return ()
    elif "-README" in argv and argv.index("-README") > 1:
        print(usage())
        return ()
    else:
        pass
    ## check for -print
    if "-print" in argv and argv.index("-print") == 0:
        flag_printopt = True
        print("-print detected!")
    else:
        print(usage())
        return ()
    # check number of arguments, we are expecting 7 args + options


def usage():
    help = 'usage: project2 [options] <args> args are (in this order):\n' + \
           '\tcustomer\t\tPerson whose phone bill we’re modeling\n' + \
           '\tcallerNumber\t\tPhone number of caller\n' + \
           '\tcalleeNumber\t\tPhone number of person who was called\n' + \
           '\tstartTime\t\tDate and time call began (24-hour time)\n' + \
           '\tendTime\t\t\tDate and time call ended (24-hour time)\n' + \
           'options are (options may appear in any order):\n' + \
           '\t-print\t\t\tPrints a description of the new phone call\n' + \
           '\t-README\t\t\tPrints a README for this project and exits\n' + \
           '\t-textfile file\t\t\tWhere to read/write the\n' + \
           'Date and time should be in the format: mm/dd/yyyy hh:mm'



if __name__ == "__main__":
    person1 = Person('Kennedy', 'kennedy@cau.edu', '123-233-4444', '234-443-4422')
    phonebook = PhoneBook('cis301')
    phonebook.add_contact(person1)
    Util.saveCSV_phonebook(phonebook)
    phonebook_contacts_copy = Util.readCSV_phonebook('..\\Data\\phonebook.csv')
    assert (phonebook.contacts[0] == phonebook_contacts_copy[0])
    Util.to_pickle(phonebook, '..\\Data\\phonebook.dat')
    phonebook_from_pickle = Util.from_pickle('..\\Data\\phonebook.dat')
    assert (phonebook.owner == phonebook_from_pickle.owner)
    Util.toJSON('..\\Data\\phonebook.dat', phonebook.toJSON())
    phonebook_from_json = Util.fromJSON('..\\Data\\phonebook.json')

    main()