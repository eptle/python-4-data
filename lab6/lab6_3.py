import xmltodict

if __name__ == "__main__":
    with open('lab6/ex_3.xml', encoding="windows-1251") as raw_xml:
        xml_dict = xmltodict.parse(raw_xml.read(), encoding="windows-1251")
        for product in xml_dict["Файл"]["Документ"]["ТаблСчФакт"]["СведТов"]:
            print(f'Товар: {product["@НаимТов"]}, Количество: {product["@КолТов"]}, Цена: {product["@ЦенаТов"]}')