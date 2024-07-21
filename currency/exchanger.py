def exchanger(amount: float, currency: str) -> float:
    amount = amount
    match currency:
        case "USD":
            amount = amount
        case "ILS":
            amount = amount * 3.65
        case "EUR":
            amount = amount * 0.91


    return amount

if __name__ == "__main__":
    pass