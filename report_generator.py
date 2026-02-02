import pandas as pd

data = pd.read_csv("data.csv")
print(data)


average = data["Marks"].mean()
highest = data["Marks"].max()
lowest = data["Marks"].min()


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("Automated_Report.pdf", pagesize=A4)
width, height = A4

pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "Automated Report")

pdf.setFont("Helvetica", 12)
pdf.drawString(50, height - 100, f"Average Marks: {average}")
pdf.drawString(50, height - 130, f"Highest Marks: {highest}")
pdf.drawString(50, height - 160, f"Lowest Marks: {lowest}")

y = height - 220
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(50, y, "Student Details:")

pdf.setFont("Helvetica", 11)
y -= 30

for index, row in data.iterrows():
    pdf.drawString(50, y, f"{row['Name']} - {row['Marks']}")
    y -= 20

pdf.save()
