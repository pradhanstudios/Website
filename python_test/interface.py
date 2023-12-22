import pyscript as pys
from basic_functions import int_to_list

def int_to_list(event):
    integer = pys.document.querySelector("#integer")
    integer = int(integer)
    if integer > 0:
        output = pys.document.querySelector("#output")
        output.innerText = str(int_to_list(integer))