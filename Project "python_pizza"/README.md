# Pizza Ordering System

This is a simple Python program for ordering pizza, drinks, and sweets from a pizzeria. Here's a breakdown of the program:

### Functions:
1. `choose_pizza()`: Asks the user to choose a type of pizza and returns the user's choice.
2. `choose_size()`: Asks the user to choose the size of the pizza and returns the user's choice.
3. `calculate_price()`: Calculates the price of the selected pizza and adds it to the cart.
4. `order_pizza()`: Allows the user to order multiple pizzas and calculates the total price of the order.
5. `order_drinks()`: Asks the user if they want to add drinks to their order and calculates the total price accordingly.
6. `order_sweets()`: Asks the user if they want to add sweets to their order and calculates the total price accordingly.
7. `payment()`: Provides options for payment and calculates the change if the user chooses to pay by cash.

### Main Program Flow:
1. The `order_pizza()` function is called to initiate the pizza ordering process by asking the user to choose the type and size of the pizza.
2. Once the pizza order is completed, the program proceeds to ask if the user wants to add drinks and/or sweets to their order.
3. After the additional items are added (if chosen), the user is prompted to select the payment method and, if applicable, enter the payment amount to calculate the change.

The program is designed to provide an interactive experience for ordering items from the pizzeria, allowing the user to customize their order and complete the payment process.

Please note that the program currently lacks the logic for choosing and calculating the price of drinks and sweets, which should be implemented according to the pizzeria's menu and pricing.
