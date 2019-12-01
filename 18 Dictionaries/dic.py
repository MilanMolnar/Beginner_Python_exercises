month_conversion = {
    "Jan": "January",
    "Feb":  "February",
    "Mar": "March",
}

print(month_conversion["Mar"])

print(month_conversion.get("Jan"))

print(month_conversion.get("Fak", "Nem honap"))