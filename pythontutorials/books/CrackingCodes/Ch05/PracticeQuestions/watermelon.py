""" Watermelon.py

Demonstration for :py:mod:`CrackingCodes.Ch05.PracticeQuestions.Question3`

Note:
    Contains spoilers for Chapter 7 (functions)
"""


def nutrition() -> None:
    """Watermelon nutrition info.

    Contains nutrition facts of a serving of watermelon.

    Returns:
      Prints a series of strings containing the nutrition facts of a serving of watermelon.
    """
    print("Serving: About 2 cups, diced (280g)\n",
          "___________________________________\n",
          "Calories: 80\n",
          "___________________________________\n",
          "Total Fat: 0g\n",
          "Cholesterol: 0mg\n",
          "Sodium: 0mg\n",
          "Total Carbohydrate: 21g\n",
          "  Dietary Fiber: 1g\n",
          "  Total Sugars: 17g\n",
          "    Includes 0g Added Sugars\n",
          "Protein: 2g\n",
          "___________________________________\n",
          "Vitamin D: 0mcg\n",
          "Calcium: 20mg\n",
          "Iron: 0.7mg\n",
          "Potassium: 310mg\n",
          "Vitamin A: 80mcg\n",
          "Vitamin C: 23mg\n",
          "___________________________________\n",
          "INGREDIENTS: WATERMELON, RAW\n",
          "Source: https://www.watermelon.org/assets/Nutrition/FDAWatermelonLabel.pdf")
    return None


def main():
    nutrition()
    return None


if __name__ == "__main__":
    main()
