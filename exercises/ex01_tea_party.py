"""Planning My Cozy Tea Party"""

__author__ = "730574207"


def main_planner(guests: int) -> None:
    """Tea Party information based on number of guests"""
    required_tea = tea_bags(people=guests)
    required_treats = treats(people=guests)
    combined_cost = cost(tea_count=required_tea, treat_count=required_treats)

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(required_tea))
    print("Treats: " + str(required_treats))
    print("Cost: $" + str(combined_cost))


def tea_bags(people: int) -> int:
    """Assuming each person uses two tea bags, this
    function multiplies the number of people by 2 to
    calculate total teabags needed"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the total number of teas using the tea_bags function.
    Then calculates number of treats by teas x 1.5"""
    teas = tea_bags(people=people)
    return int(teas * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Converts count for tea and treat to float type"""
    tea_cost: float = tea_count * 0.50
    treat_cost: float = treat_count * 0.75
    combined_cost: float = tea_cost + treat_cost
    return combined_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
