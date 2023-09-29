from barcode import EAN13

number = '7896253401557'
my_code = EAN13(number)
my_code.save("new_code")