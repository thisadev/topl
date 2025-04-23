import sys

class RobotActions:
    def wave(self):
        print("Robot waves hello! 👋")

    def spin(self):
        print("Robot spins around! 💫")

    def report_status(self):
        print("Robot status: All systems nominal. ✅")

if __name__ == "__main__":
    print(f"Running Python {sys.version.split()[0]}")
    robot = RobotActions()

    # Get command dynamically from user input
    command = input("Enter robot command (e.g., wave, spin, report_status): ")

    print(f"\nReceived command: '{command}'")

    # Runtime Metaprogramming: Use the input string to find and call the method
    if hasattr(robot, command):
        method_to_call = getattr(robot, command)

        if callable(method_to_call):
            print("Executing command...")
            method_to_call() # Dynamic method invocation
        else:
            print(f"Error: '{command}' is an attribute but not a callable method.")
    else:
        print(f"Error: Unknown command '{command}'. Robot cannot perform this action.")

    print("\n--- End of demo ---")
