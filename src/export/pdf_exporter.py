import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


class PDFExporter:

    EXPORT_DIR = "exports"

    def __init__(self):
        os.makedirs(self.EXPORT_DIR, exist_ok=True)

    def export(
        self,
        filename: str,
        title: str,
        content: str
    ):

        file_path = os.path.join(
            self.EXPORT_DIR,
            filename
        )

        document = SimpleDocTemplate(file_path)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(f"<b>{title}</b>", styles["Heading1"])
        )

        story.append(
            Paragraph(content, styles["BodyText"])
        )

        document.build(story)

        return file_path