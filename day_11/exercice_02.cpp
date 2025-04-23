#include <iostream>
#include <string>

// Write the function ONCE using placeholder type 'T'
template <typename T>
T get_larger(T a, T b) {
    // Assumes type T supports the '>' operator
    return (a > b) ? a : b;
}

int main() {
    // Use the SAME function logic for different types:
    std::cout << "Larger int: " << get_larger(5, 10) << std::endl;
    std::cout << "Larger double: " << get_larger(12.5, 12.1) << std::endl;
    std::cout << "Larger string: " << get_larger(std::string("apple"), std::string("banana")) << std::endl;

    // It's type-safe - the compiler checks each usage:
    // std::cout << get_larger(10, "hello"); // COMPILE ERROR! Types don't match.

    return 0;
}
