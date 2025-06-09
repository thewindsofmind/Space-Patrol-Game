import time
import random

def space_patrol_adventure():
    """
    A Space Patrol inspired choose-your-own-adventure game.
    """

    print("--- Space Patrol: The Asteroid Menace ---")
    print("You are Cadet Jax, a rookie Space Patrol officer.")
    print("Your mission: Investigate a distress signal from mining outpost Zeta-7.")
    print("Prepare for hyperspace jump...")
    time.sleep(2)

    # Initial choice
    print("\n1. Engage hyperspace jump.")
    print("2. Run a diagnostic check on the ship's systems.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nEngaging hyperspace...")
        time.sleep(3)
        print("Hyperspace jump successful. You arrive at Zeta-7.")

        # Asteroid field encounter
        print("\nZeta-7 is surrounded by a dense asteroid field.")
        print("1. Navigate through the asteroids carefully.")
        print("2. Attempt a risky shortcut through a narrow gap.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nCareful navigation pays off. You avoid major collisions.")
            time.sleep(2)
            print("You detect a faint energy signature from the outpost.")

            # Outpost investigation
            print("\n1. Approach the outpost cautiously.")
            print("2. Send a drone to investigate first.")
            choice = input("Enter your choice (1 or 2): ")

            if choice == "1":
                print("\nApproaching the outpost, you see signs of damage and strange, metallic footprints.")
                time.sleep(2)
                print("You encounter the 'Asteroid Men' - robotic creatures!")
                print("1. Attempt to communicate.")
                print("2. Open fire with your laser cannons.")
                choice = input("Enter your choice (1 or 2): ")

                if choice == "1":
                    print("\nYour communication attempt is met with hostility. They attack!")
                    if random.random() > 0.5:
                        print("You manage to repel the attack and find a survivor who explains that the Asteroid Men are automated mining drones that have gone rogue.")
                        print("1. Repair the drones.")
                        print("2. Destroy the drones.")
                        choice = input("Enter your choice (1 or 2): ")
                        if choice == "1":
                            print("You repaired the drones, saving the day!")
                            end_game_with_drones_and_platinum()
                        else:
                            print("You destroyed the drones, the planet is safe!")
                            end_game_with_platinum()
                    else:
                        print("You are overwhelmed and captured.")
                        print("Game Over.")
                else:
                    print("\nYour laser cannons are effective. You disable several Asteroid Men.")
                    if random.random() > 0.5:
                        print("You find a survivor who explains the situation")
                        print("1. Repair the drones.")
                        print("2. Destroy the drones.")
                        choice = input("Enter your choice (1 or 2): ")
                        if choice == "1":
                            print("You repaired the drones, saving the day!")
                            end_game_with_drones_and_platinum()
                        else:
                            print("You destroyed the drones, the planet is safe!")
                            end_game_with_platinum()
                    else:
                        print("Your ship is damaged, you must retreat!")
                        print("Game Over.")

            else:
                print("\nYour drone detects heavily armed robotic creatures - the Asteroid Men!")
                print("You prepare for battle.")
                if random.random() > 0.5:
                    print("You manage to repel the attack and find a survivor who explains that the Asteroid Men are automated mining drones that have gone rogue.")
                    print("1. Repair the drones.")
                    print("2. Destroy the drones.")
                    choice = input("Enter your choice (1 or 2): ")
                    if choice == "1":
                        print("You repaired the drones, saving the day!")
                        end_game_with_drones_and_platinum()
                    else:
                        print("You destroyed the drones, the planet is safe!")
                        end_game_with_platinum()
                else:
                    print("Your ship is damaged, you must retreat!")
                    print("Game Over.")

        else:
            print("\nThe shortcut is too risky! You collide with a large asteroid.")
            if random.random() > 0.5:
                print("Your ship's shields hold, but you are heavily damaged. You limp towards Zeta-7.")
                print("You still manage to save the day!")
                end_game_with_platinum()
            else:
                print("Your ship is destroyed.")
                print("Game Over.")

    else:
        print("\nPerforming system diagnostics...")
        time.sleep(2)
        print("You detect a critical malfunction in the hyperspace drive.")
        print("1. Attempt an emergency repair.")
        print("2. Abort the mission and return to base.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nAfter a tense repair, you manage to fix the drive.")
            time.sleep(2)
            print("You engage hyperspace jump and arrive at Zeta-7.")
            print("The adventure continues...")
            #Go to asteroid field encounter.
            print("\nZeta-7 is surrounded by a dense asteroid field.")
            print("1. Navigate through the asteroids carefully.")
            print("2. Attempt a risky shortcut through a narrow gap.")
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1":
                print("\nCareful navigation pays off. You avoid major collisions.")
                time.sleep(2)
                print("You detect a faint energy signature from the outpost.")
                print("\n1. Approach the outpost cautiously.")
                print("2. Send a drone to investigate first.")
                choice = input("Enter your choice (1 or 2): ")
                if choice == "1":
                    print("\nApproaching the outpost, you see signs of damage and strange, metallic footprints.")
                    time.sleep(2)
                    print("You encounter the 'Asteroid Men' - robotic creatures!")
                    print("1. Attempt to communicate.")
                    print("2. Open fire with your laser cannons.")
                    choice = input("Enter your choice (1 or 2): ")
                    #Add rest of game here.
                else:
                    #Add rest of game here
                    print("Drone sent")
            else:
                print("Crash")
        else:
            print("\nYou return to base. Mission failed.")
            print("Game Over.")

def end_game_with_drones_and_platinum():
    """Ends the game with the player returning home with the drones and platinum."""
    print("\nWith the Asteroid Men repaired, you salvage a significant amount of regolithic platinum.")
    print("1. Return home with the drones and all the platinum.")
    print("2. Return home with the drones and half the platinum.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nGreed overtakes you. The extra weight of the platinum makes your ship less maneuverable.")
        if random.random() > 0.5:
            print("You manage to navigate the asteroid field, but your ship sustains heavy damage.")
            print("You return home, but the ship needs extensive repairs.")
            print("Mission successful, but costly.")
        else:
            print("You are unable to navigate the asteroid field with the extra weight. Your ship is destroyed.")
            print("Game Over.")
    else:
        print("\nYou decide to be moderate, taking only half the platinum.")
        print("You safely navigate the asteroid field and return home with the drones and the platinum.")
        print("Mission successful!")

def end_game_with_platinum():
    """Ends the game with the player returning home with just the platinum."""
    print("\nYou salvage a significant amount of regolithic platinum.")
    print("1. Return home with all the platinum.")
    print("2. Return home with half the platinum.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nGreed overtakes you. The extra weight of the platinum makes your ship less maneuverable.")
        if random.random() > 0.5:
            print("You manage to navigate the asteroid field, but your ship sustains heavy damage.")
            print("You return home, but the ship needs extensive repairs.")
            print("Mission successful, but costly.")
        else:
            print("You are unable to navigate the asteroid field with the extra weight. Your ship is destroyed.")
            print("Game Over.")
    else:
        print("\nYou decide to be moderate, taking only half the platinum.")
        print("You safely navigate the asteroid field and return home with the platinum.")
        print("Mission successful!")

if __name__ == "__main__":
    space_patrol_adventure()
  
