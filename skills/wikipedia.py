import wikipedia

wikipedia.set_lang("es")


class Wikipedia(object):
    __instance = None

    def __new__(cls):
        if Wikipedia.__instance is None:
            Wikipedia.__instance = object.__new__(cls)
        return Wikipedia.__instance

    def init(self, intent):
        search = intent.placeholder['search']
        result = wikipedia.summary(search)

        return result

    def skill_exit(self):
        pass

    def kill(self):
        pass
