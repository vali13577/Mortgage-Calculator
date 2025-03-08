def calculate_monthly_payment(principal, annual_interest_rate, years):
    """
    Calculate monthly mortgage payment.

    Args:
        principal (float): The loan amount
        annual_interest_rate (float): Annual interest rate (in percentage, e.g., 5 for 5%)
        years (int): Loan term in years

    Returns:
        float: Monthly payment amount
    """
    # Convert annual interest rate to monthly rate (decimal)
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Convert years to total number of monthly payments
    total_payments = years * 12

    # Formula for monthly payment:
    # M = P [ r(1 + r)^n ] / [ (1 + r)^n - 1 ]
    # Where M = monthly payment, P = principal, r = monthly interest rate, n = total payments
    if monthly_interest_rate == 0:  # Handle 0% interest case
        monthly_payment = principal / total_payments
    else:
        monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                          ((1 + monthly_interest_rate) ** total_payments - 1)

    return monthly_payment


def mortgage_calculator():
    print("=== Mortgage Calculator ===")

    # Get user input with basic error handling
    try:
        principal = float(input("Enter the loan amount (e.g., 200000): $"))
        annual_interest_rate = float(input("Enter the annual interest rate (e.g., 5 for 5%): "))
        years = int(input("Enter the loan term in years (e.g., 30): "))

        if principal <= 0 or annual_interest_rate < 0 or years <= 0:
            print("Please enter positive values for loan amount and years, and a non-negative interest rate.")
            return

        # Calculate monthly payment
        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)

        # Calculate total payment and total interest
        total_payment = monthly_payment * years * 12
        total_interest = total_payment - principal

        # Display results
        print("\n--- Results ---")
        print(f"Monthly Payment: ${monthly_payment:,.2f}")
        print(f"Total Payment: ${total_payment:,.2f}")
        print(f"Total Interest Paid: ${total_interest:,.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the calculator
if __name__ == "__main__":
    mortgage_calculator()
