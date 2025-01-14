import xml.etree.ElementTree as ET


if __name__ == "__main__":
    tree = ET.parse("lab6/ex_2.xml")
    root = tree.getroot()

    detail = root.find("Detail")

    new_item = ET.SubElement(detail, "Item")
    ET.SubElement(new_item, "ArtName").text = "Сыр Чеддер"
    ET.SubElement(new_item, "Barcode").text = "2000000000131"
    ET.SubElement(new_item, "QNT").text = "100.5"
    ET.SubElement(new_item, "QNTPack").text = "100.5"
    ET.SubElement(new_item, "Unit").text = "шт"
    ET.SubElement(new_item, "SN1").text = "00000015"
    ET.SubElement(new_item, "SN2").text = "24.12.2024"
    ET.SubElement(new_item, "QNTRows").text = "10"

    summary = root.find("Summary")
    old_sum = float(summary.find("Summ").text.replace(",", "."))
    old_rows = int(summary.find("SummRows").text)

    new_sum = old_sum + 100.5
    new_rows = old_rows + 10

    summary.find("Summ").text = f"{new_sum:.2f}".replace(".", ",")
    summary.find("SummRows").text = str(new_rows)

    tree.write("lab6/ex_2_modified.xml", encoding="utf-8", xml_declaration=True)
