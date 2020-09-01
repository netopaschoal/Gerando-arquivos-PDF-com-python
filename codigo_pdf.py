from reportlab.pdfgen import canvas
from PyQt5 import  uic,QtWidgets

lista_nomes = []


def listar_dados():
   dado_lido = lista.lineEdit.text()
   lista_nomes.append(dado_lido)
   lista.listWidget.addItem(dado_lido)
   lista.lineEdit.setText("")

def deletar():
    lista.listWidget.clear()
    lista_nomes.clear()


def gerar_pdf():
    y = 0
    pdf = canvas.Canvas("pdf_nomes.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(100,800, "Lista de nomes:")
    pdf.setFont("Times-Bold", 18)

    for nome in lista_nomes:
        y = y + 50
        pdf.drawString(100,800 - y, nome)

    pdf.save()
    print(lista_nomes)


app=QtWidgets.QApplication([])
lista=uic.loadUi("lista.ui")
lista.pushButton.clicked.connect(listar_dados)
lista.pushButton_2.clicked.connect(deletar)
lista.pushButton_3.clicked.connect(gerar_pdf)

lista.show()
app.exec()