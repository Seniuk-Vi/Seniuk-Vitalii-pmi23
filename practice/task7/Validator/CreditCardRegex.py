class CreditCardRegex:
    owner_name_regex = "^[a-zA-z ,.'-]+$"
    id_regex = "\\d{1,15}"
    card_regex = "(\\d{4}) (\\d{4}) (\\d{4}) (\\d{4})"
    cvc_regex = "\\d{3}"
