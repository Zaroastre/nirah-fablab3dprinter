class Credential:
    def __init__(self) -> None:
        self.username: str = None;
        self.password: str = None;

class User:
    def __init__(self) -> None:
        self.identifier: int = 0;

class WebService:
    def __init__(self) -> None:
        self.group_id: str = None;
        self.project_id: str = None;
        self.artifact_id: str = None;
        self.version: str = None;
        self.host: str = None;
        self.port: int = None;
