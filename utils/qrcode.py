import segno

dynamo_blue = (3, 122, 204)
dynamo_purple = (95, 85, 200)
epfl_red = (255, 0, 0)

segno.make_qr("https://github.com/EPFL-LAP/dynamatic").save(
    "dynamatic-qr.png",
    scale=5,
    dark=epfl_red,
)

segno.make_qr("https://dynamo.ethz.ch/").save(
    "dynamo-qr.png",
    scale=5,
    dark=dynamo_purple,
)
