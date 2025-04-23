global_event_counter = 0

def process_event(event_id, event_data):
    global global_event_counter

    print(f"\n--- Processing Event ID: {event_id} ---")

    global_event_counter += 1

    print(f"Received data type: {type(event_data)}")
    print(f"Received data value: '{event_data}'")

    status_message = "Processing"
    print(f"Initial function scope: status_message = '{status_message}'")

    if isinstance(event_data, int) and event_data == 0:
        status_message = "Zero event!"
        print(f"Inside if (event == 0): status_message = '{status_message}'")

    print(f"Outside if block: status_message = '{status_message}'")

    print(f"Attempting to rebind 'event_data' parameter...")
    try:
        event_data = "Processed"
        print(f"Reassigned 'event_data' to: '{event_data}'")
        print(f"Type of 'event_data' after reassignment: {type(event_data)}")
    except Exception as e:
        print(f"An unexpected error occurred during reassignment: {e}")

    print(f"--- Finished Event ID: {event_id} ---")
    return True

print("Starting event processing...")
global_event_counter = 0

process_event(1, 100)
process_event(2, 0)
process_event(3, "Error signal")

print("\n=============================")
print(f"Total events processed: {global_event_counter}")
print("=============================")
