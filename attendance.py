import sys
import csv
import argparse


class Attendance:
    @staticmethod
    def run(config_name, output):
        config_file = open(config_name)
        people = Attendance.read_people_from_CSV(config_file)

        user_input = input("Swipe PolyCards...(\"quit\" to finish)\n")
        while user_input != 'quit' and user_input != 'exit':
            member_id = to_id(user_input)

            if member_id and member_id in people:
                people[member_id].here()
            else:
                print("ID doesn't exist in database")
            user_input = input()

        config_file = open(output, "w")
        Attendance.write_people_to_CSV(config_file, people)

    @staticmethod
    def read_people_from_csv(input_file):
        person_dict = {}
        reader = csv.DictReader(input_file, ['first', 'last', 'id'])

        for person in reader:
            person_dict[to_id(person['id'])] = Member(person['first'], person['last'])

        return person_dict

    @staticmethod
    def write_people_to_csv(output_file, person_dict):
        writer = csv.writer(output_file)

        for person in sorted(person_dict.values()):
            writer.writerow([person.first, person.last, "TRUE" if person.attended else "FALSE"])


def to_id(text):
    """
    Takes a string of text and returns the id from it. The id is defined as the
    string of 16 digits between the ';' and '?'. Ex:
    '%2015000000000^STUDENT?;6278561000000000?' -> '6278561000000000'. This
    function will also work if the 16 digits are passed in on their own.
    """
    if ';' in text:
        text = text.split(';')[1]
    return text.strip('?')


class Member():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.attended = False

    def __lt__(self, other):
        if isinstance(other, Member):
            if self.last == other.last:
                return self.first < other.first
            else:
                return self.last < other.last

    def here(self):
        self.attended = True
        print(self.first + " " + self.last)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="The name of a .csv file with columns 'First Name', 'Last Name', 'ISO Number'")
    parser.add_argument("output", help="The name of the output .csv file that will have columns 'First Name', "
                                       "'Last Name', 'Attendance'")
    args = parser.parse_args()
    Attendance.run(args.config, args.output)
