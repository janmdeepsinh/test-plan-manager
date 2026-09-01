def show_test_plan_summary():
    test_plans = [
        {"name": "Login Test", "status": "Passed"},
        {"name": "Checkout Test", "status": "Pending"},
    ]

    print("Test Plan Summary:")
    for plan in test_plans:
        print(f"- {plan['name']}: {plan['status']}")


def main():
    print("Test Plan Manager started")
    show_test_plan_summary()


if __name__ == "__main__":
    main()