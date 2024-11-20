from Game.Game_ascii_art.casual_garbage_can import ascii_carbage_can
from Game.airport_selection_function import airportselection
from Game.game_texts import yes, no, approve, tax_free_question, money_is_zero_str, garbage_can_question, \
    airport_selection_question, no_money_for_flight_str
from Game.garbage_can import garbage_can
from Game.sql_querys.money_function import fetch_player_money
from Game.taxfree import yes_no_taxfree

class Section:
    """Sections of the game. Each section happens max once in one airport."""

    def __init__(self, question, action, approved_answer, negative_answer, art, number_to_be_checked, condition_minimum,
                 condition_explanation):
        self.question = str(question)
        self.action = action
        self.approved_answer = approved_answer
        self.other_answer = negative_answer
        self.art = art
        self.function_to_number = number_to_be_checked
        self.condition_minimum = condition_minimum
        self.condition_explanation = condition_explanation

    def check_condition(self, parameter_int):
        if self.function_to_number(parameter_int) >= self.condition_minimum:
            return True


garbage_can_section = Section(question=garbage_can_question,
                              action=garbage_can,
                              approved_answer=[yes],
                              negative_answer=[no],
                              art=ascii_carbage_can,
                              number_to_be_checked=fetch_player_money,
                              condition_minimum=1,
                              condition_explanation=money_is_zero_str)

tax_free_section = Section(question=tax_free_question,
                           action=yes_no_taxfree,
                           approved_answer=[yes],
                           negative_answer=[no],
                           art="",
                           number_to_be_checked=fetch_player_money,
                           condition_minimum=1,
                           condition_explanation=money_is_zero_str)

flight_section = Section(question=airport_selection_question,
                         action=airportselection,
                         approved_answer=[approve],
                         negative_answer=[],
                         art="",
                         number_to_be_checked=fetch_player_money,
                         condition_minimum=50,
                         condition_explanation=no_money_for_flight_str)