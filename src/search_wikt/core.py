import sys
import argparse
import wiktionaryparser
import configparser
import pathlib

# creates and reads the config file


def write_prefs(language="Old English", etymology=True,
                ipa=True, examples=False, related_words=False):
    config = configparser.ConfigParser()
    config["Default"] = {"Language": language,
                         "Etymology": etymology,
                         "IPA": ipa,
                         "Examples": examples,
                         "Related Words": related_words
                         }
    with open("config.ini", "w") as configfile:
        config.write(configfile)

    return config


def read_prefs():
    config = configparser.ConfigParser()
    with open("config.ini", "r") as configfile:
        config.read_file(configfile)

    return config


check_prefs = pathlib.Path("config.ini")
if check_prefs.is_file():
    prefs = read_prefs()
else:
    prefs = write_prefs()

# handles command line inputs with argparse


def check_truth(line):
    return line == "True"


parser = argparse.ArgumentParser(
        description="Search Wiktionary is a simple command line"
                    " utility for Wiktionary that uses WiktionaryParser ("
                    "https://github.com/Suyash458/WiktionaryParser).",
        epilog="\nWiktionary definitions are licensed under CC BY-SA 4.0."
               "\nvisit Wiktionary at wiktionary.org."
        )
parser.add_argument(
        "word",
        help="choose the word you would like to search.")
parser.add_argument(
        "-l",
        "--language",
        type=str,
        default=prefs["Default"]["Language"],
        help="choose the language you would like to search."
        )
parser.add_argument(
       "-e",
       "--etymology",
       action="store_false",
       default=check_truth(prefs["Default"]["Etymology"]),
       help="display your word's etymology. enabled by default."
       )
parser.add_argument(
        "-i",
        "--ipa",
        action="store_false",
        default=check_truth(prefs["Default"]["IPA"]),
        help="display phonetic information about your word."
             " enabled by defualt."
        )
parser.add_argument(
        "-ex",
        "--examples",
        action="store_true",
        default=check_truth(prefs["Default"]["Examples"]),
        help="display examples of your word being used if possible."
        )
parser.add_argument(
        "-r",
        "--related",
        action="store_true",
        default=check_truth(prefs["Default"]["Related Words"]),
        help="display related words if possible."
        )

default_behaviours = parser.add_mutually_exclusive_group()
default_behaviours.add_argument(
        "-d",
        "--default",
        action="store_true",
        help="save your current options to the program's default settings."
        )
default_behaviours.add_argument(
        "-rd",
        "--restore_defaults",
        action="store_true",
        help="restore the program's initial default settings."
        )

args = parser.parse_args()

if args.default:
    prefs = write_prefs(
            language=args.language,
            etymology=args.etymology,
            ipa=args.ipa,
            examples=args.examples,
            related_words=args.related,
            )

if args.restore_defaults:
    prefs = write_prefs()


# grabs the definition with wiktionaryparser

scraper = wiktionaryparser.WiktionaryParser()


def get_definition(word, language):
    definition = scraper.fetch(word, language)
    return definition


wikt_page = get_definition(args.word, args.language)

# parses the definitions returned by wiktionaryparser and prints them


class Entry:
    def __init__(self, page):
        self.etymology = page["etymology"]
        self.ipa = page["pronunciations"]["text"]

        try:
            self.definitions = page["definitions"][0]
        except IndexError:
            print("Looks like Wiktionary doesn't have that word, sorry!")
            sys.exit(1)

        self.wordclass = self.definitions["partOfSpeech"]
        self.meanings = self.definitions["text"]
        self.examples = self.definitions["examples"]

        self.related_words_list = self.definitions["relatedWords"]


def print_encoded(statement):
    print(statement.encode("utf-8"))


def print_container(container):
    for item in container:
        print(item.encode("utf-8"))


if wikt_page:
    for index, lexical_item in enumerate(wikt_page):
        content = Entry(lexical_item)

        if len(wikt_page) > 1:
            print_encoded(f"{args.word} {index + 1}\n")
        else:
            print_encoded(f"{args.word}\n")

        if args.etymology:
            print_encoded(content.etymology)

        if args.ipa:
            print_container(content.ipa)

        print_encoded(content.wordclass)
        print_container(content.meanings)

        if args.examples:
            print("\n")
            print_container(content.examples)

        if args.related:
            for item in content.related_words_list:
                print_encoded(f"\n{item['relationshipType']}")
                print_container(item["words"])
else:
    print("Wiktionary doesn't seem to have that language, sorry!")
    sys.exit(1)
