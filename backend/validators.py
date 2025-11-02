def validate_transaction(data: dict):
    if not isinstance(data, dict):
        return "Invalid JSON body"

    title = data.get("title")
    category = data.get("category")
    type_ = data.get("type")
    amount = data.get("amount")
    date = data.get("date")

    if not title or not isinstance(title, str):
        return "Field 'title' is required"
    if not category or not isinstance(category, str):
        return "Field 'category' is required"
    if type_ not in ("income", "expense"):
        return "Field 'type' must be either 'income' or 'expense'"
    if not isinstance(amount, (int, float)) or amount <= 0:
        return "Field 'amount' must be a positive number"
    if not date or not isinstance(date, str):
        return "Field 'date' is required (format: YYYY-MM-DD)"
    
    return None