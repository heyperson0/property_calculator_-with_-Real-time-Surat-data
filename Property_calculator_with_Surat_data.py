#  Property Investment Calculator
#^ made by: Madni khan
#^ email madnikhan.work@gmail.com
#^ whatapp +91 90997 16001

# --- Limitation Agreement ---
def show_limitations():
    print("\n Property Investment Calculator Limitation Agreement ⚠️")
    print("""
Before using this tool, you must understand and accept the following:
1. This calculator provides insights, not confirmation for buying property.
2. It gives a vision of possible outcomes, not a guarantee.
3. Always consider:
   - Location and local real estate conditions
   - Politics and government policies affecting property
   - Economic trends (national and local)
   - Real estate market trends
   - Overall economy and macroeconomic conditions
4. This tool should not be the sole basis for your investment decision.
""")
    user_input = input("Type 'agree' to accept and continue: ").strip().lower()
    if user_input != "agree":
        print("You did not agree to the terms. Exiting the calculator.")
        exit()
    else:
        print("✅ Agreement accepted. You may proceed.\n")
show_limitations()
# --- Utility Functions ---
def get_float(prompt):
    """Safely gets float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# --- Calculation Functions ---
def calculate_cashflow(rent, emi):
    return rent - emi

def calculate_annual_cashflow(cashflow):
    return cashflow * 12

def calculate_roi(annual_cashflow, cash_invested):
    return (annual_cashflow / cash_invested * 100) if cash_invested > 0 else 0

def calculate_rental_yield(rent, price):
    return (rent * 12 / price * 100) if price > 0 else 0


def calculate_ltv(loan_amount, price):
    return (loan_amount / price * 100) if price > 0 else 0

def calculate_future_value(price, appreciation, years=5):
    return price * ((1 + appreciation) ** years)

def calculate_future_rent(rent, rent_growth, years=5):
    return rent * ((1 + rent_growth) ** years)

def calculate_taxable_income(annual_cashflow, maintenance, vacancy_loss, tax_rate):
    taxable = annual_cashflow - maintenance - vacancy_loss
    return max(taxable * tax_rate, 0)


# --- Decision Messages ---
def investment_decision(real_roi, cashflow):
    print("\n--- Investment Insights ---")
    
    # ROI message
    if real_roi < 0:
        print("❌ Avoid: This investment loses money after costs.")
    elif real_roi < 3:
        print("⚠️ Weak: Returns too low, consider better deals.")
    elif real_roi < 8:
        print("🟡 Moderate: Decent but not great.")
    else:
        print("✅ Strong investment: ROI above 8%.")

    # Cashflow message
    if cashflow <= 0:
        print("🔴 Negative cash flow. You’re losing money monthly.")
    elif cashflow <= 1000:
        print("🟠 Very low cash flow — risky if vacancy occurs.")
    elif cashflow <= 5000:
        print("🟡 Moderate cash flow.")
    else:
        print("🟢 Strong monthly cash flow.")


# --- Main Program ---
def main():
    print("\n --- Property Investment Calculator ---")

    # Inputs
    price = get_float("Enter property price (₹): ")
    loan_amount = get_float("Enter loan amount (₹): ")
    rent = get_float("Enter monthly rent (₹): ")
    emi = get_float("Enter monthly EMI (₹): ")
    cash_invested = get_float("Enter your total cash invested (₹): ")
    appreciation = get_float("Expected annual appreciation (e.g., 0.05 for 5%): ")
    rent_growth = get_float("Expected annual rent growth (e.g., 0.03 for 3%): ")
    vacancy_rate = get_float("Expected vacancy rate (e.g., 0.08 for 8%): ")
    maintenance_annual = get_float("Annual maintenance cost (₹): ")
    tax_rate = get_float("Tax rate on profit (e.g., 0.10 for 10%): ")
 
    # Calculations
    cashflow = calculate_cashflow(rent, emi)
    annual_cashflow = calculate_annual_cashflow(cashflow)
    roi = calculate_roi(annual_cashflow, cash_invested)
    rental_yield = calculate_rental_yield(rent, price)
    ltv = calculate_ltv(loan_amount, price)
    future_value = calculate_future_value(price, appreciation)
    future_rent = calculate_future_rent(rent, rent_growth)
    vacancy_loss = rent * 12 * vacancy_rate
    tax = calculate_taxable_income(annual_cashflow, maintenance_annual, vacancy_loss, tax_rate)
    net_annual_cashflow = annual_cashflow - maintenance_annual - vacancy_loss - tax
    real_roi = (net_annual_cashflow / cash_invested * 100) if cash_invested > 0 else 0
    rent_to_emi_coverage = (rent / emi * 100) if emi > 0 else 0

    # --- Output Summary ---
    print("\n--- Investment Summary ---")
    print(f"Monthly Cash Flow: ₹{cashflow:,.2f}")
    print(f"Annual Cash Flow (before tax): ₹{annual_cashflow:,.2f}")
    print(f"Net Annual Cash Flow (after tax): ₹{net_annual_cashflow:,.2f}")
    print(f"Real ROI after expenses: {real_roi:.2f}%")
    print(f"Rental Yield: {rental_yield:.2f}%")
    print(f"Rent covers {rent_to_emi_coverage:.1f}% of your EMI")
    print(f"Loan-to-Value Ratio (LTV): {ltv:.1f}%")
    print(f"Projected Property Value (5 yrs): ₹{future_value:,.0f}")
    print(f"Projected Monthly Rent (5 yrs): ₹{future_rent:,.0f}")

    # Decision Logic
    investment_decision(real_roi, cashflow)


# --- Run Program ---
if __name__ == "__main__":
    main()
