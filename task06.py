emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]


def get_gmails_01(emails: list[str]):
    result01 = []
    for email in emails:
        if email.endswith("gmail.com"):
            result01.append(email)

    return result01


def get_gmails_02(emails: list[str]):
    result02 = [email for email in emails if email.endswith("gmail.com")]
    return result02


result01 = get_gmails_01(emails)
result02 = get_gmails_02(emails)
result03 = filter(lambda email: email.endswith("gmail.com"), emails)

print(result01)
print(result02)
print(list(result03))
