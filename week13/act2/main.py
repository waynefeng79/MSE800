import os
from google import genai
from google.genai import types

def generate_auckland_itinerary():
    # Initialize the client. It automatically picks up the GEMINI_API_KEY environment variable.
    client = genai.Client()

    # Extracting and structuring the prompt variables from your image criteria
    instructions = (
        "Generate a detailed 3-day travel itinerary for a trip to Auckland, New Zealand. "
        "The itinerary should include visits to landmarks, museums, and popular local restaurants. "
        "Ensure there is a balance between guided tours and free time for exploration. "
        "Each day should have suggestions for breakfast, lunch, and dinner, with brief "
        "descriptions of each activity and restaurant."
    )
    
    context = (
        "The traveller has never been to Auckland before and wants to experience both the "
        "well-known and hidden gems of the city. They are particularly interested in the "
        "history of Auckland. They are comfortable using public transport and enjoy walking tours."
    )
    
    input_data = (
        "3-day trip to Auckland. Focus heavily on rich historical landmarks, utilizing AT public transit "
        "(buses, trains, ferries), and exploring historic inner suburbs like Devonport and Parnell."
    )
    
    output_indicator = (
        "Travel itinerary formatting with specific timestamps (e.g., 9:00 AM), clear locations, "
        "vivid descriptions, and specific dining recommendations for each slot."
    )

    # Combine into a highly structured prompt configuration
    full_prompt = f"""
    === INSTRUCTIONS ===
    {instructions}

    === CONTEXT ===
    {context}

    === INPUT DATA ===
    {input_data}

    === OUTPUT INDICATOR ===
    {output_indicator}
    """

    print("Sending prompt to Gemini...")

    # Execute using the recommended, stateful interactions API and the fast, capable flash model
    # Change this block in your code:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=full_prompt,
        system_instruction="You are an expert New Zealand travel concierge specializing in historical and local itineraries."
    )

    # Output the result
    print("\n=== GENERATED ITINERARY ===\n")
    print(interaction.output_text)

if __name__ == "__main__":
    # Quick sanity check for the API key environment variable
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it in your terminal: export GEMINI_API_KEY='your_key'")
    else:
        generate_auckland_itinerary()
