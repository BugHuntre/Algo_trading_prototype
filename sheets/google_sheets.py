import gspread

def log_to_google_sheets(trades):
    client = gspread.service_account("sheets/credential.json")  # Automatically handles scopes
    sheet = client.open("Algo_Trade_Log").worksheet("Trade_Log")

    for trade in trades:
        row = [str(item) if not isinstance(item, (int, float)) else item for item in trade]
        sheet.append_row(row)
