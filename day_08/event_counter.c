#include <stdio.h>
#include <stdbool.h>

int global_event_counter = 0;


typedef enum {
    TYPE_INT,
    TYPE_STRING
} DataType;

bool process_event(int event_id, void* event_data, DataType data_type);

int main() {
    printf("Starting event processing...\n");
    global_event_counter = 0;
    
    int data1 = 100;
    int data2 = 0;
    char* data3 = "Error signal";

    process_event(1, &data1, TYPE_INT);
    process_event(2, &data2, TYPE_INT);
    process_event(3, data3, TYPE_STRING);

    printf("\n=============================\n");
    printf("Total events processed: %d\n", global_event_counter);
    printf("=============================\n");
    return 0;
}

bool process_event(int event_id, void* event_data, DataType data_type) {
    printf("\n--- Processing Event ID: %d ---\n", event_id);
    global_event_counter++;

    printf("Received data type: ");
    if (data_type == TYPE_INT) {
        printf("Integer\n");
        printf("Received data value: '%d'\n", *(int*)event_data);
    } else if (data_type == TYPE_STRING) {
        printf("String\n");
        printf("Received data value: '%s'\n", (char*)event_data);
    } else {
        printf("Unknown\n");
        printf("Received data value: 'N/A'\n");
    }

    char* status_message = "Processing";
    printf("Initial function scope: status_message = '%s'\n", status_message);

    if (data_type == TYPE_INT && *(int*)event_data == 0) {
        char* status_message = "Zero event!";
        printf("Inside if (event == 0): status_message = '%s'\n", status_message);
    }

    printf("Outside if block: status_message = '%s'\n", status_message);

    printf("Attempting to rebind 'event_data' parameter conceptually...\n");
    
    char* status_message = "Processed";
    void* original_pointer = event_data; // Keep original for clarity if needed later

    // Reassign the void pointer itself to point to the string literal
    event_data = status_message;

    printf("Reassigned 'event_data' pointer to point to: '%s'\n", (char*)event_data);
    printf("Type after reassignment (conceptual): String (pointer now points to string literal)\n");
    // Note: The memory location originally pointed to by original_pointer remains unchanged.

    printf("--- Finished Event ID: %d ---\n", event_id);
    return true;
}
