class PostalAddress:
    def __init__(self):
        self.country: str = None;
        self.city: str = None;
        self.zip_code: int = None;
        self.address: str = None;

class User:
    def __init__(self):
        self.identifier: int = -1;
        self.first_name: str = None;
        self.last_name: str = None;
        self.birth_date: int = -1;
        self.registration_date: int = -1;
        self.phone_number: str = None;
        self.email_address: str = None;
        self.postal_address: PostalAddress = PostalAddress();
        self.password: str = None;
        self.had_allready_buy_something: bool = False;