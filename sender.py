import requests
import datetime

def send_discord_webhook(webhook_url, embed):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'embeds': [embed]
    }
    response = requests.post(webhook_url, json=payload, headers=headers)
    if response.status_code == 204:
        print("Webhook sent successfully!")
    else:
        print(f"Failed to send webhook: {response.status_code}")
        print(response.text)

def main():
    webhook_url = input("Enter the Discord webhook URL: ")

    embed_color = input("Embed Color (Expects Hex Code, e.g., #FF5733): ")
    embed_title = input("Embed Title: ")
    embed_contents = input("Embed Contents: ")
    include_date = input("Include Date (Y/N): ").strip().lower() == 'y'

    embed = {
        "title": embed_title,
        "description": embed_contents,
        "color": int(embed_color.lstrip('#'), 16)
    }

    if include_date:
        embed["timestamp"] = datetime.datetime.utcnow().isoformat()

    send_discord_webhook(webhook_url, embed)

if __name__ == "__main__":
    main()
