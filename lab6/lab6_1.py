import xmlschema

if __name__ == "__main__":
    with open("lab6/ex_1.xsd") as schemeFile:
        scheme = xmlschema.XMLSchema(schemeFile)
        print(scheme.is_valid('lab6/ex_1.xml'))
        print(scheme.is_valid('lab6/ex_1 error.xml'))