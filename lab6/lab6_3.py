import xmltodict

if __name__ == "__main__":
    with open('lab6/ex_3.xml', encoding="windows-1251") as rawXml:
        xmlDict = xmltodict.parse(rawXml.read(), encoding="windows-1251")
        for product in xmlDict["Файл"]["Документ"]["ТаблСчФакт"]["СведТов"]:
            print(f'Товар: {product["@НаимТов"]}, Количество: {product["@КолТов"]}, Цена: {product["@ЦенаТов"]}')