from util import print_banner, print_help
from commands import send_message, purge, receive_messages, clear_console

def user_interaction_dialog():
    print_help()
    while True:
        queue_name = input("Please provide queue name (e. g. scheduling-queue)\n")

        if queue_name == "end":
            break

        while True:
            command = input(f"({queue_name}) What do you want to do:\n")
            if command == "1":
                file_name = input(f"({queue_name}) Please provide payload file name:\n")
                send_message(queue_name, file_name)
            elif command == "2":
                purge(queue_name)
            elif command == "3":
                receive_messages(queue_name)
            elif command == "help":
                print_help()
            elif command == "end":
                exit()
            elif command == "reset":
                break
            elif command == "clear":
                clear_console()
            else:
                print("Please provide a valid command!\n")    


if __name__ == "__main__":
    print_banner()
    user_interaction_dialog()