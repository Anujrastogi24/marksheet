# import PyPDF2
#
#
# file = 'sbi.pdf'
# writer = PyPDF2.PdfWriter()
# reader = PyPDF2.PdfReader(file)
# #
# # if reader.is_encrypted:
# #     reader.decrypt('7548557311')
# #
# for page in reader.pages:
#     writer.add_page(page)
#
# # 7559205526
# pdf_permissions_flag_bin = '0b1101110000'
#
# pdf_permissions_flag_int = int(pdf_permissions_flag_bin, 2)
#
# writer.encrypt('7559205526', use_128bit=True, permissions_flag=pdf_permissions_flag_int)
# with open("sbi1.pdf", 'wb') as file:
#     writer.write(file)



from datetime import datetime
from pypdf import PdfReader, PdfWriter

reader = PdfReader(".pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

metadata = reader.metadata
print(metadata)
writer.add_metadata(metadata)
utc_time = "+05'30'"
time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")
writer.add_metadata(
    {

        "/Producer": "iText 2.0.4 (by lowagie.com)",
        "/CreationDate": time,
        "/ModDate": time,

    }
)

# Save the new PDF to a file
with open("meta-pdf.pdf", "wb") as f:
    writer.write(f)
