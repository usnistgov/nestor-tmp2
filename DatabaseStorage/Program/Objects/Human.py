import collections


class Human:
    """

    Its utility is to represent the HUMAN data from a Maintenance Work Order.
    HUMAN are extracted from a CSV files and store in a Neo4J database using the my methods by create CYPHER queries
    Often defined using my name (it needs a name)

    In the database it can be a OPERATOR or a TECHNICIAN,
        If it is an OPERATOR, it only have a a parameter name and it is link to the node ISSUE with an edges REQUESTED_BY
        If it is a TECHNICIAN, it have the parameter name, skills and crafts and it is link to the node ISSUE with an edges SOLVE_BY


    In the future it might be a abstract class of the classes TECHNICIAN and OPERATOR.

    PARAMETERS:
        name    --  String to define the name of the HUMAN
        skills  --  Array of string to define all skills of this HUMAN based on the KPI he solved (only for TECHNICIAN)
        crafts  --  Array of string to define all crafts of this HUMAN based on the KPI he solved (only for TECHNICIAN)


    METHODS:
        toCypher        --  DEPRECIATE (use toCypherName and toCypherUpdate instead) Used to represent a Cypher query to Create a new HUMAN
        toCypherName    --  Used to represent a CYPHER query to represent a HUMAN in the database using the name
        toCypherUpdate  --  Used to update the information of the node HUMAN in the database
                            If in the database a HUMAN already have my name, It updated it and add skills and crafts
    """

    def __init__(self, name=None,  databaseInfo=None):
        self.databaseInfoHuman = databaseInfo['human']
        #self.databaseInfoEdges = databaseInfo['edges']

        self._set_name(name)

    def _get_name(self):
        """
        :return: the name of the HUMAN
        """
        return self.name

    def _set_name(self, name):
        """
        Set the name of the HUMAN
        if the name is empty "" it became "unknown"

        :param name: a String
        """
        if name is "" or name is None:
            self.name = None
        else:
            try:
                self.name = name.lower().lstrip()
            except AttributeError:
                self.name = [n.lower().lstrip() for n in name]

    def __str__(self):
        return f"{type(self)}\n\t" \
               f"Name: {self.name}"

    def cypher_human_name(self, variable="human"):
        if self.name is None:
            return ""
        return f'({variable} {self.databaseInfoHuman["label"]["human"]}' + \
               "{" + f'{self.databaseInfoHuman["properties"]["name"]}:"{self.name}"' + "})"

    def cypher_human_all(self, variable="human"):
        query = f'({variable} {self.databaseInfoHuman["label"]["human"]}'
        if self.name is not None:
            query += "{" + f'{self.databaseInfoHuman["properties"]["name"]}:"{self.name}"' + "}"
        query += ")"

        return query

    def cypher_human_createNode(self, variable="human"):
        if self.name is None:
            return ""
        query = f'MERGE {self.cypher_human_name(variable)}'
        return query

    # def cypher_kpi(self, variable="human"):
    #     match = f'MATCH (issue {NodeIssue.LABEL_ISSUE.value})-->({variable} {self.label_human})'
    #     where, res = self.cypher_where_properties(variable=variable)
    #
    #     return match, " OR ".join(where), res
    #
    # def cypher_where_properties(self, variable="human"):
    #     where = []
    #     res = []
    #     if self.name is not None:
    #         for n in self.name:
    #             if n == "_":
    #                 res.append(f'{variable}.{self.property_name}')
    #             else:
    #                 where.append(f'{variable}.{self.property_name} = "{n}"')
    #
    #     return where, res


