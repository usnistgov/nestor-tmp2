"""
File: human.py
Author: Sascha MOCCOZET
Organisation:
   Departament of Commerce USA
   National Institute of Standards and Technology - NIST
   Engineering Laboratory - EL
   Systems Integration Division - SID
   Information Modeling and Testing Group - IMTG
   <Insert Project Name>
Description:
   This file contains the object KPI,
   It represent every information needed to create any kind of query into the database to get and create KPI's

THE IDEA OF THIS KPI OBJECT IS STILL IN PROCESS, LOTS OF THE IDEA MIGHT CHANGE IN THE FUTUR
"""


import networkx as nx


from database_storage.objects.issue import *
from database_storage.objects.machine import *
from database_storage.objects.human import *
from database_storage.objects.tag import *
from database_storage.helper import updateDict

class Kpi:

    def __init__(self, operator= None, cypherMatch=set(), cypherWhere="", cypherReturn=set(), result=None):
        self.dict = {
            '=': '=',
            '<>': '<>',
            '<': '<',
            '>': '>',
            '<=': '<=',
            '>=': '>=',
            '0': 'IS NULL',
            '1': 'IS NOT NULL',
            '.-': 'STARTS WITH',
            '-.': 'ENDS WITH',
            '-': 'CONTAINS',
            '~': '=~'
        }
        self._set_operator(operator)
        self._set_result(result)

        self._set_cypherMatch(cypherMatch)
        self._set_cypherWhere(cypherWhere)
        self._set_cypherReturn(cypherReturn)

    def _get_result(self):
        return self.result

    def _set_result(self, result):
        self.result = result

    def _get_operator(self):
        return self.operator

    def _set_operator(self, operator):
        if operator in self.dict:
            self.operator = self.dict[operator]
        else:
            self.operator = None

    def _get_cypherMatch(self):
        return self.cypherMatch

    def _set_cypherMatch(self, cypherMatch):
        if cypherMatch:
            if isinstance(cypherMatch, str):
                self.cypherMatch.add(cypherMatch)
            else:
                self.cypherMatch.update(cypherMatch)
        else:
            self.cypherMatch = set()


    def _get_cypherWhere(self):
        return self.cypherWhere

    def _set_cypherWhere(self, cypherWhere):
        self.cypherWhere=cypherWhere

    def _get_cypherReturn(self):
        return self.cypherReturn

    def _set_cypherReturn(self, cypherReturn):
        if cypherReturn:
            if isinstance(cypherReturn, str):
                self.cypherReturn.add(cypherReturn)
            else:
                self.cypherReturn.update(cypherReturn)
        else:
            self.cypherReturn = set()

    def __add__(self, other):
        tmp = Kpi()

        cypherMatch = self.cypherMatch.union(other.cypherMatch)
        cypherWhere = self.mergeWhere(self.cypherWhere, other.cypherWhere, 'AND')
        cypherReturn = self.cypherReturn.union(other.cypherReturn)

        tmp._set_cypherMatch(cypherMatch)
        tmp._set_cypherWhere(cypherWhere)
        tmp._set_cypherReturn(cypherReturn)

        return tmp

    def __sub__(self, other):
        tmp = Kpi()

        cypherMatch = self.cypherMatch.union(other.cypherMatch)
        cypherWhere = self.mergeWhere(self.cypherWhere, other.cypherWhere, 'OR')
        cypherReturn = self.cypherReturn.union(other.cypherReturn)

        tmp._set_cypherMatch(cypherMatch)
        tmp._set_cypherWhere(cypherWhere)
        tmp._set_cypherReturn(cypherReturn)

        return tmp

    def __mul__(self, other):
        tmp = Kpi()

        cypherMatch = self.cypherMatch.union(other.cypherMatch)
        cypherWhere = self.mergeWhere(self.cypherWhere, other.cypherWhere, 'XOR')
        cypherReturn = self.cypherReturn.union(other.cypherReturn)

        tmp._set_cypherMatch(cypherMatch)
        tmp._set_cypherWhere(cypherWhere)
        tmp._set_cypherReturn(cypherReturn)

        return tmp

    def __neg__(self):
        tmp = Kpi()

        cypherMatch = self.cypherMatch
        cypherWhere = f'NOT {self.cypherWhere}'
        cypherReturn = self.cypherReturn

        tmp._set_cypherMatch(cypherMatch)
        tmp._set_cypherWhere(cypherWhere)
        tmp._set_cypherReturn(cypherReturn)

        return tmp


    def mergeWhere(self, where1, where2, operator):
        tmp = set()
        if where1 and where2:
            return f'{where1} {operator} {where2}'
        if where1:
            return where1
        if where2:
            return where2
        return ""

    def cypher_where(self):
        return "this function has to be defined for all the object inherit from kpi"

    def cypher_match(self):
        return "this function has to be defined for all the object inherit from kpi"

    def cypher_return(self):
        return "this function has to be defined for all the object inherit from kpi"

    def cypher_createQuery(self):
        if self.cypherReturn:
            query = f'MATCH {" ,".join(self.cypherMatch)}\n'
            if self.cypherWhere:
                query += f'WHERE {self.cypherWhere}\n'
            query += f'RETURN DISTINCT {", ".join(self.cypherReturn)}'
        else:
            query = None
        return query

    def cypherWhere_special(self, variable, property, value):
        if self.operator == "IS NULL" or self.operator == "IS NOT NULL":
            return f'{variable}.{property} {self.operator}'
        else:
            if isinstance(value, int):
                return f'{variable}.{property} {self.operator} {value}'
            else:
                return f'{variable}.{property} {self.operator} "{value}"'


