import pyautogui
import time
import traceback

def show_menu():
    options = ["food", "wood", "steel", "oil"]
    print("Please choose a resource:")
    for idx, resource in enumerate(options, 1):
        print(f"{idx}. {resource.capitalize()}")

    while True:
        choice = input("Enter the number of your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            selected = options[int(choice) - 1]
            print(f"You selected: {selected.capitalize()}")

            # Step 1: Click region.png
            try:
                region = pyautogui.locateOnScreen("region.png", confidence=0.8)
                if region:
                    center = pyautogui.center(region)
                    pyautogui.moveTo(center.x, center.y, duration=1)
                    pyautogui.click()
                else:
                    print("region.png not found.")
            except Exception as e:
                print(f"Error locating region.png: {e}")
                traceback.print_exc()
            time.sleep(1)

            # Step 2: Click search.png
            try:
                search = pyautogui.locateOnScreen("search.png", confidence=0.5)
                if search:
                    center = pyautogui.center(search)
                    pyautogui.moveTo(center.x, center.y, duration=1)
                    pyautogui.click()
                else:
                    print("search.png not found.")
            except Exception as e:
                print(f"Error locating search.png: {e}")
                traceback.print_exc()
            time.sleep(1)

            # Step 3: Click the chosen resource image
            try:
                resource_img = f"{selected}.png"
                resource = pyautogui.locateOnScreen(resource_img, confidence=0.5)
                if resource:
                    center = pyautogui.center(resource)
                    pyautogui.moveTo(center.x, center.y, duration=1)
                    pyautogui.click()
                else:
                    print(f"{resource_img} not found.")
            except Exception as e:
                print(f"Error locating {resource_img}: {e}")
                traceback.print_exc()
            time.sleep(1)

            # Step 4: Click search_big.png
            try:
                search_big = pyautogui.locateOnScreen("search_big.png", confidence=0.5)
                if search_big:
                    center = pyautogui.center(search_big)
                    pyautogui.moveTo(center.x, center.y, duration=1)
                    pyautogui.click()
                else:
                    print("search_big.png not found.")
            except Exception as e:
                print(f"Error locating search_big.png: {e}")
                traceback.print_exc()
            time.sleep(5)

            # Step 5: After locating the post-resource image, move to window center, wait, then click
            try:
                post_img = f"{selected}1.png"
                post_search = pyautogui.locateOnScreen(post_img, confidence=0.5)
                if post_search:
                    win = pyautogui.getActiveWindow()
                    if win is not None:
                        center_x = win.left + win.width // 2
                        center_y = win.top + win.height // 2
                        print(f"Moving to center of window at ({center_x}, {center_y})")
                        pyautogui.moveTo(center_x, center_y, duration=1)
                        time.sleep(2)
                        pyautogui.click()
                        print("Clicked in the center of the application window.")
                    else:
                        print("No active window found.")
                else:
                    print(f"{post_img} not found.")
            except Exception as e:
                print(f"Error locating {post_img}: {e}")
                traceback.print_exc()
            time.sleep(1)

            return selected
        else:
            print("Invalid choice. Please try again.")
# ----------- MAIN EXECUTION FLOW -----------
try:
    print("Checking if squad is free...")
    try:
        check = pyautogui.locateOnScreen("check.png", confidence=0.9)
    except Exception:
        check = None

    if check:
        print("Squad is not free. Exiting.")
    else:
        print("Squad is free. Proceeding to menu...")
        show_menu()

except Exception as e:
    print(f"Error during initial check: {e}")
    traceback.print_exc()