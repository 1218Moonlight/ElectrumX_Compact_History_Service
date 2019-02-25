from systemd import journal
from elecXjournal import manager

def main():
    j = manager.service(journal=journal)
    # j.testWatch()
    j.watch()

if __name__ == '__main__':
    main()
