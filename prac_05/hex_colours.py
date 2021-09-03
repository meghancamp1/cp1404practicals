COLOUR_NAME_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
                       "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "BlanchedAlmond": "#ffebcd",
                       "blue1": "#0000ff", "BlueViolet": "#8a2be2"}
name = input("Colour name: ")
while name != "":
    if name in COLOUR_NAME_TO_CODE:
        print(COLOUR_NAME_TO_CODE[name])
    else:
        print("Invalid colour name")
    name = input("Colour name: ")
