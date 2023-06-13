def get_date_info(year_month, quarter):
    year = int(year_month[:4])
    month = int(year_month[4:])

    # Calculate previous month
    previous_month = (year * 100 + month - 1) if month > 1 else ((year - 1) * 100 + 12)
    previous_month = str(previous_month).zfill(6)

    # Calculate previous quarter
    previous_quarter = quarter - 1 if quarter > 1 else 4
    previous_quarter = f"Q{previous_quarter}"

    # Calculate future year and month
    future_year = year
    future_month = month + 11
    if future_month > 12:
        future_month -= 12
        future_year += 1
    future_year_month = str(future_year).zfill(4) + str(future_month).zfill(2)

    # Calculate quarter of the parameter
    parameter_quarter = f"Q{quarter}_{year}"

    return previous_month, previous_quarter, future_year_month, parameter_quarter


# Example usage
year_month = "202306"
quarter = 2

previous_month, previous_quarter, future_year_month, parameter_quarter = get_date_info(year_month, quarter)

print("Previous Month:", previous_month)
print("Previous Quarter:", previous_quarter)
print("Future Year and Month:", future_year_month)
print("Quarter of Parameter:", parameter_quarter)