import csv


def main():
    # Index of some of the key column
    NUMERATION = 0

    # Read the contents of a CSV file named personality.csv and store it in questions.
    questions = questionnaire("personality.csv", NUMERATION)

    # present questions to the user.
    Answers = form_questions(questions)

    # collect the answers of the user.
    try:
        E_I, S_I, T_F, J_P = answer(Answers)
    except IndexError as bad_index:
        print("Your Personality type is not deductible.\n")
        print()
    # parse answers into dichotmy
    try:
        I, E, S, N, T, F, J, P = dichotomy(E_I, S_I, T_F, J_P)
    except UnboundLocalError as bad_variable:
        print("You may try again later.")
        print("Or")
    except NameError as bad_variable:
        print("You may try again later.")
        print("Or")
    # provides dichotomous personality type to user in words.
    try:
        attitude, learning, decision, strategy = nomenclature(I, E, S, N, T, F, J, P)
    except UnboundLocalError as no_dychotomy:
        print("Please reach out to us so we can help you.")
        print()
    except NameError as no_dychotomy:
        print("Please reach out to us so we can help you.")
        print()
    # provides dichotomous personality type to user in letters.
    try:
        personality(attitude, learning, decision, strategy)
    except UnboundLocalError as no_personality:
        print("Developer's contacts:\n \nEmail: ndiramiye.robert@gmail.com")
    except NameError as no_personality:
        print("Developer's contacts:\n \nEmail: ndiramiye.robert@gmail.com")

    # provides explanation of personality type functions of the user.
    try:
        cognitive_functions(attitude, learning, decision, strategy)
    except UnboundLocalError as no_dychotomy:
        print()
        print("     Thank you!")
    except NameError as no_dychotomy:
        print()
        print("     Thank you!")

    print()


def questionnaire(filename, number):
    """This function reads the contents 
    of a CSV file named personality.csv and 
    store it in a dictionary called 'dictionary'."""
    dictionary = {}

    try:
        with open(filename,
                  "rt") as csv_file:  # Open the CSV file for reading and store a reference to the opened file in a variable named csv_file.
            reader = csv.reader(
                csv_file)  # Use the csv module to create a reader object that will read from the opened CSV file.
            next(reader)  # skip the first line

            for row in reader:
                key = row[number]
                dictionary[key] = row
    # Return the dictionary.

    except FileNotFoundError as not_found_err:
        print()
        print("☉ o☉ !!!  Oh Noooohh!! The questionnaire system is not connected!")
        print()

    return dictionary


def form_questions(questionnaire):
    """This fuction creates a questionnaire that is presetneted
    to a user to return the answers of the user in a list called
    'Answers'"""
    Answers = []
    for key, value in questionnaire.items():
        number = value[0]
        question = value[1]
        choiceA = value[2]
        choiceB = value[3]
        neutral_choice = value[4]
        ask = input(
            f"{number}. {question}:\n A. {choiceA}\n B. {choiceB}\n C. {neutral_choice}\n \nEnter The Letter Of Your Choice: ")
        print()
        print()
        ask = ask.upper()
        Answers.append(ask)
    # Return the dictionary.
    return Answers


