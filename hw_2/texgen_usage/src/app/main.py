import os
import tempfile

from pdflatex import PDFLaTeX
from texgen import *


def generate_pdf(path_to_tex: str, path_to_pdf: str) -> None:
    pdf_bytes, _, _ = PDFLaTeX.from_texfile(path_to_tex).create_pdf()
    with open(path_to_pdf, "wb") as file:
        file.write(pdf_bytes)


if __name__ == "__main__":
    table_tex = generate_table(
        [
            ["Item", "Quantity"],
            ["Widgets", 42],
            ["Gadgets", 13],
        ],
        centering=True,
        caption="Very interesting table",
    )

    image_tex = generate_image(
        os.path.join("res", "frog.png"),
        width_factor=0.8,
        centering=True,
        caption="Cute Frog!",
    )

    doc_tex = generate_document(table_tex + image_tex, ["graphicx"])

    os.makedirs("artifacts", exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp_dir:
        doc_tex_path = os.path.join(tmp_dir, "doc.tex")
        with open(doc_tex_path, "w") as file_tex:
            file_tex.write(doc_tex)

        generate_pdf(doc_tex_path, os.path.join("artifacts", "doc.pdf"))
