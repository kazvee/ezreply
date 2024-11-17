import textwrap

replies = {
    "Add User to Account": """\
        Thank you for your message. To add additional users to your account, please follow the steps below:
        
        Login > Account Settings > Sharing > Add Users > Add the email addresses of the users you would like to add.

        I hope this resolves your query but please do not hesitate to reach out to us if you need any further assistance.

        You can email us at support@techsupport.net or phone us at 1-800-555-1337.
    """,
    "Billing Details": """\
        Thank you for your message. To change the credit card details held on file for you, please follow the steps below:

        Login > Account Settings > Billing > Change Credit Card Details

        I hope this resolves your query but please do not hesitate to reach out to us if you need any further assistance.

        You can email us at support@techsupport.net or phone us at 1-800-555-1337.
    """,
    "Password Reset": """\
        Thank you for your message. To reset your password, please follow the steps below:

        1. Visit the login page and click on 'Forgot Password'.
        2. Enter your registered email address and submit the form.
        3. Check your email inbox for a password reset link and follow the instructions provided.

        If you do not receive the email, please check your spam folder.

        I hope this resolves your query but please do not hesitate to reach out to us if you need any further assistance.

        You can email us at support@techsupport.net or phone us at 1-800-555-1337.
    """,
    "Cancel Subscription": """\
        We're sorry to see you go. To cancel your subscription, please follow the steps below:

        1. Visit the Account Cancellation page at https://techsupport.net/cancel/
        2. Enter your account details and click 'Cancel Subscription'.
        3. Follow the instructions provided to complete the cancellation process.

        Your subscription will remain active until the end of the billing period. If you have any questions or concerns, please reach out to us at support@techsupport.net or phone us at 1-800-555-1337.
    """,
    "Update Contact Information": """\
        To update your contact information, please follow the steps below:

        Login > Account Settings > Personal Information > Edit Contact Info

        Once updated, your changes will take effect immediately. 
       
        I hope this resolves your query but please do not hesitate to reach out to us if you need any further assistance.

        You can email us at support@techsupport.net or phone us at 1-800-555-1337.
    """
}

replies = {key: textwrap.dedent(value) for key, value in replies.items()}