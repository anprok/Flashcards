import argparse
import collections
import logging
import random
import shutil
import sys

parser = argparse.ArgumentParser(description="This program creates flash cards, import and export cards. checks, "
                                             "provides stats.")
parser.add_argument("--import_from", dest='import_file', help='External file to read cards')
parser.add_argument("--export_to", dest='export_file', help="Filename to export after exit")
args = parser.parse_args()

logging.basicConfig(handlers=[logging.FileHandler("temp_file.log", mode='w'), logging.StreamHandler(sys.stdout)],
                    format="%(message)s",
                    level='DEBUG')

cards = dict()
errors_counter = collections.Counter()


def import_cards(cards_file):
    global i
    try:
        file = open(cards_file, 'r')
        i = 0
        for line in file:
            item = line.split(":")
            cards[item[0].strip()] = item[1].strip()
            i += 1
        logging.info("{} cards have been loaded.".format(i))
    except FileNotFoundError:
        logging.info("File not found.")


def export_cards_to_file(export_fn):
    name_file = open(export_fn, 'w', encoding='utf-8')
    for ic, jc in cards.items():
        name_file.write("{}:{}\n".format(ic, jc))
    name_file.close()
    logging.info("{} cards have been saved.".format(len(cards)))


if args.import_file:
    import_cards(args.import_file)


while True:
    logging.info("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
    command = input()
    logging.info(command)
    if command == 'add':
        logging.info("The card:")
        while True:
            card_term = input()
            logging.info(card_term)
            if len(cards.keys()) == 0 or card_term not in cards.keys():
                break
            else:
                logging.info('The term "{}" already exists. Try again:'.format(card_term))
        logging.info("The definition for card:")
        while True:
            card_def = input()
            logging.info(card_def)
            if len(cards.values()) == 0 or card_def not in cards.values():
                break
            else:
                logging.info('The definition "{}" already exists. Try again:'.format(card_def))
        cards[card_term] = card_def
        logging.info(" The pair {} has been added.".format((card_term, card_def)))

    elif command == 'remove':
        logging.info("Which card?")
        card_name = input()
        logging.info(card_name)
        try:
            cards.pop(card_name)
            logging.info("The card has been removed.")
        except KeyError:
            logging.info('Can\'t remove "{}": there is no such card.'.format(card_name))
    elif command == 'import':
        logging.info("File name:")
        import_file = input()
        import_cards(import_file)

    elif command == 'export':
        logging.info("File name:")
        export_file_name = input()
        export_cards_to_file(export_file_name)
    elif command == 'ask':
        logging.info("How many times to ask?")
        quests = int(input())

        for i in range(0, quests):
            card_key = random.choice(list(cards.keys()))
            answer = input('Print the definition of "{}":\n'.format(card_key))
            if answer == cards[card_key]:
                logging.info("Correct!")
            else:
                print_else = 1
                errors_counter[card_key] += 1
                for new_def, new_answer in cards.items():
                    if answer == new_answer:
                        logging.info('Wrong. The right answer is "{}", but your definition is correct for "{}".'.format(
                            cards[card_key], new_def))

                        print_else = 0
                        break

                if print_else:
                    logging.info('Wrong. The right answer is "{}".'.format(cards[card_key]))
    elif command == 'exit':
        if args.export_file:
            export_cards_to_file(args.export_file)
        logging.info("Bye bye!")
        break
    elif command == 'log':
        logging.info("File name:")
        fn = input()
        logging.info(fn)
        shutil.copy('temp_file.log', fn)
        logging.info("The log has been saved.")
    elif command == 'hardest card':
        errors_list = list()
        most_common = errors_counter.most_common()

        if len(most_common):
            max_errors = most_common[0][1]
            errors_list.append(most_common[0][0])
            i = 1
            while most_common[i][1] == max_errors and i < len(most_common):
                errors_list.append(most_common[i][0])
                i += 1
        if len(errors_list) > 1:
            logging.info('The hardest cards are "{}"'.format("\", ".join(errors_list)))
        elif len(errors_list) == 1:
            logging.info('The hardest card is "{}". You have {} errors answering it'.format(*errors_list, max_errors))
        else:
            logging.info('There are no cards with errors.')

    elif command == 'reset stats':
        errors_counter.clear()
        logging.info("Card statistics have been reset")

    else:
        logging.info("Incorrect command")
