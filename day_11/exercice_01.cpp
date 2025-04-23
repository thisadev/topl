#include <iostream>

// To test, define DEBUG (or pass -DDEBUG to compiler)
//#define DEBUG

int main() {
    std::cout << "Program started." << std::endl;

    #ifdef DEBUG
        // This code only exists in the compiled program if DEBUG is defined
        std::cout << "[Debug] Performing extra validation..." << std::endl;
    #endif

    // This code is always included
    std::cout << "Performing main task." << std::endl;

    #ifndef DEBUG
        // This code only exists if DEBUG is NOT defined (e.g., Release build)
        std::cout << "[Release] Running optimised." << std::endl;
    #endif

    return 0;
}
