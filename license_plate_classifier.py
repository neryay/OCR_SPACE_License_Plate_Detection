import ocr_space_api_engine as ocr_eng
import licensePlate_string_parser as license_parser
import DB_Utils
import os
import datetime


def run():
    dataset_rel_path = 'images/'
    files = os.listdir(dataset_rel_path)
    vehicles = {license_parser.tables_names[0]: {},
                license_parser.tables_names[1]: {},
                license_parser.tables_names[2]: {},
                license_parser.tables_names[3]: {},
                license_parser.tables_names[4]: {}}

    for file in files:
        timestamp = datetime.datetime.now().__str__();
        license_plate = ocr_eng.get_text_file(dataset_rel_path + file)
        vehicle_type, license_plate = license_parser.license_plate_classification(license_plate)
        vehicles[vehicle_type][license_plate] = timestamp

    DB_Utils.run_database(vehicles)


