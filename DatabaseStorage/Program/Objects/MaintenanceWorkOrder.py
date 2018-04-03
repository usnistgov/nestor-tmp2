import collections


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

    def __init__(self, issue=None, machine=None, operators=None, technicians=None, tag_items=None, tag_problems=None,
                 tag_solutions=None, tag_unknowns=None, tag_problemItems=None, tag_solutionsItems=None,  databaseInfo=None):

        #self.databaseInfo = databaseInfo
        self.databaseInfoEdges = databaseInfo['edges']
        self._set_issue(issue)
        self._set_machine(machine)
        self._set_operators(operators)
        self._set_technicians(technicians)
        self._set_tag_items(tag_items)
        self._set_tag_problems(tag_problems)
        self._set_tag_solutions(tag_solutions)
        self._set_tag_unknowns(tag_unknowns)
        self._set_tag_problemItems(tag_problemItems)
        self._set_tag_solutionsItems(tag_solutionsItems)

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
        if not operators:
            self.operators = None
        else:
            if not isinstance(operators, collections.Iterable) or isinstance(operators, str):
                operators = [operators]
            self.operators = operators

    def _get_technician(self):
        return self.technicians

    def _set_technicians(self, technicians):
        if not technicians:
            self.technicians = None
        else:
            if not isinstance(technicians, collections.Iterable) or isinstance(technicians, str):
                technicians = [technicians]
            self.technicians = technicians

    def _get_tag_items(self):
        return self.tag_items

    def _set_tag_items(self, tag_items):
        if not tag_items:
            self.tag_items = None
        else:
            if not isinstance(tag_items, collections.Iterable) or isinstance(tag_items, str):
                tag_items = [tag_items]
            self.tag_items = tag_items

    def _get_tag_problems(self):
        return self.tag_problems

    def _set_tag_problems(self, tag_problems):
        if not tag_problems:
            self.tag_problems = None
        else:
            if not isinstance(tag_problems, collections.Iterable) or isinstance(tag_problems, str):
                tag_problems = [tag_problems]
            self.tag_problems = tag_problems

    def _get_tag_solutions(self):
        return self.tag_solutions

    def _set_tag_solutions(self, tag_solutions):
        if not tag_solutions:
            self.tag_solutions = None
        else:
            if not isinstance(tag_solutions, collections.Iterable) or isinstance(tag_solutions, str):
                tag_solutions = [tag_solutions]
            self.tag_solutions = tag_solutions

    def _get_tag_unknowns(self):
        return self.tag_unknowns

    def _set_tag_unknowns(self, tag_unknowns):
        if not tag_unknowns:
            self.tag_unknowns = None
        else:
            if not isinstance(tag_unknowns, collections.Iterable) or isinstance(tag_unknowns, str):
                tag_unknowns = [tag_unknowns]
            self.tag_unknowns = tag_unknowns

    def _get_tag_problemItems(self):
        return self.tag_problemItems

    def _set_tag_problemItems(self, tag_problemItems):
        if not tag_problemItems:
            self.tag_problemItems = None
        else:
            if not isinstance(tag_problemItems, collections.Iterable) or isinstance(tag_problemItems, str):
                tag_problemItems = [tag_problemItems]
            self.tag_problemItems = tag_problemItems

    def _get_tag_solutionsItems(self):
        return self.tag_solutionsItems

    def _set_tag_solutionsItems(self, tag_solutionsItems):
        if not tag_solutionsItems:
            self.tag_solutionsItems = None
        else:
            if not isinstance(tag_solutionsItems, collections.Iterable) or isinstance(tag_solutionsItems, str):
                tag_solutionsItems = [tag_solutionsItems]
            self.tag_solutionsItems = tag_solutionsItems

    def __str__(self):
        return "OBJECT: %s -->\n\t\t ISSUE:\n %s" \
               "\n\t\t MACHINE:\n %s" \
               "\n\t\t OPERATORS: \n %s" \
               "\n\t\t TECHNICIAN:\n %s" \
               "\n\t\t ITEM_TAG:\n %s" \
               "\n\t\t PROBLEM_TAGS:\n %s" \
               "\n\t\t SOLUTION_TAGS:\n %s" % \
               (type(self), self.issue, self.machine, self.operators, self.technicians, self.tag_items,
                self.tag_problemts,
                self.tag_solutions)

    def cypher_mwo_createGraphData(self, var_issue="issue", var_machine="machine", var_machine_type="machine_type",
                             var_operators="operators", var_technicians="technicians", var_tag_items="items",
                             var_tag_problems="problems", var_tag_solutions="solutions", var_tag_unknowns="unknowns",
                             var_tag_problemItems="tag_problemItems", var_tag_solutionItems="tag_solutionItems"):
        ## TODO add the code for the other tag unknown and stopword

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

        query = self.issue.cypher_issue_createNode(var_issue) + "\n"

        if self.machine:
            query += self.machine.cypher_machine_createNode(var_machine) + "\n"
            query += f'MERGE ({var_issue})-[{self.databaseInfoEdges["issue-machine"]}]->({var_machine})' + "\n"

            if not self.machine:
                query += self.machine.cypher_machineType_createNode(var_machine_type) + "\n"
                query += f'MERGE ({var_machine})-[{self.databaseInfoEdges["issue-machine"]}]->({var_machine_type})' + "\n"

        if self.operators:
            for index, operator in enumerate(self.operators):
                if operator:
                    var = var_operators + str(index)
                    query += operator.cypher_operator_createNode(var) + "\n"
                    query += f'MERGE ({var_issue})-[{self.databaseInfoEdges["issue-operator"]}]->({var})' + "\n"

        if self.technicians:
            for index, technician in enumerate(self.technicians):
                if technician:
                    var = var_technicians + str(index)
                    query += technician.cypher_technician_createNode(var) + "\n"
                    query += f'MERGE ({var_issue})-[{self.databaseInfoEdges["issue-technician"]}]->({var})' + "\n"

        if self.tag_items:
            for index, item in enumerate(self.tag_items):
                if item:
                    var = var_tag_items + str(index)
                    query += item.cypher_itemTag_createNode(var) + "\n"
                    query += f'MERGE ({var_issue})-[{self.databaseInfoEdges["issue-item"]}]->({var})' + "\n"

        if self.tag_problems:
            for index, problem in enumerate(self.tag_problems):
                if problem:
                    var = var_tag_problems + str(index)
                    query += problem.cypher_problemTag_createNode(var) + "\n"
                    query += f'MERGE ({var_issue})-[{self.databaseInfoEdges["issue-problem"]}]->({var})' + "\n"

        if self.tag_solutions:
            for index, solution in enumerate(self.tag_solutions):
                if solution:
                    var = var_tag_solutions + str(index)
                    query += solution.cypher_solutionTag_createNode(var) + "\n"
                    query += f'MERGE ({var_issue})-[{self.databaseInfoEdges["issue-solution"]}]->({var})' + "\n"

        if self.tag_unknowns:
            for index, unknown in enumerate(self.tag_unknowns):
                if unknown:
                    var = var_tag_unknowns + str(index)
                    query += unknown.cypher_unknownTag_createNode(var) + "\n"
                    query += f'MERGE ({var_issue})-[{self.databaseInfoEdges["issue-unknown"]}]->({var})' + "\n"

        if self.tag_problemItems:
            for index, problemItem in enumerate(self.tag_problemItems):
                if problemItem:
                    var = var_tag_problemItems + str(index)
                    query += problemItem.cypher_problemItemTag_createNode(var) + "\n"
                    query += f'MERGE ({var_issue})-[{self.databaseInfoEdges["issue-problemitem"]}]->({var})' + "\n"

        if self.tag_solutionsItems:
            for index, solutionItem in enumerate(self.tag_solutionsItems):
                if solutionItem:
                    var = var_tag_solutionItems + str(index)
                    query += solutionItem.cypher_solutionItemTag_createNode(var) + "\n"
                    query += f'MERGE ({var_issue})-[{self.databaseInfoEdges["issue-solutionitem"]}]->({var})' + "\n"

        return query
    #
    # def cypher_mwo_tagdata(self, var_issue, var_tag_items, var_tag_problems, var_tag_solutions, var_tag_unknowns,
    #                        var_tag_others):
    #     query = 'MATCH' + self.issue.cypher_issue_all(var_issue) + "\n"
    #
    #     if self.tag_items is not None and len(self.tag_items) is not 0:
    #         for i in range(0, len(self.tag_items)):
    #             if self.tag_items[i]._get_keyword() is not None:
    #                 var_tag_items = f'{var_tag_items}{i}'
    #                 query += self.tag_items[i].cypher_item_create_node(var_tag_items) + "\n"
    #                 query += f'MERGE ({var_issue})-[{self.tag_items[i].label_link}]->({var_tag_items})' + "\n"
    #
    #     if self.tag_problems is not None and len(self.tag_problems) is not 0:
    #         for i in range(0, len(self.tag_problems)):
    #             if self.tag_problems[i]._get_keyword() is not None:
    #                 var_tag_problems = f'{var_tag_problems}{i}'
    #                 query += self.tag_problems[i].cypher_action_create_node(var_tag_problems) + "\n"
    #                 query += f'MERGE ({var_issue})-[{self.tag_problems[i].label_link}]->({var_tag_problems})' + "\n"
    #
    #     if self.tag_solutions is not None and len(self.tag_solutions) is not 0:
    #         for i in range(0, len(self.tag_solutions)):
    #             if self.tag_solutions[i]._get_keyword() is not None:
    #                 var_tag_solutions = f'{var_tag_solutions}{i}'
    #                 query += self.tag_solutions[i].cypher_action_create_node(var_tag_solutions) + "\n"
    #                 query += f'MERGE ({var_issue})-[{self.tag_solutions[i].label_link}]->({var_tag_solutions})' + "\n"
    #
    #     if self.tag_unknowns is not None and len(self.tag_unknowns) is not 0:
    #         for i in range(0, len(self.tag_unknowns)):
    #             if self.tag_unknowns[i]._get_keyword() is not None:
    #                 var_tag_unknowns = f'{var_tag_unknowns}{i}'
    #                 query += self.tag_unknowns[i].cypher_unknown_create_node(var_tag_unknowns) + "\n"
    #                 query += f'MERGE ({var_issue})-[{self.tag_unknowns[i].label_link}]->({var_tag_unknowns})' + "\n"
    #
    #     if self.tag_others is not None and len(self.tag_others) is not 0:
    #         for i in range(0, len(self.tag_others)):
    #             if self.tag_others[i]._get_keyword() is not None:
    #                 var_tag_others = f'{var_tag_others}{i}'
    #                 query += self.tag_others[i].cypher_tag_createNode(var_tag_others) + "\n"
    #                 query += f'MERGE ({var_issue})-[{self.tag_others[i].label_link}]->({var_tag_others})' + "\n"
    #
    #     return query
    #
    # @staticmethod
    # def get_dict_database_structure(database):
    #     dict = {'Tag': '(node:TAG)',
    #             'Problem': '(node:TAG:ACTION)-[rel:PROBLEM]-()',
    #             'Solution': '(node:TAG:ACTION)-[rel:SOLUTION]-()',
    #             'Item': '(node:TAG:ITEM)',
    #             'Human': '(node:HUMAN)',
    #             'Operator': '(node:HUMAN:OPERATOR)',
    #             'Technician': '(node:HUMAN:TECHNICIAN)',
    #             'Machine': '(node:MACHINE)',
    #             'Machine Type': '(node:MACHINE_TYPE)',
    #             'Issue': '(node:ISSUE)',
    #             }
    #     d = {}
    #     index = 0
    #     for key, value in dict.items():
    #         property = set()
    #
    #         query = f'MATCH {value} RETURN DISTINCT keys(node) as prop'
    #         results, done = database.runQuery(query)
    #
    #         for result in results.records():
    #             for r in result["prop"]:
    #                 property.add(r)
    #         if property :
    #             d[key] = property
    #         index += 1
    #
    #     return d
    # """
    # TRYING TO DO THAT DYNAMIC
    #
    # query = "MATCH (node)<-[relationship]-() RETURN DISTINCT labels(node) as node, type(relationship) as rel"
    # results, done = database.runQuery(query)
    #
    # index = 0
    #
    # df = pd.DataFrame(columns=['nodes','label', 'properties'])
    # for result in results.records():
    #     node_labels = result["node"]
    #     edge_labels = result["rel"]
    #
    #     query = f'MATCH (node:{":".join(node_labels)})<-[:{edge_labels}]-() RETURN DISTINCT keys(node) as prop'
    #     res, done = database.runQuery(query)
    #     for p in res.records():
    #         property = p["prop"]
    #
    #     serie = [node_labels,edge_labels,property]
    #
    #     df.loc[index]=serie
    #     index +=1
    #
    # query = "MATCH (node:ISSUE)-->() RETURN DISTINCT labels(node) as node, keys(node) as prop"
    # results, done = database.runQuery(query)
    #
    # property = set()
    # for result in results.records():
    #     node_labels = result["node"]
    #     for r in result["prop"]:
    #         property.add(r)
    #
    # df.loc[index] = [node_labels, None, list(property)]
    #
    # """
