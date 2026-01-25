import pywhatkit as kit
import datetime
import time

# ===== BASIC FUNCTIONS =====

def send_instant_message(phone_number, message):
    """
    Send an instant WhatsApp message
    Args:
        phone_number: Phone number with country code (e.g., '+919876543210')
        message: Message text to send
    """
    try:
        # Get current time and add 1 minute for scheduling
        now = datetime.datetime.now()
        future_time = now + datetime.timedelta(minutes=1)
        hour = future_time.hour
        minute = future_time.minute
        
        print(f"Scheduling message for {hour}:{minute:02d} (in 1 minute)")
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")

def send_bulk_messages(contacts, message):
    """
    Send same message to multiple contacts
    Args:
        contacts: List of phone numbers with country code
        message: Message to send to all contacts
    """
    for phone in contacts:
        try:
            now = datetime.datetime.now()
            future_time = now + datetime.timedelta(minutes=1)
            hour = future_time.hour
            minute = future_time.minute
            
            print(f"Sending message to {phone} at {hour}:{minute:02d} (in 1 minute)")
            kit.sendwhatmsg(phone, message, hour, minute)
            time.sleep(15)  # Wait 15 seconds between messages
        except Exception as e:
            print(f"Error sending to {phone}: {e}")

def send_image(phone_number, image_path, caption=""):
    """
    Send an image via WhatsApp
    Args:
        phone_number: Phone number with country code
        image_path: Path to image file
        caption: Optional caption for the image
    """
    try:
        kit.sendwhats_image(phone_number, image_path, caption)
        print("Image sent successfully!")
    except Exception as e:
        print(f"Error sending image: {e}")

def send_to_group(group_id, message):
    """
    Send message to a WhatsApp group
    Args:
        group_id: Group ID (you'll need to find this)
        message: Message to send
    """
    try:
        now = datetime.datetime.now()
        future_time = now + datetime.timedelta(minutes=1)
        hour = future_time.hour
        minute = future_time.minute
        
        print(f"Scheduling group message for {hour}:{minute:02d} (in 1 minute)")
        kit.sendwhatmsg_to_group(group_id, message, hour, minute)
        print("Group message sent successfully!")
    except Exception as e:
        print(f"Error sending to group: {e}")

# ===== INTERACTIVE MENU =====

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("WhatsApp Automation Menu")
    print("="*50)
    print("1. Send message to single contact")
    print("2. Send bulk messages to multiple contacts")
    print("3. Send image to contact")
    print("4. Send message to group")
    print("5. Exit")
    print("="*50)

def get_phone_number():
    """Get phone number with validation"""
    while True:
        phone = input("Enter phone number with country code (e.g., +919876543210): ").strip()
        if phone.startswith('+') and len(phone) >= 10:
            return phone
        else:
            print("Invalid format! Please include country code (e.g., +91 for India)")

def main():
    """Main interactive function"""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            # Send single message
            print("\n--- Send Single Message ---")
            phone = get_phone_number()
            message = input("Enter your message: ")
            send_instant_message(phone, message)
            
        elif choice == '2':
            # Send bulk messages
            print("\n--- Send Bulk Messages ---")
            num_contacts = int(input("How many contacts? "))
            contacts = []
            for i in range(num_contacts):
                print(f"\nContact {i+1}:")
                phone = get_phone_number()
                contacts.append(phone)
            message = input("\nEnter message to send to all: ")
            send_bulk_messages(contacts, message)
            
        elif choice == '3':
            # Send image
            print("\n--- Send Image ---")
            phone = get_phone_number()
            image_path = input("Enter image path: ")
            caption = input("Enter caption (or press Enter to skip): ")
            send_image(phone, image_path, caption)
            
        elif choice == '4':
            # Send to group
            print("\n--- Send to Group ---")
            group_id = input("Enter group ID: ")
            message = input("Enter your message: ")
            send_to_group(group_id, message)
            
        elif choice == '5':
            print("\nThank you for using WhatsApp Automation!")
            break
            
        else:
            print("\nInvalid choice! Please enter 1-5.")
        
        # Ask if user wants to continue
        if choice in ['1', '2', '3', '4']:
            continue_choice = input("\nDo you want to perform another action? (yes/no): ").lower()
            if continue_choice not in ['yes', 'y']:
                print("\nThank you for using WhatsApp Automation!")
                break

# ===== USAGE =====

if __name__ == "__main__":
    print("Welcome to WhatsApp Automation!")
    print("Make sure WhatsApp Web is logged in on your browser.")
    input("Press Enter to continue...")
    main()

