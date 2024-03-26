Puls.SetValues(
0,
700,
0,
100
)
basic.forever(function () {
    Puls.Puls_highlow()
    Puls.Hjärtslag()
})
