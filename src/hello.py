def say_hello(name: str) -> str:
    """Greets a person

    Args:
        name (str): name of the person

    Returns:
        str
    """
    print(f"hello {name}")


if __name__ == "__main__":
    say_hello("John Doe")
