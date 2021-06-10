from json import loads;

class ApplicationConfiguration:
    @staticmethod
    def load() -> dict:
        configuration: dict = None;
        with open("{}/{}".format(__file__.replace(__file__.replace("\\\\", '/').replace('\\', '/').split('/')[-1], ''), "manifest.json"), "r") as file:
            configuration = loads(file.read());
        return configuration;
