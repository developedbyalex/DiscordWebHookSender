# Discord Webhook Embed Sender

This Python script allows you to send a Discord webhook message with an embed. The script prompts you for the embed color, title, contents, and whether to include the date.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage

1. Clone the repository or download the script.

2. Run the script:

```bash
python sender.py
```

3. Follow the prompts to input the webhook URL, embed color, title, contents, and whether to include the date.

## Example

```plaintext
Enter the Discord webhook URL: https://discord.com/api/webhooks/your_webhook_url
Embed Color (Expects Hex Code, e.g., #FF5733): #FF5733
Embed Title: Test Embed
Embed Contents: This is a test message
Include Date (Y/N): Y
```

## Notes

- Ensure you have the correct permissions to send messages to the webhook URL you provide.
- The embed color should be a valid hex code (e.g., `#FF5733`).
- The date included in the embed is in UTC format.

## License

This project is licensed under the MIT License.
