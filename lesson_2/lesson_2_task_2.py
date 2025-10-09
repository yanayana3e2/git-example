def is_year_leap(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False
if __name__ == "__main__":
  print(f"2004 год високосный? {is_year_leap(2004)}")
  print(f"1900 год високосный? {is_year_leap(1900)}")
  print(f"2024 год високосный? {is_year_leap(2024)}")
  print(f"2023 год високосный? {is_year_leap(2023)}")