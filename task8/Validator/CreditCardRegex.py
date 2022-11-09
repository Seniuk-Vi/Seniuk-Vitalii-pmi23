class CreditCardRegex:
    owner_name_regex = "^[a-zA-z ,.'-]+$"
    id_regex = "\\d{1,15}"
    card_regex = "(\\d{4}) (\\d{4}) (\\d{4}) (\\d{4})"
    cvc_regex = "\\d{3}"
    email_regex = "^[^@\s]+@[^@\s\.]+\.[^@\.\s]+$"
    password_regex = "(?=.*[a-z])(?=.*[A-Z])\w+"
