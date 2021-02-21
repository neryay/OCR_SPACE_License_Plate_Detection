import re


_public_trans_indicator = ['25', '26']
_prohibited_7_digits_license_suffix = ['85', '86', '87', '88', '89', '00']
_license_plate_lengths = [7, 8]

tables_names = ('Public_Transportation',
                'Military_and_Law',
                'prohibited_7_digits_plates',
                'Gas_Operated',
                'Permitted')


def license_plate_classification(license_plate):
    if license_plate is None:
        return None

    nonAlphe_plate = __remove_nonAlpha(license_plate)

    if __is_public_transport(nonAlphe_plate):
        return tables_names[0], nonAlphe_plate

    elif __is_military_law_english(license_plate):
        return tables_names[1], nonAlphe_plate

    elif __is_7_digits_suffix(nonAlphe_plate):
        return tables_names[2], nonAlphe_plate

    elif __is_gas_operated(nonAlphe_plate):
        return tables_names[3], nonAlphe_plate

    else:
        return tables_names[4], nonAlphe_plate


def __remove_nonAlpha(license_plate):
    return re.sub(r'[^0-9]', '', license_plate)


def __is_gas_operated(license_plate):
    return len(license_plate) in _license_plate_lengths \
           and (sum(int(value) for value in license_plate) % 7) == 0


def __is_7_digits_suffix(license_plate):
    return license_plate[-2:] in _prohibited_7_digits_license_suffix


def __is_military_law_english(license_plate):
    return re.search('[a-zA-Z]', license_plate)


def __is_public_transport(license_plate):
    return license_plate[-2:] in _public_trans_indicator
