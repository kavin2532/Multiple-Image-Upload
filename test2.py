import typing
from decimal import Decimal
from borb.pdf.document import document
from borb.pdf.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.toolkit.location.location_filter import LocationFilter
from borb.toolkit.text.regular_expression_text_extraction import RegularExpressionTextExtraction, PDFMatch
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction

def from_Address() -> Rectangle:    # this means that from_address will return rectangle variable

    d: typing.Optional[document] = None

    # This implementation of EventListener allows you to search for regular expressions in a PDF Document
    l: RegularExpressionTextExtraction = RegularExpressionTextExtraction("J SAKTHI")
    with open("001-J-ARAVIND.pdf", "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l])

    assert d is not None   #The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.

    matches: typing.List[PDFMatch] = l.get_matches_for_page(0)
    assert len(matches) == 1

    return matches[0].get_bounding_boxes()[0]


def to_Address() -> Rectangle:
    e: typing.Optional[document]=None
    j:RegularExpressionTextExtraction =RegularExpressionTextExtraction("DESCRIPTION")
    with open("001-J-ARAVIND.pdf","rb")as to_addr:
        d=PDF.loads(to_addr,[j])
    assert d is not None

    matchword: typing.List[PDFMatch] =j.get_matches_for_page(0)
    assert len(matchword) == 1

    return matchword[0].get_bounding_boxes()[0]

def Billed_To_invoice() -> Rectangle:
    e: typing.Optional[document]=None
    j:RegularExpressionTextExtraction =RegularExpressionTextExtraction("SAKTHIJ")
    with open("Invoice_425561.pdf","rb")as to_addr:
        d=PDF.loads(to_addr,[j])
    assert d is not None

    matchwords: typing.List[PDFMatch] =j.get_matches_for_page(0)
    assert len(matchwords) == 1

    return matchwords[0].get_bounding_boxes()[0]


def from_address_invoice() -> Rectangle:
    e: typing.Optional[document]=None
    j:RegularExpressionTextExtraction =RegularExpressionTextExtraction("BilledTo")
    with open("Invoice_425561.pdf","rb")as to_addr:
        d=PDF.loads(to_addr,[j])
    
    assert d is not None

    matchword: typing.List[PDFMatch] =j.get_matches_for_page(0)
    #print(matchword)
    assert len(matchword) == 1

    return matchword[0].get_bounding_boxes()[0]

def main():

    d: typing.Optional[document] = None

    # Define rectangle of interest
    from_Address_rect: Rectangle = from_Address()
    r: Rectangle = Rectangle(from_Address_rect.get_x() - Decimal(50), #x position
                             from_Address_rect.get_y() - Decimal(100), # y position
                             Decimal(200), #width position
                             Decimal(130))  #height position

    # Set up EventListener(s)
    l0: LocationFilter = LocationFilter(r)
    l1: SimpleTextExtraction = SimpleTextExtraction()
    l0.add_listener(l1)

    with open("001-J-ARAVIND.pdf", "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l0])

    assert d is not None
    print("----------FROM ADDRESS    ARAVIND.PDF--------")
    arv_from_output=l1.get_text_for_page(0)
    print("\n".join(arv_from_output.split("\n")[1:]))


#######################################################################################################3

    to_Address_rect: Rectangle = to_Address()
    s: Rectangle = Rectangle(to_Address_rect.get_x() - Decimal(20),
                             to_Address_rect.get_y() - Decimal(100),
                             Decimal(200),
                             Decimal(130)) 

    # Set up EventListener(s)
    l01: LocationFilter = LocationFilter(s)
    l11: SimpleTextExtraction = SimpleTextExtraction()
    l01.add_listener(l11)

    with open("001-J-ARAVIND.pdf", "rb") as pdf_in_handle:
        d1 = PDF.loads(pdf_in_handle, [l01])

    assert d1 is not None
    print("---------BILL ADDRESS  ARAVIND.PDF--------")

    arv_bill_output=l11.get_text_for_page(0)
    print("\n".join(arv_bill_output.split("\n")[1:]))


#######################################################################################################3

    Billed_To_invoice_rect: Rectangle = Billed_To_invoice()
    s: Rectangle = Rectangle(Billed_To_invoice_rect.get_x() - Decimal(10),
                             Billed_To_invoice_rect.get_y() - Decimal(100),
                             Decimal(200),
                             Decimal(130)) 

    # Set up EventListener(s)
    l01: LocationFilter = LocationFilter(s)
    l11: SimpleTextExtraction = SimpleTextExtraction()
    l01.add_listener(l11)

    with open("Invoice_425561.pdf", "rb") as pdf_in_handle:
        d1 = PDF.loads(pdf_in_handle, [l01])

    assert d1 is not None
    print("---------FROM ADDRESS  Invoice PDF--------")

    inv_from_output=l11.get_text_for_page(0)
    print("\n".join(inv_from_output.split("\n")[2:]))
   




#######################################################################################################3

    from_address_invoice_rect: Rectangle = from_address_invoice()
    s: Rectangle = Rectangle(from_address_invoice_rect.get_x() - Decimal(65), # get podition from right to left
                             from_address_invoice_rect.get_y() - Decimal(150),# get position from up to down
                             Decimal(200),
                             Decimal(130)) 

    # Set up EventListener(s)
    l01: LocationFilter = LocationFilter(s)
    l11: SimpleTextExtraction = SimpleTextExtraction()
    l01.add_listener(l11)

    with open("Invoice_425561.pdf", "rb") as pdf_in_handle:
        d1 = PDF.loads(pdf_in_handle, [l01])

    assert d1 is not None
    print("---------BILLED TO ADDRESS for invoice PDF--------")

    inv_bill_output=l11.get_text_for_page(0)
    print("\n".join(inv_bill_output.split("\n")[1:]))
    

#######################################################################################################


    # d:typing.Optional[Document]= None
    # q:SimpleTextExtraction =SimpleTextExtraction()
    # with open("Invoice_425561.pdf","rb") as pdf_text:
    #     d=PDF.loads(pdf_text, [q])

    # assert d is not None
    # #print(q.get_text_for_page(0))


if __name__ == "__main__":
    main()