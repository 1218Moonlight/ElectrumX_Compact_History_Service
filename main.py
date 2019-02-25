from systemd import journal


def main():
    j = journal.Reader()
    j.this_boot()
    j.log_level(journal.LOG_INFO)
    j.add_match(_SYSTEMD_UNIT='electrumx.service')
    for entry in j:
        print(entry['MESSAGE'])


if __name__ == '__main__':
    main()
