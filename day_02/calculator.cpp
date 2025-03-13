#include <iostream>
#include <vector>

class EvenSumCalculator {
public:
    
    int calculateEvenSum(int range) {
        int sum = 0;
        for (int i = 1; i <= range; ++i) {
            if (i % 2 == 0) {
                sum += i;
            }
        }
        return sum;
    }
};

int main() {
    EvenSumCalculator calculator;  
    int result = calculator.calculateEvenSum(10);
    std::cout << "Sum of even numbers from 1 to 10: " << result << std::endl;
    return 0;
}