def answer(answers):
    """This function distributes the answers of a user into
     different lists by index depending on the
     intended purpose of the question and returns the answers into
     variables according to their meaning"""
    INTROVERT_EXTROVERT_INDEX = (0, 7, 14, 21, 28, 35, 42, 49, 56, 63)
    SENSOR_INTUITIVE_INDEX = (1, 2, 8, 9, 15, 16, 22, 23, 29, 30, 36, 37, 43, 44, 50, 51, 57, 58, 64, 65)
    FEELER_THINKER_INDEX = (3, 4, 10, 11, 17, 18, 24, 25, 31, 32, 38, 39, 45, 46, 52, 53, 59, 60, 66, 67)
    PERCEIVER_JUDGER_INDEX = (5, 6, 12, 13, 19, 20, 26, 27, 33, 34, 40, 41, 47, 48, 54, 55, 61, 62, 68, 69)
    INTROVERT_EXTROVERT = list(map(answers.__getitem__, INTROVERT_EXTROVERT_INDEX))
    SENSOR_INTUITIVE = list(map(answers.__getitem__, SENSOR_INTUITIVE_INDEX))
    FEELER_THINKER = list(map(answers.__getitem__, FEELER_THINKER_INDEX))
    PERCEIVER_JUDGER = list(map(answers.__getitem__, PERCEIVER_JUDGER_INDEX))

    return INTROVERT_EXTROVERT, SENSOR_INTUITIVE, FEELER_THINKER, PERCEIVER_JUDGER


def dichotomy(E_I, S_I, T_F, J_P):
    """This function creates a dichotomy that parses
    each list from the function answer() into specific personality
    type traits"""
    Introvert = 0
    Extrovert = 0
    Neutral_E_I = 0
    Intuitive = 0
    Sensor = 0
    Neutral_S_I = 0
    Thinker = 0
    Feeler = 0
    Neutral_T_F = 0
    Perceiver = 0
    Judger = 0
    Neutral_J_P = 0

    for result in E_I:
        if result == "A":
            Extrovert += 1
        elif result == "B":
            Introvert += 1
        elif result == "C":
            Neutral_E_I += 1
        else:
            Neutral_E_I += 1
            print("You have made an invalid choice.\nIt will be considered neutral")
            print()
    for result in S_I:
        if result == "A":
            Sensor += 1
        elif result == "B":
            Intuitive += 1
        elif result == "C":
            Neutral_S_I += 1
        else:
            Neutral_S_I += 1
            print("You have made an invalid choice.\nIt will be considered neutral")
            print()
    for result in T_F:
        if result == "A":
            Thinker += 1
        elif result == "B":
            Feeler += 1
        elif result == "C":
            Neutral_T_F += 1
        else:
            Neutral_T_F += 1
            print("You have made an invalid choice.\nIt will be considered neutral")
            print()
    for result in J_P:
        if result == "A":
            Judger += 1
        elif result == "B":
            Perceiver += 1
        elif result == "C":
            Neutral_J_P += 1
        else:
            Neutral_J_P += 1
            print("You have made an invalid choice.\nIt will be considered neutral")
            print()
    return Introvert, Extrovert, Sensor, Intuitive, Thinker, Feeler, Judger, Perceiver


def nomenclature(Introversion, Extraversion, Sensing, Intuition, Thinking, Feeling, Judging, Perceiving):
    """This function provides the nomenclature of personality
    to a user by using their traits"""
    Attitude = 'INTROVERT' if Introversion > Extraversion else 'EXTROVERT'
    counter_att = "EXTROVERT" if Introversion > Extraversion else 'INTROVERT'
    Attitude_perc = round(100 * (Introversion / 10 if Introversion > Extraversion else Extraversion / 10), 3)

    Learning = 'OBSERVER' if Sensing > Intuition else 'INTUITIVE'
    counter_lea = 'INTUITIVE' if Sensing > Intuition else 'OBSERVER'
    Learning_perc = round(100 * (Sensing / 20 if Sensing > Intuition else Intuition / 20), 3)

    Deciding = 'THINKER' if Thinking > Feeling else 'FEELER'
    counter_dec = 'FEELER' if Thinking > Feeling else 'THINKER'
    Deciding_perc = round(100 * (Thinking / 20 if Thinking > Feeling else Feeling / 20), 3)

    Strategy = 'JUDGER' if Judging > Perceiving else 'PERCEIVER'
    counter_strat = 'PERCEIVER' if Judging > Perceiving else 'JUDGER'
    Strategy_perc = round(100 * (Judging / 20 if Judging > Perceiving else Perceiving / 20), 3)

    print("--------------------------------------------------")
    print("              How you ◉ ‿ ◉ are:")
    print("--------------------------------------------------")
    print(f"      {Attitude}       |       {counter_att}")
    print(f"          {Attitude_perc}%                     {100 - Attitude_perc}%")
    print("--------------------------------------------------")
    print(f"      {Learning}       |       {counter_lea}")
    print(f"          {Learning_perc}%                     {100 - Learning_perc}%")
    print("--------------------------------------------------")
    print(f"         {Deciding}       |       {counter_dec}")
    print(f"          {Deciding_perc}%                     {100 - Deciding_perc}%")
    print("--------------------------------------------------")
    print(f"      {Strategy}       |       {counter_strat}")
    print(f"          {Strategy_perc}%                     {100 - Strategy_perc}%")
    print("--------------------------------------------------")

    return Attitude, Learning, Deciding, Strategy


