from systemd import journal
from elecXjournal import manager

def main():
    j = manager.service(journal=journal)
    j.testWatch()


if __name__ == '__main__':
    main()
