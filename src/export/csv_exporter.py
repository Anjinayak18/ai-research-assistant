import os
import csv


class CSVExporter:

    EXPORT_DIR = "exports"

    def __init__(self):
        os.makedirs(self.EXPORT_DIR, exist_ok=True)

    def export(
        self,
        filename: str,
        data: dict
    ):

        file_path = os.path.join(
            self.EXPORT_DIR,
            filename
        )

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow(
                ["Metric", "Value"]
            )

            for key, value in data.items():

                writer.writerow(
                    [key, value]
                )

        return file_path