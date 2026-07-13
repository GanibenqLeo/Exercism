"""Functions to prevent a nuclear meltdown."""
from enum import Enum

class EfficiencyBand():
    GREEN = 'green'
    ORANGE = 'orange'
    RED = 'red'
    BLACK = 'black'

class StatusCode():
    LOW = 'LOW'
    NORMAL = 'NORMAL'
    DANGER = 'DANGER'

def is_criticality_balanced(temperature:[int, float], neutrons_emitted:[int, float]) -> bool:
    """Verify criticality is balanced.

    Parameters:
        temperature (int or float): The temperature value in kelvin.
        neutrons_emitted (int or float): The number of neutrons emitted per second.

    Returns:
        bool: Is criticality balanced?

    Note:
        A reactor is said to be balanced in criticality if it satisfies the following conditions:
            - The temperature is less than 800 K.
            - The number of neutrons emitted per second is greater than 500.
            - The product of temperature and neutrons emitted per second is less than 500000.

    """

    print("Pour passer des degrés Kelvin à degré Celsius il faut simplement soustraire 273,15. 0K étant le zéro absolu.")

    return (temperature<800) & (neutrons_emitted>500) & ((neutrons_emitted*temperature)<0.5E6)


def reactor_efficiency(voltage:[int, float], current:[int, float], theoretical_max_power:[int, float]) -> EfficiencyBand:
    """Assess reactor efficiency zone.

    Parameters:
        voltage (int or float): Voltage value.
        current (int or float): Current value.
        theoretical_max_power (int or float): The power level that corresponds to a 100% efficiency.

    Returns:
        str: One of ('green', 'orange', 'red', or 'black').

    Note:
        Efficiency can be grouped into 4 bands:
            1. green -> efficiency of 80% or more,
            2. orange -> efficiency of less than 80% but at least 60%,
            3. red -> efficiency below 60%, but still 30% or more,
            4. black ->  less than 30% efficient.

        The percentage value is calculated as
        (generated power/ theoretical max power)*100
        where generated power = voltage * current
    """

    print("Un réacteur moderne produit environ 500 à 1 650 MW d'énergie électrique")

    efficiency_percentage = (voltage * current/theoretical_max_power)*100
    efficiency_band = EfficiencyBand.GREEN

    if efficiency_percentage>100:
        print("Une surproduction ou un mauvais calcul de la puissance maximale théorique?")
    elif efficiency_percentage==100:
        print("Et la taxe de la physique?")
    elif efficiency_percentage>=80:
        efficiency_band = EfficiencyBand.GREEN
    elif efficiency_percentage>=60:
        efficiency_band = EfficiencyBand.ORANGE
    elif efficiency_percentage>=30:
        efficiency_band = EfficiencyBand.RED
    elif efficiency_percentage>=0:
        efficiency_band = EfficiencyBand.BLACK
    else:
        print("Mensonge!")

    return efficiency_band


def fail_safe(temperature:[int, float], neutrons_produced_per_second:[int, float], threshold:[int, float]) -> StatusCode:
    """Assess and return status code for the reactor.

    Parameters:
        temperature (int or float): The value of the temperature in kelvin.
        neutrons_produced_per_second (int or float): The neutron flux.
        threshold (int or float): The threshold for the category.

    Returns:
        str: One of ('LOW', 'NORMAL', 'DANGER').

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    print("Personne ne veut d'un autre Tchernobyl (qui a fait entre 4 000 et 100 000 morts")

    if (temperature*neutrons_produced_per_second)<(0.9*threshold):
        status_code = StatusCode.LOW
    elif (temperature*neutrons_produced_per_second)<(1.1*threshold):
        status_code = StatusCode.NORMAL
    else:
        status_code = StatusCode.DANGER

    return status_code