import os

from openpyxl import Workbook


class ExcelExporter:

    EXPORT_DIR = "exports"

    def __init__(self):
        os.makedirs(self.EXPORT_DIR, exist_ok=True)

    def export(
        self,
        filename: str,
        data: dict
    ):

        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "Analytics"

        sheet.append(
            ["Metric", "Value"]
        )

        for key, value in data.items():

            sheet.append(
                [key, value]
            )

        file_path = os.path.join(
            self.EXPORT_DIR,
            filename
        )

        workbook.save(file_path)

        return file_path