class MachineKpi(Machine, Kpi):

    def __init__(self, name=None, manufacturer=None, locasion=None, machine_type=None, databaseInfo=None, operator=None, result=None):
        Machine.__init__(self, name=name, manufacturer=manufacturer, locasion=locasion, machine_type=machine_type, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)


        self.databaseInfo = databaseInfo

        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoMachine["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_machine="machine", variable_machinetype="machine_type"):
        cypherMatch = f'(issue{self.databaseInfo["issue"]["label"]["issue"]})' \
                      f'-[{self.databaseInfo["edges"]["issue-machine"]}]->' \
                      f'({variable_machine}{self.label})'
        if self.machine_type:
            cypherMatch += f'-[{self.databaseInfo["edges"]["machine-machinetype"]}]->' \
                           f'({variable_machinetype}{self.labelType})'

        return cypherMatch

    def cypher_where(self, variable_machine="machine", variable_machinetype="machine_type"):
        if self.name:
            return self.cypherWhere_special(variable_machine, self.databaseInfoMachine['properties']['name'], self.name)
        if self.location:
            return self.cypherWhere_special(variable_machine, self.databaseInfoMachine['properties']['location'], self.location)
        if self.manufacturer:
            return self.cypherWhere_special(variable_machine, self.databaseInfoMachine['properties']['manufacturer'], self.manufacturer)
        if self.machine_type:
            return self.cypherWhere_special(variable_machinetype, self.databaseInfoMachine['properties']['type'], self.machine_type)

        return None

    def cypher_return(self, variable_machine="machine", variable_machinetype="machine_type"):
        if self.result:
            if self.result == "type":
                return f'{variable_machinetype}.{self.databaseInfoMachine["properties"][self.result]}'
            else:
                return f'{variable_machine}.{self.databaseInfoMachine["properties"][self.result]}'



class IssueKpi(Issue, Kpi):

    def __init__(self, problem=None, solution=None, cause=None, effects=None,
                 part_in_process=None, necessary_part=None, machine_down=None,
                 cost=None,
                 date_machine_up=None, date_machine_down=None,
                 date_workorder_start=None, date_workorder_completion=None,
                 date_maintenance_technician_arrive=None,
                 date_problem_found=None, date_problem_solved=None,
                 date_part_ordered=None, date_part_received=None,
                 databaseInfo=None, operator=None, result=None):
        Issue.__init__(self, problem=problem, solution=solution, cause=cause, effects=effects,
                       part_in_process=part_in_process, necessary_part=necessary_part, machine_down=machine_down, cost=cost,
                       date_machine_up=date_machine_up, date_machine_down=date_machine_down, date_workorder_start=date_workorder_start,
                       date_workorder_completion=date_workorder_completion, date_maintenance_technician_arrive=date_maintenance_technician_arrive,
                       date_problem_found=date_problem_found, date_problem_solved=date_problem_solved, date_part_ordered=date_part_ordered,
                       date_part_received=date_part_received, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)


        self.databaseInfo = databaseInfo

        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())


    def _set_result(self, result):
        if result in self.databaseInfoIssue["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_issue="issue"):
        return f'({variable_issue}{self.label})'

    def cypher_where(self, variable_issue="issue"):
        if self.problem:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['description_problem'], self.problem)
        if self.solution:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['description_solution'], self.solution)
        if self.cause:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['description_cause'], self.cause)
        if self.effects:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['description_effect'], self.effects)
        if self.part_in_process:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['machine_down'], self.part_in_process)
        if self.necessary_part:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['necessary_part'], self.necessary_part)
        if self.date_machine_down:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['part_in_process'], self.date_machine_down)
        if self.cost:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['cost'], self.cost)

        if self.date_machine_up:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['date_machine_down'], self.date_machine_up)
        if self.date_machine_down:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['date_workorder_start'], self.date_machine_down)
        if self.date_workorder_start:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['date_maintenance_technician_arrive'], self.date_workorder_start)
        if self.date_workorder_completion:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['date_problem_found'], self.date_workorder_completion)
        if self.date_maintenance_technician_arrive:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['date_part_ordered'], self.date_maintenance_technician_arrive)
        if self.date_problem_found:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['date_part_received'], self.date_problem_found)
        if self.date_problem_solve:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['date_problem_solve'], self.date_problem_solve)
        if self.date_part_ordered:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['date_machine_up'], self.date_part_ordered)
        if self.date_part_received:
            return self.cypherWhere_special(variable_issue, self.databaseInfoIssue['properties']['date_workorder_completion'], self.date_part_received)
        return None

    def cypher_return(self, variable_issue="issue"):
        if self.result:
            return f'{variable_issue}.{self.databaseInfoIssue["properties"][self.result]}'


