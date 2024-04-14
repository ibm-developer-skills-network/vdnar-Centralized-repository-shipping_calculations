# /modules/converter.py


def calculate_cbm_shipping_unit_price(x, y, z, l, u):
    '''
    Converts dimensions from one unit to another
    '''
    
    # Convert MM, CM, DM to M
    m = 1
    dm = 1/10
    cm = 1/100
    mm = 1/1000

    # Check condition for unit
    if l == "m":
        x = x * m
        y = y * m
        z = z * m
    elif l == "dm":
        x = x * dm
        y = y * dm
        z = z * dm
    elif l == "cm":
        x = x * cm
        y = y * cm
        z = z * cm
    elif l == "mm":
        x = x * mm
        y = y * mm
        z = z * mm
    
    cbm = (x * y * z)
    cbm_unit_price = cbm * u
    
    return cbm_unit_price



def calculate_kg_shipping_unit_price(w, u):
    kg = w
    kg_unit_price = kg * u
    return kg_unit_price