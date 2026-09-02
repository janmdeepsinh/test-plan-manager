def show_test_plan_summary(test_plans):
    print("Test Plan Summary:")
    for plan in test_plans:
        print(f"- {plan['name']}: {plan['status']} ({len(plan['test_cases'])} test case(s))")


def create_test_plan(test_plans, name, status="Pending"):
    new_plan = {"name": name, "status": status, "test_cases": []}
    test_plans.append(new_plan)
    print(f"Created new test plan: '{name}' with status '{status}'")
    return test_plans


def add_test_case(test_plan, case_name):
    new_case = {"case_name": case_name, "tester": None, "status": "Not Executed"}
    test_plan["test_cases"].append(new_case)
    print(f"Added test case '{case_name}' to plan '{test_plan['name']}'")
    return test_plan


def assign_tester(test_plan, case_name, tester_name):
    for case in test_plan["test_cases"]:
        if case["case_name"] == case_name:
            case["tester"] = tester_name
            print(f"Assigned '{tester_name}' to test case '{case_name}'")
            return case
    print(f"Test case '{case_name}' not found in plan '{test_plan['name']}'")
    return None


def main():
    print("Test Plan Manager started")

    test_plans = [
        {"name": "Login Test", "status": "Passed", "test_cases": []},
        {"name": "Checkout Test", "status": "Pending", "test_cases": []},
    ]

    show_test_plan_summary(test_plans)

    # SCRUM-5: create a new task
    test_plans = create_test_plan(test_plans, "Signup Test")

    # SCRUM-7: add test cases to a test plan
    add_test_case(test_plans[-1], "Verify email validation on signup form")
    add_test_case(test_plans[-1], "Verify duplicate email is rejected")

    # SCRUM-8: assign tester to a test case
    assign_tester(test_plans[-1], "Verify email validation on signup form", "Jan")

    show_test_plan_summary(test_plans)


if __name__ == "__main__":
    main()