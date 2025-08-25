"""Command-line interface for engine performance calculations."""

from calc import horsepower, bmep, piston_speed, airflow


def prompt_float(prompt: str) -> float:
    """Prompt the user for a floating-point number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    """Prompt for inputs and display calculated engine metrics."""
    displacement = prompt_float("Enter engine displacement (cu in): ")
    stroke = prompt_float("Enter stroke (in): ")
    rpm = prompt_float("Enter engine RPM: ")
    ve_percent = prompt_float("Enter volumetric efficiency (%): ")
    torque_value = prompt_float("Enter torque (lb-ft): ")

    ve = ve_percent / 100.0

    hp = horsepower(torque_value, rpm)
    bmep_val = bmep(torque_value, displacement)
    ps = piston_speed(stroke, rpm)
    af = airflow(displacement, rpm, ve)

    rows = [
        ("Horsepower (hp)", hp),
        ("Torque (lb-ft)", torque_value),
        ("BMEP (psi)", bmep_val),
        ("Piston Speed (ft/min)", ps),
        ("Airflow (CFM)", af),
    ]

    header = f"{'Metric':<25}{'Value':>15}"
    print("\n" + header)
    print("-" * len(header))
    for label, value in rows:
        print(f"{label:<25}{value:>15.2f}")


if __name__ == "__main__":
    main()