class HumanKpi(Human, Kpi):

    def __init__(self, name= None,
                 databaseInfo=None, operator=None, result=None):
        Human.__init__(self, name=name, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo

        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())


    def _set_result(self, result):
        if result in self.databaseInfoHuman["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_human="human"):
        return f'({variable_human}{self.label})'

    def cypher_where(self, variable_human="human"):
        if self.name:
            return self.cypherWhere_special(variable_human, self.databaseInfoHuman['properties']['name'], self.name)
        return None

    def cypher_return(self, variable_human="human"):
        if self.result:
            return f'{variable_human}.{self.databaseInfoHuman["properties"][self.result]}'


class OperatorKpi(Operator, Kpi):

    def __init__(self, name= None,
                 databaseInfo=None, operator=None, result=None):
        Operator.__init__(self, name=name, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)


        self.databaseInfo = databaseInfo

        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoHuman["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_operator="operator"):
        return  f'(issue{self.databaseInfo["issue"]["label"]["issue"]})' \
                f'-[{self.databaseInfo["edges"]["issue-machine"]}]->' \
                f'({variable_operator}{self.label})'

    def cypher_where(self, variable_operator="operator"):
        if self.name:
            return self.cypherWhere_special(variable_human, self.databaseInfoHuman['properties']['name'], self.name)
        return None

    def cypher_return(self, variable_operator="operator"):
        if self.result:
            return f'{variable_operator}.{self.databaseInfoHuman["properties"][self.result]}'


class TechnicianKpi(Technician, Kpi):

    def __init__(self, name= None, skills=None, crafts=None,
                 databaseInfo=None, operator=None, result=None):
        Technician.__init__(self, name=name, skills=skills, crafts=crafts, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)
        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoHuman["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_technician="technician"):
        return f'({variable_technician}{self.label})'

    def cypher_where(self, variable_technician="technician"):
        if self.name:
            return self.cypherWhere_special(variable_technician, self.databaseInfoHuman['properties']['name'], self.name)
        if self.skills:
            self.operator = "IN"
            return self.cypherWhere_special(variable_technician, self.databaseInfoHuman['properties']['skills'], self.skills)
        if self.crafts:
            self.operator = "IN"
            return self.cypherWhere_special(variable_technician, self.databaseInfoHuman['properties']['crafts'], self.crafts)
        return None

    def cypher_return(self, variable_technician="technician"):
        if self.result:
            return f'{variable_technician}.{self.databaseInfoHuman["properties"][self.result]}'


class TagKpi(Tag, Kpi):
    def __init__(self, keyword=None, synonyms= None,
                 databaseInfo=None, operator=None, result=None):
        Tag.__init__(self, keyword=keyword, synonyms=synonyms, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoTag["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_tag="tag"):
        return f'({variable_tag}{self.label})'

    def cypher_where(self, variable_tag="tag"):
        if self.keyword:
            return self.cypherWhere_special(variable_tag, self.databaseInfoTag['properties']['keyword'], self.keyword)
        if self.synonyms:
            self.operator = "IN"
            return self.cypherWhere_special(variable_tag, self.databaseInfoTag['properties']['synonyms'],self.synonyms)

        return None

    def cypher_return(self, variable_tag="tag"):
        if self.result:
            return f'{variable_tag}.{self.databaseInfoTag["properties"][self.result]}'


class TagOneGramKpi(TagOneGram, Kpi):
    def __init__(self, keyword=None, synonyms= None,
                 databaseInfo=None, operator=None, result=None):
        TagOneGram.__init__(self, keyword=keyword, synonyms=synonyms, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoTag["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_tagOnGram="onegram_tag"):
        return f'({variable_tagOnGram}{self.label})'

    def cypher_where(self, variable_tagOnGram="onegram_tag"):
        if self.keyword:
            return self.cypherWhere_special(variable_tagOnGram, self.databaseInfoTag['properties']['keyword'], self.keyword)
        if self.synonyms:
            self.operator = "IN"
            return self.cypherWhere_special(variable_tagOnGram, self.databaseInfoTag['properties']['synonyms'],self.synonyms)
        return None

    def cypher_return(self, variable_tagOnGram="onegram_tag"):
        if self.result:
            return f'{variable_tagOnGram}.{self.databaseInfoTag["properties"][self.result]}'


class TagItemKpi(TagItem, Kpi):
    def __init__(self, keyword=None, synonyms= None,
                 databaseInfo=None, operator=None, result=None):
        TagItem.__init__(self, keyword=keyword, synonyms=synonyms, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoTag["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_tagItem="tag_item"):
        return f'({variable_tagItem}{self.label})'

    def cypher_where(self, variable_tagItem="tag_item"):
        if self.keyword:
            return self.cypherWhere_special(variable_tagItem, self.databaseInfoTag['properties']['keyword'], self.keyword)
        if self.synonyms:
            self.operator = "IN"
            return self.cypherWhere_special(variable_tagItem, self.databaseInfoTag['properties']['synonyms'],self.synonyms)
        return None

    def cypher_return(self, variable_tagItem="tag_item"):
        if self.result:
            return f'{variable_tagItem}.{self.databaseInfoTag["properties"][self.result]}'


class TagProblemKpi(TagProblem, Kpi):
    def __init__(self, keyword=None, synonyms= None,
                 databaseInfo=None, operator=None, result=None):
        TagProblem.__init__(self, keyword=keyword, synonyms=synonyms, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoTag["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_tagProblem="tag_problem"):
        return f'({variable_tagProblem}{self.label})'

    def cypher_where(self, variable_tagProblem="tag_problem"):
        if self.keyword:
            return self.cypherWhere_special(variable_tagProblem, self.databaseInfoTag['properties']['keyword'], self.keyword)
        if self.synonyms:
            self.operator = "IN"
            return self.cypherWhere_special(variable_tagProblem, self.databaseInfoTag['properties']['synonyms'],self.synonyms)
        return None

    def cypher_return(self, variable_tagProblem="tag_problem"):
        if self.result:
            return f'{variable_tagProblem}.{self.databaseInfoTag["properties"][self.result]}'


class TagSolutionKpi(TagSolution, Kpi):
    def __init__(self, keyword=None, synonyms= None,
                 databaseInfo=None, operator=None, result=None):
        TagSolution.__init__(self, keyword=keyword, synonyms=synonyms, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoTag["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_tagSolution="tag_solution"):
        return f'({variable_tagSolution}{self.label})'

    def cypher_where(self, variable_tagSolution="tag_solution"):
        if self.keyword:
            return self.cypherWhere_special(variable_tagSolution, self.databaseInfoTag['properties']['keyword'], self.keyword)
        if self.synonyms:
            self.operator = "IN"
            return self.cypherWhere_special(variable_tagSolution, self.databaseInfoTag['properties']['synonyms'],self.synonyms)
        return None

    def cypher_return(self, variable_tagSolution="tag_solution"):
        if self.result:
            return f'{variable_tagSolution}.{self.databaseInfoTag["properties"][self.result]}'



class TagUnknownKpi(TagUnknown, Kpi):
    def __init__(self, keyword=None, synonyms= None,
                 databaseInfo=None, operator=None, result=None):
        TagUnknown.__init__(self, keyword=keyword, synonyms=synonyms, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoTag["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_tagUnknown="tag_unknown"):
        return f'({variable_tagUnknown}{self.label})'

    def cypher_where(self, variable_tagUnknown="tag_unknown"):
        if self.keyword:
            return self.cypherWhere_special(variable_tagUnknown, self.databaseInfoTag['properties']['keyword'], self.keyword)
        if self.synonyms:
            self.operator = "IN"
            return self.cypherWhere_special(variable_tagUnknown, self.databaseInfoTag['properties']['synonyms'],self.synonyms)
        return None

    def cypher_return(self, variable_tagUnknown="tag_unknown"):
        if self.result:
            return f'{variable_tagUnknown}.{self.databaseInfoTag["properties"][self.result]}'


class TagNGramKpi(TagNGram, Kpi):
    def __init__(self, keyword=None, synonyms= None,
                 databaseInfo=None, operator=None, result=None):
        TagNGram.__init__(self, keyword=keyword, synonyms=synonyms, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoTag["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_tagNGram="ngram_tag"):
        return f'({variable_tagNGram}{self.label})'

    def cypher_where(self, variable_tagNGram="ngram_tag"):
        if self.keyword:
            return self.cypherWhere_special(variable_tagNGram, self.databaseInfoTag['properties']['keyword'], self.keyword)
        if self.synonyms:
            self.operator = "IN"
            return self.cypherWhere_special(variable_tagNGram, self.databaseInfoTag['properties']['synonyms'],self.synonyms)
        return None

    def cypher_return(self, variable_tagNGram="ngram_tag"):
        if self.result:
            return f'{variable_tagNGram}.{self.databaseInfoTag["properties"][self.result]}'


class TagProblemItemKpi(TagProblemItem, Kpi):
    def __init__(self, keyword=None, synonyms= None,
                 databaseInfo=None, operator=None, result=None):
        TagProblemItem.__init__(self, keyword=keyword, synonyms=synonyms, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoTag["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_tagProblemItem="problemitem_tag"):
        return f'({variable_tagProblemItem}{self.label})'

    def cypher_where(self, variable_tagProblemItem="problemitem_tag"):
        if self.keyword:
            return self.cypherWhere_special(variable_tagProblemItem, self.databaseInfoTag['properties']['keyword'], self.keyword)
        if self.synonyms:
            self.operator = "IN"
            return self.cypherWhere_special(variable_tagProblemItem, self.databaseInfoTag['properties']['synonyms'],self.synonyms)
        return None

    def cypher_return(self, variable_tagProblemItem="problemitem_tag"):
        if self.result:
            return f'{variable_tagProblemItem}.{self.databaseInfoTag["properties"][self.result]}'


class TagSolutionItemKpi(TagSolutionItem, Kpi):
    def __init__(self, keyword=None, synonyms= None,
                 databaseInfo=None, operator=None, result=None):
        TagSolutionItem.__init__(self, keyword=keyword, synonyms=synonyms, databaseInfo=databaseInfo)
        Kpi.__init__(self, operator=operator, result=result)

        self.databaseInfo = databaseInfo
        self._set_result(result)

        self._set_cypherMatch(self.cypher_match())
        self._set_cypherWhere(self.cypher_where())
        self._set_cypherReturn(self.cypher_return())

    def _set_result(self, result):
        if result in self.databaseInfoTag["properties"]:
            self.result = result
        else:
            self.result = None

    def cypher_match(self, variable_tagSolutionItem="solutionitem_tag"):
        return f'({variable_tagSolutionItem}{self.label})'

    def cypher_where(self, variable_tagSolutionItem="solutionitem_tag"):
        if self.keyword:
            return self.cypherWhere_special(variable_tagSolutionItem, self.databaseInfoTag['properties']['keyword'], self.keyword)
        if self.synonyms:
            self.operator = "IN"
            return self.cypherWhere_special(variable_tagSolutionItem, self.databaseInfoTag['properties']['synonyms'],self.synonyms)
        return None

    def cypher_return(self, variable_tagSolutionItem="solutionitem_tag"):
        if self.result:
            return f'{variable_tagSolutionItem}.{self.databaseInfoTag["properties"][self.result]}'