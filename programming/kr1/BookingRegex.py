class BookingRegex:
    price = "^[0-9]*\.[0-9][0-9]$"
    year = "^[0-2][0-9][0-9][0-9]$"
    day = "^[0-31]$"
    driver_name_regex = "^[a-zA-z]+$"
    name = "^[a-zA-z ,.'-]+$"

