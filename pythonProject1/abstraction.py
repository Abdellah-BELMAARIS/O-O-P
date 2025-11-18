class EmailService:
    def __init__(self, server="smtp.example.com", port=587):
        self.server = server
        self.port = port
        self.is_connected = False
        self.is_authenticated = False

    def send_email(self, recipient, subject, message):
        try:
            self._connect()
            self._authenticate()
            print(f"Sending email to {recipient}")
            print(f"Subject: {subject}")
            print(f"Message: {message}")
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
        finally:
            self._disconnect()

    def _connect(self):
        if not self.is_connected:
            print(f"Connecting to {self.server}:{self.port}...")
            self.is_connected = True
        else:
            print("Already connected to email server")

    def _authenticate(self):
        if self.is_connected and not self.is_authenticated:
            print("Authenticating...")
            self.is_authenticated = True
        elif not self.is_connected:
            raise ConnectionError("Must connect before authenticating")
        else:
            print("Already authenticated")

    def _disconnect(self):
        if self.is_connected:
            print("Disconnecting from email server...")
            self.is_connected = False
            self.is_authenticated = False
        else:
            print("Not connected to any server")


if __name__ == "__main__":
    email_service = EmailService(server="smtp.gmail.com", port=587)

    success = email_service.send_email(
        recipient="user@example.com",
        subject="Test Email",
        message="This is a test email message."
    )

    if success:
        print("Email sent successfully!")
    else:
        print("Failed to send email")