import os
from xml.dom import minidom


class LectorXML:

    def Lector(self):
        directorio=os.path.dirname(os.path.abspath(__file__))

        doc = minidom.parse(f"{directorio}/EjemploimpuestoTrasladado.xml")

        print("")
        Comprobante = doc.getElementsByTagName("cfdi:Comprobante")
        for datos in Comprobante:
            Total = datos.getAttribute("Total")
            Moneda = datos.getAttribute("Moneda")
            print(f"Total de factura: {Total} {Moneda}")

        Emisor = doc.getElementsByTagName("cfdi:Emisor")
        for datos in Emisor:
            RFC_Emisor = datos.getAttribute("Rfc")
            print(f"RFC emisor: {RFC_Emisor}")

        Receptor = doc.getElementsByTagName("cfdi:Receptor")
        for datos in Receptor:
            RFC_Receptor = datos.getAttribute("Rfc")
            print(f"RFC receptor: {RFC_Receptor}")

lector = LectorXML()
lector.Lector()