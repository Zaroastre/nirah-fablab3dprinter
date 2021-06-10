import re;
from configuration import ApplicationConfiguration;

class WebService:
    def __init__(self) -> None:
        self.group_id: str = None;
        self.project_id: str = None;
        self.artifact_id: str = None;
        self.version: str = None;
        self.host: str = None;
        self.port: int = None;
    
    @staticmethod
    def parse(json: dict):
        web_service: WebService = None;
        if (json != None):
            keys: dict = {};
            for json_key in json.keys():
                keys[json_key] = (json_key in WebService().__dict__.keys());
            if (not False in keys.values()):
                web_service = WebService();
                web_service.group_id = json.get("group_id");
                web_service.project_id = json.get("project_id");
                web_service.artifact_id = json.get("artifact_id");
                web_service.version = json.get("version");
                web_service.host = json.get("host");
                web_service.port = json.get("port");
        return web_service;

class Version:
    def __init__(self) -> None:
        self.major: int = -1;
        self.minor: int = -1;
        self.build: int = -1;
        self.tag: str = None;
        self.full: str = str(self);

    def __repr__(self):
        version: str = "";
        if (self.tag != None):
            version = "{}.{}.{}-{}".format(self.major, self.minor, self.build, self.tag);
        else:
            version = "{}.{}.{}".format(self.major, self.minor, self.build);
        return version;

    @staticmethod
    def parse(text: str):
        version: Version = None;
        if ((text != None) and (len(text) > 0)):
            pattern = re.compile(r"^[0-9]{1,}(\.[0-9]{1,}){2}(-[A-Za-z]{3,})?$");
            if (pattern.match(text)):
                version = Version();
                version_without_tag = text;
                if ('-' in text):
                    version_without_tag = text.split('-')[0];
                    version.tag = text.split('-')[1];
                version_parts: list = version_without_tag.split('.');
                version.major = int(version_parts[0]);
                version.minor = int(version_parts[1]);
                version.build = int(version_parts[2]);
                version.full = str(version);
        return version;

class RestErrorResponse:
    def __init__(self, ) -> None:
        self.code: str = None;
        self.reason: str = None;