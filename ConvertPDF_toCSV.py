import tabula

path = '2024-09 BBVA RVD Visa.pdf'

tables = tabula.read_pdf(path, pages=2)
print(type(tables))
print(len(tables))

table = tables[0]
print(table)