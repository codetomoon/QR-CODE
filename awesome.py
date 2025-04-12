
import time
import random

def countdown(seconds):
    """Displays a countdown timer."""
    for i in range(seconds, 0, -1):
        print(f"Get ready... {i}")
        time.sleep(1)
    print("GO!\n")

def display_random_gesture():
    """Randomly selects a gesture for the user to respond to."""
    gestures = ["Wave", "Fist", "Point", "Palm"]
    return random.choice(gestures)

def main():
    print("Welcome to the Reflex Trainer!")
    print("Respond to the gestures as fast as you can!")
    print("Type the gesture name when it appears on the screen.")
    print("Gestures: Wave, Fist, Point, Palm\n")
    input("Press Enter to start...")
    
    score = 0
    start_time = time.time()

    try:
        while True:
            # Countdown before showing the gesture
            countdown(3)
            
            # Randomly choose a gesture
            gesture = display_random_gesture()
            print(f"Gesture: {gesture}")
            
            # Measure the time it takes for the user to respond
            user_input = input("Your Response: ").strip()
            reaction_time = time.time() - start_time
            
            # Check if the user responded correctly
            if user_input.lower() == gesture.lower():
                print(f"Correct! Reaction Time: {reaction_time:.2f} seconds\n")
                score += 1
            else:
                print(f"Wrong! The correct gesture was '{gesture}'.\n")
            
            start_time = time.time()
    except KeyboardInterrupt:
        # Exit gracefully when the user interrupts
        print("\nGame Over!")
        print(f"Your final score: {score}")
        print("Thanks for playing. Goodbye!")

if __name__ == "__main__":
    main()

       