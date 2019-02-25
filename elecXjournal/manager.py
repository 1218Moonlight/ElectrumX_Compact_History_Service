class service:
    def __init__(self, journal):
        self.__j = journal
        self.__jr = journal.Reader()
        self.__set()

    def __set(self):
        self.__jr.log_level(self.__j.LOG_INFO)
        self.__jr.add_match(_SYSTEMD_UNIT='electrumx.service')
        self.__jr.seek_tail()
        self.__jr.get_previous()

    def testWatch(self):
        msg = ["flush #78 took 0.0s.  Height 278,249 txs: 335,337",
               "flush #178 took 0.0s.  Height 278,249 txs: 335,337",
               "flush #1,178 took 0.0s.  Height 278,249 txs: 335,337",
               "flush #65,535 took 0.0s.  Height 278,249 txs: 335,337",
               "flush #60,010 took 0.0s.  Height 278,249 txs: 335,337"]
        for v in msg:
            self.__filter(v)

    def watch(self):
        while True:
            event = self.__jr.wait(-1)
            if event == self.__j.APPEND:
                for entry in self.__jr:
                    self.__filter(entry['MESSAGE'])

    def __filter(self, msg):
        if 'flush' in msg and '#' in msg:
            self.__verification(msg[msg.find('#'):msg.find("took")].strip().replace("#", "").replace(",", ""))

    def __verification(self, msg):
        try:
            if int(msg) > 60000:
                print("compact")
        except:
            print("Error Type", msg)