def personality(ATTITUDE, LEARNING, DECISION, STRATEGY):
    """This function provides the symbol name of personality
    to a user by using their traits"""
    if ATTITUDE == "INTROVERT":
        attitude_symbol = "I"

    elif ATTITUDE == "EXTROVERT":
        attitude_symbol = "E"

    elif ATTITUDE == "AMBIVERT":
        attitude_symbol = "X"

    if LEARNING == "INTUITIVE":
        learning_symbol = "N"

    elif LEARNING == "OBSERVER":
        learning_symbol = "S"

    elif LEARNING == "UNKNOWN":
        learning_symbol = "X"

    if DECISION == "THINKER":
        decision_symbol = "T"

    elif DECISION == "FEELER":
        decision_symbol = "F"

    elif DECISION == "UNKNOWN":
        decision_symbol = "X"

    if STRATEGY == "JUDGER":
        strategy_symbol = "J"

    elif STRATEGY == "PERCEIVER":
        strategy_symbol = "P"

    elif STRATEGY == "UNKNOWN":
        strategy_symbol = "X"
    print(f"\nPersonality Type ʘ‿ ʘ: {attitude_symbol}{learning_symbol}{decision_symbol}{strategy_symbol}\n")


def cognitive_functions(ATTITUDE, LEARNING, DECISION, STRATEGY):
    """This function uses the data of personality traits to
    deduce and provide a user with cognitive functions of
    they are predisposed to have and an explanation of these functions"""
    print("**************************************************")
    print("✯ If you are Introverted, the cognitive function you use\nfirst is also an introverted function.")
    print()
    print("✯ If you are Extroverted, the cognitive function you use\nfirst is also an Extroverted function.")
    to_learn = "★ You use the following process to learn:"
    to_decide = "★ You use the following process to make decisions:"
    if ATTITUDE == "INTROVERT" and STRATEGY == "PERCEIVER":
        if DECISION == "THINKER":
            TP = "Introverted Thinking [Ti]:\n Understanding the nature of causation\nOr\nUnderstanding causation is not correlation.\n Clarity/Accuracy/Truth/Logic"
            print(f"\n{to_decide}:")
            print("--------------------------------------------------")
            print(TP)
        elif DECISION == "FEELER":
            FP = "Introverted Feeling [Fi]:\n Understanding emotions and values of the self and acting accordingly\n Authenticity/Knowing good and bad"
            print(f"\n{to_learn}:")
            print("--------------------------------------------------")
            print(FP)
            print()
        if LEARNING == "INTUITIVE":
            NP = "Extroverted Intuition [Ne]:\n Using information to create something new.\n Asks 'WHAT IF?'"
            print(f"\n{to_learn}:")
            print("--------------------------------------------------")
            print(NP)
            print()
        elif LEARNING == "OBSERVER":
            SP = "Extroverted Sensing [Se]:\n Being ready to respond to spontaneity and surprising experience/Being physically and mentaly ready. \n Physical Sensitivity/Perpetual Observing"
            print(f"\n{to_learn}:")
            print("--------------------------------------------------")
            print(SP)
            print()

    elif ATTITUDE == "EXTROVERT" and STRATEGY == "PERCEIVER":
        if LEARNING == "INTUITIVE":
            NP = "Extroverted Intuition [Ne]:\n Using information to create something new.\n Asks 'WHAT IF?'"
            print(f"\n{to_learn}:")
            print("--------------------------------------------------")
            print(NP)
            print()
        elif LEARNING == "OBSERVER":
            SP = "Extroverted Sensing [Se]:\n Being ready to respond to spontaneity and surprising experience/Being physically and mentaly ready. \n Physical Sensitivity/Perpetual Observing"
            print(f"\n{to_learn}:")
            print("--------------------------------------------------")
            print(SP)
            print()
        if DECISION == "THINKER":
            TP = "Introverted Thinking [Ti]:\n Understanding the nature of causation\nOr\nUnderstanding causation is not correlation.\n Clarity/Accuracy/Truth/Logic"
            print(f"\n{to_decide}:")
            print("--------------------------------------------------")
            print(TP)
            print()
        elif DECISION == "FEELER":
            FP = "Introverted Feeling [Fi]:\n Understanding emotions and values of the self and acting accordingly\n Authenticity/Knowing good and bad"
            print(f"\n{to_decide}:")
            print("--------------------------------------------------")
            print(FP)
            print()

    elif ATTITUDE == "EXTROVERT" and STRATEGY == "JUDGER":
        if DECISION == "THINKER":
            TJ = "Extraverted Thinking [Te]:\n Understanding priority\n Organization/Effectiveness/Usefulness"
            print(f"\n{to_decide}:")
            print("--------------------------------------------------")
            print(TJ)
            print()
        elif DECISION == "FEELER":
            FJ = "Extroverted Feeling [Fe]:\n Understanding other people's emotions and acting accordingly\n Harmony/Togetherness"
            print(f"\n{to_decide}:")
            print("--------------------------------------------------")
            print(FJ)
            print()
        if LEARNING == "INTUITIVE":
            NJ = "Introverted Intuition [Ni]:\n Using information to understand what is most probable.\n Asks 'WHY?'"
            print(f"\n{to_learn}:")
            print("--------------------------------------------------")
            print(NJ)
            print()
        elif LEARNING == "OBSERVER":
            SJ = "Introverted Sensing [Si]:\n Storing useful facts and experience to use later for a desired outcome.\n Protection/Safe-keeing/Memory"
            print(f"\n{to_learn}:")
            print("--------------------------------------------------")
            print(SJ)
            print()

    elif ATTITUDE == "INTROVERT" and STRATEGY == "JUDGER":
        if LEARNING == "INTUITIVE":
            NJ = "Introverted Intuition [Ni]:\n Using information to understand what is most probable.\n Asks 'WHY?'"
            print(f"\n{to_learn}:")
            print("--------------------------------------------------")
            print(NJ)
            print()
        elif LEARNING == "OBSERVER":
            SJ = "Introverted Sensing [Si]:\n Storing useful facts and experience to use later for a desired outcome.\n Protection/Safe-keeing/Memory"
            print(f"\n{to_learn}:")
            print("--------------------------------------------------")
            print(SJ)
            print()
        if DECISION == "THINKER":
            TJ = "Extraverted Thinking [Te]:\n Understanding priority\n Organization/Effectiveness/Usefulness"
            print(f"\n{to_decide}:")
            print("--------------------------------------------------")
            print(TJ)
            print()
        elif DECISION == "FEELER":
            FJ = "Extroverted Feeling [Fe]:\n Understanding other people's emotions and acting accordingly\n Harmony/Togetherness"
            print(f"\n{to_decide}:")
            print("--------------------------------------------------")
            print(FJ)
    print("**************************************************")


# Call main to start this program.
if __name__ == "__main__":
    main()
