#Define checkout function

def checkout(items):
  """
  Calculates the total cost of a list of scanned items, considering offers.
  Args:
      items: A list of strings representing the scanned items (e.g., ["Apple", "Orange"]).
  Returns:
      The total cost as a formatted string (e.g., "£2.05").
  """

  # Define prices and offer thresholds

  apple_price = 0.60
  orange_price = 0.25
  apple_offer_threshold = 2
  orange_offer_threshold = 3

  # Initialize total cost

  total_cost = 0

  # Count occurrences of each item

  item_counts = {"Apple": 0, "Orange": 0}
  for item in items:
    item_counts[item] += 1

  # Apply offers for each item
  # Apples: Buy one, get one free

  apple_discount = item_counts["Apple"] // apple_offer_threshold * apple_price
  total_cost += item_counts["Apple"] * apple_price - apple_discount
  # Oranges: 3 for the price of 2
  orange_discount = (item_counts["Orange"] // orange_offer_threshold) * orange_price
  total_cost += item_counts["Orange"] * orange_price - orange_discount

  # Format and return the total cost

  return f"£{total_cost:.2f}"

# Example usage

items = ["Apple", "Apple", "Orange", "Apple", "Orange", "Orange", "Orange"]
total_cost = checkout(items)

print(f"Total cost: {total_cost}")
