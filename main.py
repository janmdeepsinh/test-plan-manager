def show_test_plan_summary(test_plans):
    print("Test Plan Summary:")
    for plan in test_plans:
        print(f"- {plan['name']}: {plan['status']}")


def create_test_plan(test_plans, name, status="Pending"):
    new_plan = {"name": name, "status": status}
    test_plans.append(new_plan)
    print(f"Created new test plan: '{name}' with status '{status}'")
    return test_plans


def main():
    print("Test Plan Manager started")

    test_plans = [
        {"name": "Login Test", "status": "Passed"},
        {"name": "Checkout Test", "status": "Pending"},
    ]

    show_test_plan_summary(test_plans)

    # SCRUM-5: create a new task
    test_plans = create_test_plan(test_plans, "Signup Test")

    show_test_plan_summary(test_plans)


if __name__ == "__main__":
    main()