class Operator(Human):
    """

    Its utility is to represent the HUMAN data from a Maintenance Work Order.
    HUMAN are extracted from a CSV files and store in a Neo4J database using the my methods by create CYPHER queries
    Often defined using my name (it needs a name)

    In the database it can be a OPERATOR or a TECHNICIAN,
        If it is an OPERATOR, it only have a a parameter name and it is link to the node ISSUE with an edges REQUESTED_BY
        If it is a TECHNICIAN, it have the parameter name, skills and crafts and it is link to the node ISSUE with an edges SOLVE_BY


    In the future it might be a abstract class of the classes TECHNICIAN and OPERATOR.

    PARAMETERS:
        name    --  String to define the name of the HUMAN
        skills  --  Array of string to define all skills of this HUMAN based on the KPI he solved (only for TECHNICIAN)
        crafts  --  Array of string to define all crafts of this HUMAN based on the KPI he solved (only for TECHNICIAN)


    METHODS:
        toCypher        --  DEPRECIATE (use toCypherName and toCypherUpdate instead) Used to represent a Cypher query to Create a new HUMAN
        toCypherName    --  Used to represent a CYPHER query to represent a HUMAN in the database using the name
        toCypherUpdate  --  Used to update the information of the node HUMAN in the database
                            If in the database a HUMAN already have my name, It updated it and add skills and crafts
    """

    def __init__(self, name=None, databaseInfo=None):
        super().__init__(name, databaseInfo=databaseInfo)

    def __str__(self):
        return f"{type(self)}\n\t" \
               f"Name: {self.name}"

    def cypher_operator_name(self, variable="operator"):
        if self.name is None:
            return ""
        return f'({variable} {self.databaseInfoHuman["label"]["human"]}{self.databaseInfoHuman["label"]["operator"]}' + \
               "{" + f'{self.databaseInfoHuman["properties"]["name"]}:"{self.name}"' + "})"

    def cypher_operator_all(self, variable="operator"):
        query = f'({variable} {self.databaseInfoHuman["label"]["human"]}{self.databaseInfoHuman["label"]["operator"]}'
        if self.name is not None:
            query += "{" + f'{self.databaseInfoHuman["properties"]["name"]}:"{self.name}"' + "}"
        query += ")"

        return query

    def cypher_operator_createNode(self, variable="operator"):
        query = self.cypher_human_createNode(variable)
        query += f'\nSET {variable} {self.databaseInfoHuman["label"]["operator"]}'

        return query

    # def cypher_kpi(self, variable="operator"):
    #     match = f'MATCH (issue {NodeIssue.LABEL_ISSUE.value})-[{self.label_link}]->({variable} {self.label_human}{self.label_operator})'
    #     where, res = self.cypher_where_properties(variable=variable)
    #
    #     return match, " OR ".join(where), res
    #
    # def cypher_where_properties(self, variable="operator"):
    #     return super().cypher_where_properties(variable)


