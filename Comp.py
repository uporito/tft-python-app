from Unit import Unit
import helperLib
from tft_constants import *

class Comp :
    
    def __init__(self, units : list[Unit]) -> None:
        self.units = units
        self.level = len(units)

        # compute initial synergies count
        self.synergies_count = {}
        for synergy in SET_8_SYNERGIES :
            self.synergies_count[synergy.name] = 0

        l = []
        for unit in self.units :
            l += unit.synergy_names
        for synergy in SET_8_SYNERGIES :
            self.synergies_count[synergy.name] = l.count(synergy.name)



    def __str__(self) -> str:
        return f'comp - level : {self.level}, units : {[u.name for u in self.units]}.'

    def get_comp_string_list(self) :
        synergies_count_string_list = [' - '.join([u.name for u in self.units]) + f" (level {self.level})"]
        self.synergies_count = dict(sorted(self.synergies_count.items(), key=lambda x:x[1], reverse=True))
        for synergy in self.synergies_count :
            if (self.synergies_count[synergy] > 0) :
                c = helperLib.find_level(synergy_levels[synergy], self.synergies_count[synergy])
                synergies_count_string_list.append(tuple( ("({}) {}".format(self.synergies_count[synergy], synergy), COLORS[c]) ))

        return synergies_count_string_list
                

    def add_unit(self, unit : Unit) :
        if not (unit in self.units) :   # update synergies if new unit
            for synergy in unit.synergy_names :
                if synergy in self.synergies_count.keys() :
                    self.synergies_count[synergy] = self.synergies_count[synergy] + 1
                else :
                    self.synergies_count[synergy] = 1

        self.units.append(unit)
        self.level += 1

        
    def remove_unit(self, unit : Unit) :
        self.units.remove(unit)
        if not (unit in self.units) :   # update synergies if last remaining
            for synergy in unit.synergy_names :
                self.synergies_count[synergy] = self.synergies_count[synergy] - 1

        self.level -= 1

    # Function to find suggestions for one synergy, for the next level only
    def find_synergy_suggestions(self, synergy_wanted : Synergy) :
        # print(f'Finding suggestions for {synergy_wanted.name}...')

        suggestions = []
        # check if one off next synergy levels
        if ( helperLib.find_level(synergy_wanted.levels, self.synergies_count[synergy_wanted.name] + 1) == (helperLib.find_level(synergy_wanted.levels, self.synergies_count[synergy_wanted.name]) + 1) ) :
            suggestions += [unit for unit in synergy_wanted.units if unit not in {unit.name for unit in self.units}]
        else :
            # print(f'more than 1 off next level for {synergy_wanted.name}')
            pass
            
        return (suggestions)

    # Function to find suggestions for an ordered/tiered ? list of wanted synergies, uses find_synergy_suggestions(), for the next level only
    def find_suggestions(self, synergies_wanted : list[str]) :
        suggestions = {}    # dictionnary of suggestions
        for synergy in synergies_wanted :
            for unit in self.find_synergy_suggestions([s for s in SET_8_SYNERGIES if s.name == synergy][0]) :
                if not (unit in suggestions.keys()) :   # unit not in dict yet
                    suggestions[unit] = 1
                else :
                    suggestions[unit] += 1
        return dict(sorted(suggestions.items(), key=lambda x:x[1], reverse=True))
