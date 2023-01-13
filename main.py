import tabula

data = tabula.read_pdf("cns.pdf.pdf", pages="all")

print(data)

tabula.convert_into("cns.pdf.pdf" , "sample2.csv", pages = "all", output_format="csv")