class Technician(Human):
    """

    Its utility is to represent the HUMAN data from a Maintenance Work Order.
    HUMAN are extracted from a CSV files and store in a Neo4J database using the my methods by create CYPHER queries
    Often defined using my name (it needs a name)

    In the database it can be a OPERATOR or a TECHNICIAN,
        If it is an OPERATOR, it only have a a parameter name and it is link to the node ISSUE with an edges REQUESTED_BY
        If it is a TECHNICIAN, it have the parameter name, skills and crafts and it is link to the node ISSUE with an edges SOLVE_BY


    In the future it might be a abstract class of the classes TECHNICIAN and OPERATOR.

    PARAMETERS:
        name    --  String to define the name of the HUMAN
        skills  --  Array of string to define all skills of this HUMAN based on the KPI he solved (only for TECHNICIAN)
        crafts  --  Array of string to define all crafts of this HUMAN based on the KPI he solved (only for TECHNICIAN)


    METHODS:
        toCypher        --  DEPRECIATE (use toCypherName and toCypherUpdate instead) Used to represent a Cypher query to Create a new HUMAN
        toCypherName    --  Used to represent a CYPHER query to represent a HUMAN in the database using the name
        toCypherUpdate  --  Used to update the information of the node HUMAN in the database
                            If in the database a HUMAN already have my name, It updated it and add skills and crafts
    """

    def __init__(self, name=None, skills=None, crafts=None, databaseInfo=None):

        super().__init__(name, databaseInfo=databaseInfo)
        self._set_skills(skills)
        self._set_crafts(crafts)

    def _get_skills(self):
        """
        :return: the skills of the HUMAN
        """
        return self.skills

    def _set_skills(self, skills):
        """
        Set the skills of the HUMAN
        The skills is store in an array

        :param skills: an Array of String or a String
        """
        if skills is "" or skills is None or len(skills) == 0:
            self.skills = None
        else:
            if not isinstance(skills, collections.Iterable) or isinstance(skills, str):
                skills = [skills]
            self.skills = [skill.lower() for skill in skills]

    def _get_crafts(self):
        """
        :return: the crafts of the Human
        """
        return self.crafts

    def _set_crafts(self, crafts):
        """
        Set the crafts of the HUMAN
        The crafts is store in an array

        :param crafts: an Array of String or a String
        """
        if crafts is "" or crafts is None or len(crafts) == 0:
            self.crafts = None
        else:
            if not isinstance(crafts, collections.Iterable):
                crafts = [crafts]
            self.crafts = [craft.lower() for craft in crafts]

    def __str__(self):
        return f"{type(self)}\n\t" \
               f"Name: {self.name}\n\t" \
               f"Skills: {self.skills}\n\t" \
               f"Crafts: {self.crafts}"

    def cypher_technician_name(self, variable="technician"):
        if self.name is None:
            return ""
        return f'({variable} {self.databaseInfoHuman["label"]["human"]}{self.databaseInfoHuman["label"]["technician"]}' + \
               "{" + f'{self.databaseInfoHuman["properties"]["name"]}:"{self.name}"' + "})"

    def cypher_technician_all(self, variable="technician"):
        query = f'({variable} {self.databaseInfoHuman["label"]["human"]}{self.databaseInfoHuman["label"]["technician"]}'
        if self.name or self.skills or self.crafts is not None:
            query += "{"
            if self.name is not None:
                query += f'{self.databaseInfoHuman["properties"]["name"]}:"{self.name}",'
            if self.skills is not None:
                query += f'{self.databaseInfoHuman["properties"]["skills"]}:' + '["' + '","'.join(self.skills) + '"],'
            if self.crafts is not None:
                query += f'{self.databaseInfoHuman["properties"]["crafts"]}:' + '["' + '","'.join(self.crafts) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_technician_createNode(self, variable="technician"):
        query = self.cypher_human_createNode(variable)
        if self.skills is not None:
            for skill in self.skills:
                query += f'\nFOREACH(x in CASE WHEN "{skill}" in {variable}.{self.databaseInfoHuman["properties"]["skills"]} THEN [] ELSE [1] END |' \
                         f'  SET {variable}.{self.databaseInfoHuman["properties"]["skills"]} = coalesce({variable}.{self.databaseInfoHuman["properties"]["skills"]},[]) + "{skill}" )'
        if self.crafts is not None:
            for craft in self.crafts:
                query += f'\nFOREACH(x in CASE WHEN "{craft}" in {variable}.{self.databaseInfoHuman["properties"]["crafts"]} THEN [] ELSE [1] END |' \
                         f'  SET {variable}.{self.databaseInfoHuman["properties"]["crafts"]} = coalesce({variable}.{self.databaseInfoHuman["properties"]["crafts"]},[]) + "{craft}" )'
        query += f'\nSET {variable} {self.databaseInfoHuman["label"]["technician"]}'
        return query

    # def cypher_kpi(self, variable="technician"):
    #     match = f'MATCH (issue {NodeIssue.LABEL_ISSUE.value})-[{self.label_link}]->({variable} {self.label_human}{self.label_technician})'
    #     where, res = self.cypher_where_properties(variable=variable)
    #
    #     return match, " OR ".join(where), res
    #
    # def cypher_where_properties(self, variable="technician"):
    #     where, res = super().cypher_where_properties(variable)
    #
    #     if self.skills is not None:
    #         for s in self.skills:
    #             if s == "_":
    #                 res.append(f'{variable}.{self.property_skills}')
    #             else:
    #                 where.append(f'"{s}" IN {variable}.{self.property_skills}')
    #
    #     if self.crafts is not None:
    #         for c in self.crafts:
    #             if c == "_":
    #                 res.append(f'{variable}.{self.property_crafts}')
    #             else:
    #                 where.append(f'"{c}" IN {variable}.{self.property_crafts}')
    #
    #     return where, res
