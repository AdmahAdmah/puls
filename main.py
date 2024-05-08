Puls.set_values(0, 700, 0, 100)

def on_forever():
    Puls.Puls_highlow()
    Puls.hjärtslag()
basic.forever(on_forever)
