#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
  int rolls;

  std::cout << "Enter the number of dice rolls: ";
  std::cin >> rolls;

  std::srand(std::time(0)); // Seed for random number generation

  int sum = 0;

  std::cout << "Dice rolls: ";
  for (int i = 0; i < rolls; ++i) {
    int dice = (std::rand() % 6) + 1; // Random number between 1 and 6
    std::cout << dice << " ";
    sum += dice;
  }

  std::cout << "\nThe sum of the rolls is: " << sum << std::endl;

  return 0;
}