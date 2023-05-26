import re


def is_valid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.fullmatch(regex, email)

def slice_email(email):
    """Return a tuple of username and email provider"""
    if not is_valid(email):
        print("Please enter a valid email address!")
        exit(1)
    idx = email.index("@")
    return (email[:idx], email[idx+1:])


def main():
    email_eg = "myemail@gmail.com"
    email_slc = slice_email(email_eg)
    print(email_slc)


if __name__ == "__main__":
    main()
