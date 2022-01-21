from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


env = Environment(loader=FileSystemLoader('templates/'))
template = env.get_template("table.html")

# Fill in the multiplication table in <tr><td>

multiplicator = 5
tr_td = ""
for i in range(21):
    tr_td += "<tr><td>{} × {}</td><td>{}</td></tr>".format(multiplicator, i, multiplicator*i)

# Render the HTML
variables = {
    "table_tr_td": tr_td,
    "multiplicator": multiplicator
}
html = template.render(variables)

# Dump the HTML in PDF
HTML(string=html).write_pdf("table_de_{}.pdf".format(multiplicator))

print("Done!")

