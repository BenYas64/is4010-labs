def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid."""
    total_age = 0
    valid_ages = 0

    for user in users:
        if isinstance(user.get("age"), (int, float)) and user["age"] >= 0:
            total_age += user["age"]
            valid_ages += 1

    return total_age / valid_ages if valid_ages > 0 else 0.0


def get_active_user_emails(users):
    """Return email addresses belonging to active users."""
    active_emails = []
    for user in users:
        if user.get("is_active") and "email" in user:
            active_emails.append(user["email"])
    return active_emails