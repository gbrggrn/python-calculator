# Funktion som står för beräkningarna
def calculate(tal1, operator, tal2):
    if operator == "+":
        return tal1 + tal2
    elif operator == "-":
        return tal1 - tal2
    elif operator == "*":
        return tal1 * tal2
    elif operator == "/":
        return tal1 / tal2
    elif operator == "//":
        return tal1 // tal2
    elif operator == "%":
        return tal1 % tal2

# Validera att anv_input kan delas i tre
def try_split(input):
    try:
        tal1, operator, tal2 = input.split();
    except (ValueError, AttributeError): # Om jag förstått rätt så går det att göra såhär: "except (tuple av error-typer):"
        return "Felaktigt format"
    else:
        return [tal1, operator, tal2]

# Validera delarna
def try_validate_split(tal1, operator, tal2):
    try:
        tal1_float = float(tal1)
        tal2_float = float(tal2)
    except (ValueError, TypeError, OverflowError): # Overflow om talet är ohanterligt stort
        return "Något av talen var inte ett tal"
    if operator not in ["+", "-", "*", "/", "//", "%"]:
        return "Felaktig operator!"
    if operator in ["/", "//", "%"] and tal2_float == 0:
        return "Divison med 0 är inte möjligt"
    else:
        return [tal1_float, operator, tal2_float]

# main() styr flödeslogiken i programmet
def main():
    while True:
        anv_input = input("\nVad vill du räkna ut? (ex 5 / 3):") 

        # Validera split
        split_input = try_split(anv_input)

        if isinstance(split_input, str):
            print(try_split(anv_input))
        else: 
            input1, input2, input3 = split_input

            # Validera input
            isValid_split = try_validate_split(input1, input2, input3)

            if isinstance(isValid_split, str):
                print(isValid_split)
            else:
        
                tal1, operator, tal2 = isValid_split

                # Beräkna resultat
                result = calculate(tal1, operator, tal2)

                # Skriv ut - om resultattyp = int = inga decimaler
                if result.is_integer():
                    print(f"{tal1} {operator} {tal2} = {int(result)}")
                else:
                    print(f"{tal1} {operator} {tal2} = {result:.2f}")

# Anropa main()
main()