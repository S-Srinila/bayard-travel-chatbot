from data import travel_packages

# -------- Destination detection --------
def extract_destination(text: str):
    text = text.lower()
    for destination in travel_packages.keys():
        if destination.lower() in text:
            return destination
    return None


# -------- Chatbot response --------
def chatbot_response(user_input: str) -> str:
    user_input = user_input.lower()
    destination = extract_destination(user_input)

    # Package-related queries
    if destination and any(
        keyword in user_input
        for keyword in ["package", "price", "details", "trip", "cost"]
    ):
        package = travel_packages[destination]

        response = (
            f"📦 {package['name']}\n\n"
            f"💰 Price: {package['price']}\n"
            f"🗓 Duration: {package['duration']}\n\n"
            "✅ Includes:\n"
        )

        for item in package["includes"]:
            response += f"- {item}\n"

        response += "\n📝 Booking Process:\n"

        for step in package["booking_process"]:
            response += f"→ {step}\n"

        return response

    # General booking intent
    if "book" in user_input or "booking" in user_input:
        return (
            "📄 Booking Process:\n"
            "1. Select your travel package\n"
            "2. Confirm travel dates\n"
            "3. Submit passport details\n"
            "4. Make payment\n"
            "5. Receive booking confirmation"
        )

    # Fallback
    return (
        "I can help you with travel packages, destinations, pricing, "
        "or the booking process. Try asking:\n"
        "👉 'Dubai package details'\n"
        "👉 'Bali trip price'"
    )
