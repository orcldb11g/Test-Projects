def checkout(items):
  """
  Calculates the total cost of a list of scanned items.
  Args:
      items: A list of strings representing the scanned items (e.g., ["Apple", "Orange"]).
  Returns:
      The total cost as a formatted string (e.g., "£2.05").
  """
  # Define prices

  apple_price = 0.60
  orange_price = 0.25
  
  # Initialize total cost
  
  total_cost = 0

  # Count occurrences of each item

  item_counts = {"Apple": 0, "Orange": 0}
  for item in items:
    item_counts[item] += 1

  # Calculate cost based on item counts

  total_cost += item_counts["Apple"] * apple_price
  total_cost += item_counts["Orange"] * orange_price

  # Format and return the total cost

  return f"£{total_cost:.2f}"

# Example usage

items = ["Apple", "Apple", "Orange", "Apple"]
total_cost = checkout(items)

print(f"Total cost: {total_cost}")
