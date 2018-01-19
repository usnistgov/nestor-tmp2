import collections

from Program.Database.Database_Properties import LabelEdges
from Program.Database.Database_Properties import NodeHuman
from Program.Database.Database_Properties import NodeTag


class MaintenanceWorkOrder():
    """
    The maintenance Work Order (MWO) represent every new MWO
    MWO are extracted from a CSV files and store in a Neo4J database using the my methods by create CYPHER queries

    In the database, a given MWO is split into different nodes used to create links between different MWOs
    a MWO can have only 1 node ISSUE and i node MACHINE (with 1 MACHINE_TYPE)
    But it can be linked with multiple OPERATOR and TECHNICIAN as well as multiple TAG

    In the future, it might be representing with the item of the soltuion and the one of the problem

    the MWO is represented in the database with the following information:
    (ISSUE) -[COVERED]-> (MACHINE) -[IS_A]-> (MACHINE_TYPE)
    (ISSUE) -[REQUESTED_BY]-> (OPERATOR)
    (ISSUE) -[SOLVE_BY]-> (TECHNICIAN)
    (ISSUE) -[PROBLEM]-> (TAG)
    (ISSUE) -[SOLUTION]-> (TAG)

    PARAMETERS:
            issue           --  (Object) Issue, The information specific to a MWO
            machine         --  (Object) Machine, the information based on the Machine
            operator        --  Array (Object) Human, the information of the Operators
            technician      --  Array (Object) Human, the information of the Technicians
            problemtags     --  Array (Object) Tag, the information of the Tag describing the problem
            solutiontags    --  Array (Object) Tag, the information of the Tag describing the solution


       METHODS:
            create_database --  return the query to create a new MWO
    """

    def __init__(self, issue, machine=None, operators=None, technicians=None, tag_items=None, tag_problems=None, tag_solutions=None):

        self.label_problem = LabelEdges.LABEL_PROBLEM.value
        self.label_solution = LabelEdges.LABEL_SOLUTION.value
        self.label_contains = LabelEdges.LABEL_CONTAINS.value
        self.label_requested = LabelEdges.LABEL_REQUESTED.value
        self.label_solve = LabelEdges.LABEL_SOLVE.value
        self.label_covered = LabelEdges.LABEL_COVERED.value
        self.label_is_a = LabelEdges.LABEL_ISA.value

        self._set_issue(issue)
        self._set_machine(machine)
        self._set_operators(operators)
        self._set_technicians(technicians)
        self._set_tag_items(tag_items)
        self._set_tag_problems(tag_problems)
        self._set_tag_solutions(tag_solutions)

    def _get_issue(self):
        return self.issue

    def _set_issue(self, issue):
        self.issue = issue

    def _get_machine(self):
        return self.machine

    def _set_machine(self, machine):
        self.machine = machine

    def _get_operators(self):
        return self.operators

    def _set_operators(self, operators):
        if operators is None or len(operators) == 0:
            self.operators = None
        else:
            if not isinstance(operators, collections.Iterable) or isinstance(operators, str):
                operators = [operators]
            self.operators = operators

    def _get_technician(self):
        return self.technicians

    def _set_technicians(self, technicians):
        if technicians is None or len(technicians) == 0:
            self.technicians = None
        else:
            if not isinstance(technicians, collections.Iterable) or isinstance(technicians, str):
                technicians = [technicians]
            self.technicians = technicians

    def _get_tag_items(self):
        return self.tag_items

    def _set_tag_items(self, tag_items):
        if tag_items is None or len(tag_items) == 0:
            self.tag_items = None
        else:
            if not isinstance(tag_items, collections.Iterable) or isinstance(tag_items, str):
                tag_items = [tag_items]
            self.tag_items = tag_items

    def _get_tag_problems(self):
        return self.tag_problemts

    def _set_tag_problems(self, tag_problems):
        if tag_problems is None or len(tag_problems) == 0:
            self.tag_problems = None
        else:
            if not isinstance(tag_problems, collections.Iterable) or isinstance(tag_problems, str):
                tag_problems = [tag_problems]
            self.tag_problemts = tag_problems

    def _get_tag_solutions(self):
        return self.tag_solutions

    def _set_tag_solutions(self, tag_solutions):
        if tag_solutions is None or len(tag_solutions) == 0:
            self.tag_solutions = None
        else:
            if not isinstance(tag_solutions, collections.Iterable) or isinstance(tag_solutions, str):
                tag_solutions = [tag_solutions]
            self.tag_solutions = tag_solutions

    def __str__(self):
        return "OBJECT: %s -->\n\t\t ISSUE:\n %s" \
               "\n\t\t MACHINE:\n %s" \
               "\n\t\t OPERATORS: \n %s" \
               "\n\t\t TECHNICIAN:\n %s" \
               "\n\t\t ITEM_TAG:\n %s" \
               "\n\t\t PROBLEM_TAGS:\n %s" \
               "\n\t\t SOLUTION_TAGS:\n %s" % \
               (type(self), self.issue, self.machine, self.operators, self.technicians, self.tag_items, self.tag_problemts,
                self.tag_solutions)

    def cypher_mwo_graphdata(self, var_issue, var_machine, var_machine_type, var_operators, var_technicians, var_tag_items,
                        var_tag_problemts, var_tag_solutions):
        """
        The query created an inuque Issue
        But merge the others:
            if a node already exists in the database with the given information
                it update it if this MWO have more information
            if a node didn't exists in the database
                it create a new one

        :param varIssue: A string to represent the Issue
        :param varMachine: A string to represent the Machine
        :param varMachinetype: A string to represent the Machine Type
        :param varOperators: A string to represent the Operators
        :param varTechnicians: A string to represent the Technicians
        :param varItemtag: A string to represent the Tag Item
        :param varProblemtags: A string to represent the Tag Problem Action
        :param varSolutiontags: A string to represent the Tag Solution Action
        :return: a query to create a new MWO
        """
        query = self.issue.cypher_create_issue_node(var_issue) + "\n"

        if self.machine._get_name() is not None:
            query += self.machine.cypher_machine_create_node(var_machine) + "\n"
            query += f'MERGE ({var_issue})-[{self.label_covered}]->({var_machine})' + "\n"

            if self.machine._get_machine_type() is not None:
                query += self.machine.cypher_machine_type_create_node(var_machine_type) + "\n"
                query += f'MERGE ({var_machine})-[{self.label_is_a}]->({var_machine_type})' + "\n"

        if self.operators is not None and len(self.operators) is not 0:
            for i in range(0, len(self.operators)):
                if self.operators[i]._get_name() is not None:
                    var_operator = f'{var_operators}{i}'
                    query +=self.operators[i].cypher_operator_create_node(var_operator) + "\n"
                    query += f'MERGE ({var_issue})-[{self.label_requested}]->({var_operator})' + "\n"

        if self.technicians is not None and len(self.technicians) is not 0:
            for i in range(0, len(self.technicians)):
                if self.technicians[i]._get_name() is not None:
                    var_technician = f'{var_technicians}{i}'
                    query += self.technicians[i].cypher_technician_create_node(var_technician) + "\n"
                    query += f'MERGE ({var_issue})-[{self.label_solve}]->({var_technician})' + "\n"

        if self.tag_items is not None and len(self.tag_items) is not 0:
            for i in range(0, len(self.tag_items)):
                if self.tag_items[i]._get_keyword() is not None:
                    var_tag_item = f'{var_tag_items}{i}'
                    query += self.tag_items[i].cypher_item_create_node(var_tag_item) + "\n"
                    query += f'MERGE ({var_issue})-[{self.label_contains}]->({var_tag_item})' + "\n"

        if self.tag_problemts is not None and len(self.tag_problemts) is not 0:
            for i in range(0, len(self.tag_problemts)):
                if self.tag_problemts[i]._get_keyword() is not None:
                    var_tag_problem = f'{var_tag_problemts}{i}'
                    query += self.tag_problemts[i].cypher_action_create_node(var_tag_problem) + "\n"
                    query += f'MERGE ({var_issue})-[{self.label_problem}]->({var_tag_problem})' + "\n"

        if self.tag_solutions is not None and len(self.tag_solutions) is not 0:
            for i in range(0, len(self.tag_solutions)):
                if self.tag_solutions[i]._get_keyword() is not None:
                    var_tag_solution = f'{var_tag_solutions}{i}'
                    query += self.tag_solutions[i].cypher_action_create_node(var_tag_solution) + "\n"
                    query += f'MERGE ({var_issue})-[{self.label_solution}]->({var_tag_solution})' + "\n"


        return query
