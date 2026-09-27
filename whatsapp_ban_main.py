import requests
import json

def ban_whatsapp(target_phone_number):
    # WhatsApp API endpoint for reporting spam
    url = "https://graph.facebook.com/v13.0/1234567890/messages"

    # Replace with your own WhatsApp Business API access token
    access_token = "YOUR_ACCESS_TOKEN_HERE"

    # Spam report payload
    data = {
        "messaging_product": "whatsapp",
        "to": target_phone_number,
        "type": "text",
        "text": {
            "body": "/reportspam"
        }
    }

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 201:
        print(f"Ban request sent for {target_phone_number}")
    else:
        print(f"Failed to send ban request: {response.text}")

# Example usage
ban_whatsapp("+1234567890")


