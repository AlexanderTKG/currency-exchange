class Currency:
    exchange_rates = {
        "$": 1.0,
        "€": 1.20,
        "£": 1.40,
        "¥": 0.0093,
        "₹": 0.013,
        "₩": 0.00087
    }

    labels = {
        "$": "US Dollar",
        "€": "Euro",
        "£": "British Pound",
        "¥": "Japanese Yen",
        "₹": "Indian Rupee",
        "₩": "South Korean Won"
    }

    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

    def __str__(self):
        return f"{self.symbol}{self.amount}"

    def to_usd(self):
        return self.amount / Currency.exchange_rates[self.symbol]

currencies = [
    Currency("$", 123.45),
    Currency("€", 98.76),
    Currency("£", 567.89),
    Currency("¥", 12000),
    Currency("₹", 98000),
    Currency("₩", 10000000)
]

for currency in currencies:
    label = Currency.labels[currency.symbol]
    usd_amount = currency.to_usd()
    print(f"{label}: {currency} ({usd_amount:.2f} USD)")
