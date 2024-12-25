import xmlschema

if __name__ == "__main__":
    with open("lab6/ex_1.xsd") as scheme_file:
        scheme = xmlschema.XMLSchema(scheme_file)
        print(scheme.is_valid('lab6/ex_1.xml'))
        print(scheme.is_valid('lab6/ex_1 error.xml'))