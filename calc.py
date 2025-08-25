"""Engine performance calculation utilities."""

from __future__ import annotations


def horsepower(torque: float, rpm: float) -> float:
    """Calculate horsepower from torque and rpm.

    Args:
        torque: Engine torque in pound-feet.
        rpm: Engine speed in revolutions per minute.

    Returns:
        Horsepower as a float.
    """
    return torque * rpm / 5252


def torque(horsepower_value: float, rpm: float) -> float:
    """Calculate torque from horsepower and rpm.

    Args:
        horsepower_value: Horsepower value.
        rpm: Engine speed in revolutions per minute.

    Returns:
        Torque in pound-feet.
    """
    return horsepower_value * 5252 / rpm


def bmep(torque_value: float, displacement: float) -> float:
    """Calculate Brake Mean Effective Pressure (BMEP).

    Args:
        torque_value: Torque in pound-feet.
        displacement: Engine displacement in cubic inches.

    Returns:
        BMEP in pounds per square inch (psi).
    """
    return (150.8 * torque_value) / displacement


def piston_speed(stroke: float, rpm: float) -> float:
    """Calculate average piston speed.

    Args:
        stroke: Stroke in inches.
        rpm: Engine speed in revolutions per minute.

    Returns:
        Piston speed in feet per minute.
    """
    return 2 * stroke * rpm / 12


def airflow(displacement: float, rpm: float, ve: float) -> float:
    """Calculate airflow through the engine.

    Args:
        displacement: Engine displacement in cubic inches.
        rpm: Engine speed in revolutions per minute.
        ve: Volumetric efficiency as a decimal (0-1).

    Returns:
        Airflow in cubic feet per minute (CFM).
    """
    return displacement * rpm * ve / 3456

