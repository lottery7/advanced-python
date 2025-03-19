import os

from texgen import generate_document, generate_image, generate_table

if __name__ == "__main__":
    table_tex = generate_table(
        [
            ["Item", "Quantity"],
            ["Widgets", 42],
            ["Gadgets", 13],
        ],
        centering=False,
        caption="",
    )

    os.makedirs("artifacts", exist_ok=True)
    with open(os.path.join("artifacts", "table.tex"), "w") as file_tex:
        file_tex.write(generate_document(table_tex))
