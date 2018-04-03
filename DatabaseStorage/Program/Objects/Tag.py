import collections



class Tag:
    """
    its utility is to represent the TAG data from a Maintenance Work Order.
    TAG are extracted from a CSV files and store in a Neo4J database using the my methods by create CYPHER queries
    Often they define my using my keyword

    In the database a TAG can be a ProblemAction_PA, a ProblemItem_PI, a SolutionAction_SA or a SolutionItem_SI
        The ACTION/ITEM definition is store in my node
        The PROBLEM/SOLUTION is tore with the link between ISSUE and TAG

    In the future it might be a abstract class of the classes ITEM and ACTION.
    And also it might store more than a 1graqmme (single word) tag but a 2,3,4,... grammes


    PARAMETERS:
        keyword    --  String to define the keyword of the TAG

    METHODS:
        toCypher    --  Used to create a Cypher query to represent a new TAG
    """

    def __init__(self, keyword=None, synonyms=None, similarTo=None, databaseInfo=None):
        self.databaseInfoTag = databaseInfo['tag']
        #self.databaseInfoEdges = databaseInfo['edges']

        self._set_keyword(keyword)
        self._set_synonyms(synonyms)
        self._set_similarTo(similarTo)

    def _get_keyword(self):
        """
        :return: the keyword of the TAG
        """
        return self.keyword

    def _set_keyword(self, keyword):
        """
        set the keyword of a TAG
        :param keyword: a String for the keyword
        """
        if keyword is "" or keyword is None:
            self.keyword = None
        else:
            try:
                self.keyword = keyword.lower().lstrip()
            except AttributeError:
                self.keyword = [k.lower().lstrip() for k in keyword]

    def _get_synonyms(self):
        """
        :return: the keyword of the TAG
        """
        return self.synonyms

    def _set_synonyms(self, synonyms):
        """
        set the keyword of a TAG
        :param keyword: a String for the keyword
        """
        if synonyms is "" or synonyms is None:
            self.synonyms = None
        else:
            if not isinstance(synonyms, collections.Iterable) or isinstance(synonyms, str):
                synonyms = [synonyms]
            self.synonyms = [synonym.lower() for synonym in synonyms]

    def _get_similarTo(self):
        """
        :return: the keyword of the TAG
        """
        return self.similarTo

    def _set_similarTo(self, similarTo):
        """
        set the keyword of a TAG
        :param keyword: a String for the keyword
        """
        if similarTo is "" or similarTo is None:
            self.similarTo = None
        else:
            tmp = []
            if not isinstance(similarTo, collections.Iterable):
                similarTo = [similarTo]
            for st in similarTo:
                if isinstance(st, Tag):
                    tmp.append(st)
            self.similarTo = tmp


    def __str__(self):
        return f"OBJECT: {type(self)}\n\t" \
               f"Keyword: {self.keyword}\n\t" \
               f"Synonyms: {self.synonyms}\n\t" \
               f"similarTo: {self.similarTo}\n\t" \

    def cypher_tag_keyword(self, variable="tag"):
        if self.keyword is None:
            return ""
        return f'({variable} {self.databaseInfoTag["label"]["tag"]}' + \
               "{" + f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}"' + "})"

    def cypher_tag_all(self, variable="tag"):
        query = f'({variable} {self.databaseInfoTag["label"]["tag"]}'
        if self.keyword or self.synonyms is not None:
            query += "{"
            if self.keyword is not None:
                query += f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}",'
            if self.synonyms is not None:
                query += f'{self.databaseInfoTag["properties"]["synonyms"]}:' + '["' + '","'.join(self.synonyms) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_tag_createNode(self, variable="tag"):
        if self.keyword is None:
            return ""
        query = f'MERGE {self.cypher_tag_keyword(variable)}'
        if self.synonyms is not None:
            for synonym in self.synonyms:
                query += f'\nFOREACH(x in CASE WHEN "{synonym}" in {variable}.{self.databaseInfoTag["properties"]["synonyms"]} THEN [] ELSE [1] END |' \
                         f' SET {variable}.{self.databaseInfoTag["properties"]["synonyms"]} = coalesce({variable}.{self.databaseInfoTag["properties"]["synonyms"]},[]) + "{synonym}" )'
        return query

    # def cypher_kpi(self, variable="tag"):
    #
    #     if self.it_is is "problem":
    #         variable += "_problem"
    #     elif self.it_is is "solution":
    #         variable += "_solution"
    #
    #     match = f'MATCH (issue {NodeIssue.LABEL_ISSUE.value})-[{self.label_link}]->({variable} {self.label_tag})'
    #     where, res = self.cypher_where_properties(variable=variable)
    #
    #     return match, " OR ".join(where), res
    #
    # def cypher_where_properties(self, variable="tag"):
    #     where = []
    #     res = []
    #     if self.keyword is not None:
    #         for k in self.keyword:
    #             if k == "_":
    #                 res.append(f'{variable}.{self.property_keyword}')
    #             else:
    #                 where.append(f'{variable}.{self.property_keyword} = "{k}"')
    #     if self.synonyms is not None:
    #         for s in self.synonyms:
    #             if s == "_":
    #                 res.append(f'{variable}.{self.property_synonyms}')
    #             else:
    #                 where.append(f'"{s}" IN {variable}.{self.property_synonyms}')
    #     return where, res


class TagOneGram(Tag):
    def __init__(self, keyword=None, synonyms=None, similarTo=None, databaseInfo=None):
        super().__init__(keyword, synonyms, similarTo, databaseInfo)

    def __str__(self):
        return f"OBJECT: {type(self)}\n\t" \
               f"Keyword: {self.keyword}\n\t" \
               f"Synonyms: {self.synonyms}\n\t" \
               f"similarTo: {self.similarTo}\n\t" \

    def cypher_onGramTag_keyword(self, variable="onegram_tag"):
        if self.keyword is None:
            return ""
        return f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}' + \
               "{" + f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}"' + "})"

    def cypher_onGramTag_all(self, variable="onegram_tag"):
        query = f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}'
        if self.keyword or self.synonyms is not None:
            query += "{"
            if self.keyword is not None:
                query += f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}",'
            if self.synonyms is not None:
                query += f'{self.databaseInfoTag["properties"]["synonyms"]}:' + '["' + '","'.join(self.synonyms) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_onGramTag_createNode(self, variable="onegram_tag"):
        if self.cypher_tag_createNode(variable) == "":
            return ""
        query = self.cypher_tag_createNode(variable)
        query += f'\nSET {variable} {self.databaseInfoTag["label"]["onegram"]}'
        return query


class TagItem(TagOneGram):
    def __init__(self, keyword=None, synonyms=None, similarTo=None, children=None, databaseInfo=None):
        super().__init__(keyword, synonyms, similarTo, databaseInfo)
        self._set_children(children)

    def _get_children(self):
        """
        :return: the keyword of the TAG
        """
        return self.children

    def _set_children(self, children):
        """
        set the keyword of a TAG
        :param keyword: a String for the keyword
        """
        if children is "" or children is None:
            self.children = None
        else:
            tmp = []
            if not isinstance(children, collections.Iterable):
                children = [children]
            for child in children:
                if isinstance(child, TagItem):
                    tmp.append(child)
            self.children = tmp

    def __str__(self):
        return f"OBJECT: {type(self)}\n\t" \
               f"Keyword: {self.keyword}\n\t" \
               f"Synonyms: {self.synonyms}\n\t" \
               f"similarTo: {self.similarTo} " \
               f"children: {self.children}\n\t"

    def cypher_itemTag_keyword(self, variable="tag_item"):
        if self.keyword is None:
            return ""
        return f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}{self.databaseInfoTag["label"]["item"]}' + \
               "{" + f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}"' + "})"

    def cypher_itemTag_all(self, variable="tag_item"):
        query = f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}{self.databaseInfoTag["label"]["item"]}'
        if self.keyword or self.synonyms is not None:
            query += "{"
            if self.keyword is not None:
                query += f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}",'
            if self.synonyms is not None:
                query += f'{self.databaseInfoTag["properties"]["synonyms"]}:' + '["' + '","'.join(self.synonyms) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_itemTag_createNode(self, variable="tag_item"):
        if self.cypher_onGramTag_createNode(variable) == "":
            return ""

        query = self.cypher_onGramTag_createNode(variable)
        query += f'\nSET {variable} {self.databaseInfoTag["label"]["item"]}'
        return query

    #TODO the relationship between item nodes from parent to child
    # def cypher_itemTag_linkChildren(self, variable="tag_item"):
    #     if not self.children or self.cypher_itemTag_keyword() == "":
    #         return ""
#         query = f'MATCH {self.cypher_itemTag_keyword(variable)}\n'
#         for index, child in enumerate(self.children):
#             var = variable + str(index)
#             query += f'MATCH {child.cypher_itemTag_keyword(var)}\n'
#             query += f'MERGE ({variable})-[{self.databaseInfoEdges["item-item"]}]->({var})'
    #
    #     return query


    # def cypher_kpi(self, variable="tag_item"):
    #     if self.it_is is "problem":
    #         variable += "_problem"
    #     elif self.it_is is "solution":
    #         variable += "_solution"
    #
    #     match = f'MATCH (issue {NodeIssue.LABEL_ISSUE.value})-[{self.label_link}]->({variable} {self.label_tag} {self.label_item})'
    #     where, res = self.cypher_where_properties(variable=variable)
    #
    #     return match, " OR ".join(where), res
    #
    # def cypher_where_properties(self, variable="tag_item"):
    #     return super().cypher_where_properties(variable)



class TagProblem(TagOneGram):
    def __init__(self, keyword=None, synonyms=None, similarTo=None, databaseInfo=None):
        super().__init__(keyword, synonyms, similarTo, databaseInfo)

    def __str__(self):
        return f"OBJECT: {type(self)}\n\t" \
               f"Keyword: {self.keyword}\n\t" \
               f"Synonyms: {self.synonyms}\n\t" \
               f"similarTo: {self.similarTo} "

    def cypher_problemTag_keyword(self, variable="tag_problem"):
        if self.keyword is None:
            return ""
        return f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}{self.databaseInfoTag["label"]["problem"]}' + \
               "{" + f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}"' + "})"

    def cypher_problemTag_all(self, variable="tag_problem"):
        query = f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}{self.databaseInfoTag["label"]["problem"]}'
        if self.keyword or self.synonyms is not None:
            query += "{"
            if self.keyword is not None:
                query += f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}",'
            if self.synonyms is not None:
                query += f'{self.databaseInfoTag["properties"]["synonyms"]}:' + '["' + '","'.join(self.synonyms) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_problemTag_createNode(self, variable="tag_problem"):
        if self.cypher_onGramTag_createNode(variable) == "":
            return ""

        query = self.cypher_onGramTag_createNode(variable)
        query += f'\nSET {variable} {self.databaseInfoTag["label"]["problem"]}'
        return query

    # def cypher_kpi(self, variable="tag_action"):
    #     if self.it_is is "problem":
    #         variable += "_problem"
    #     elif self.it_is is "solution":
    #         variable += "_solution"
    #
    #     match = f'MATCH (issue {NodeIssue.LABEL_ISSUE.value})-[{self.label_link}]->({variable} {self.label_tag} {self.label_action})'
    #     where, res = self.cypher_where_properties(variable=variable)
    #
    #     return match, " OR ".join(where), res
    #
    # def cypher_where_properties(self, variable="tag_action"):
    #     return super().cypher_where_properties(variable)


class TagSolution(TagOneGram):
    def __init__(self, keyword=None, synonyms=None, similarTo=None, databaseInfo=None):
        super().__init__(keyword, synonyms, similarTo, databaseInfo)

    def __str__(self):
        return f"OBJECT: {type(self)}\n\t" \
               f"Keyword: {self.keyword}\n\t" \
               f"Synonyms: {self.synonyms}\n\t" \
               f"similarTo: {self.similarTo} "

    def cypher_solutionTag_keyword(self, variable="tag_solution"):
        if self.keyword is None:
            return ""
        return f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}{self.databaseInfoTag["label"]["solution"]}' + \
               "{" + f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}"' + "})"

    def cypher_solutionTag_all(self, variable="tag_solution"):
        query = f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}{self.databaseInfoTag["label"]["solution"]}'
        if self.keyword or self.synonyms is not None:
            query += "{"
            if self.keyword is not None:
                query += f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}",'
            if self.synonyms is not None:
                query += f'{self.databaseInfoTag["properties"]["synonyms"]}:' + '["' + '","'.join(self.synonyms) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_solutionTag_createNode(self, variable="tag_solution"):
        if self.cypher_onGramTag_createNode(variable) == "":
            return ""

        query = self.cypher_onGramTag_createNode(variable)
        query += f'\nSET {variable} {self.databaseInfoTag["label"]["solution"]}'
        return query

    # def cypher_kpi(self, variable="tag_action"):
    #     if self.it_is is "problem":
    #         variable += "_problem"
    #     elif self.it_is is "solution":
    #         variable += "_solution"
    #
    #     match = f'MATCH (issue {NodeIssue.LABEL_ISSUE.value})-[{self.label_link}]->({variable} {self.label_tag} {self.label_action})'
    #     where, res = self.cypher_where_properties(variable=variable)
    #
    #     return match, " OR ".join(where), res
    #
    # def cypher_where_properties(self, variable="tag_action"):
    #     return super().cypher_where_properties(variable)


class TagUnknown(TagOneGram):
    def __init__(self, keyword=None, synonyms=None, similarTo=None, databaseInfo=None):
        super().__init__(keyword, synonyms, similarTo, databaseInfo)

    def __str__(self):
        return f"OBJECT: {type(self)}\n\t" \
               f"Keyword: {self.keyword}\n\t" \
               f"Synonyms: {self.synonyms}\n\t" \
               f"similarTo: {self.similarTo} "

    def cypher_unknownTag_keyword(self, variable="tag_unknown"):
        if self.keyword is None:
            return ""
        return f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}{self.databaseInfoTag["label"]["unknown"]}' + \
               "{" + f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}"' + "})"

    def cypher_unknownTag_all(self, variable="tag_unknown"):
        query = f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["onegram"]}{self.databaseInfoTag["label"]["unknown"]}'
        if self.keyword or self.synonyms is not None:
            query += "{"
            if self.keyword is not None:
                query += f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}",'
            if self.synonyms is not None:
                query += f'{self.databaseInfoTag["properties"]["synonyms"]}:' + '["' + '","'.join(self.synonyms) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_unknownTag_createNode(self, variable="tag_unknown"):
        if self.cypher_onGramTag_createNode(variable) == "":
            return ""
        query = self.cypher_onGramTag_createNode(variable)
        query += f'\nSET {variable} {self.databaseInfoTag["label"]["unknown"]}'
        return query

    # def cypher_kpi(self, variable="tag_action"):
    #     if self.it_is is "problem":
    #         variable += "_problem"
    #     elif self.it_is is "solution":
    #         variable += "_solution"
    #
    #     match = f'MATCH (issue {NodeIssue.LABEL_ISSUE.value})-[{self.label_link}]->({variable} {self.label_tag} {self.label_action})'
    #     where, res = self.cypher_where_properties(variable=variable)
    #
    #     return match, " OR ".join(where), res
    #
    # def cypher_where_properties(self, variable="tag_action"):
    #     return super().cypher_where_properties(variable)


class TagNGram(Tag):
    def __init__(self, keyword=None, synonyms=None, similarTo=None, databaseInfo=None):
        super().__init__(keyword, synonyms, similarTo, databaseInfo)

        oneGrams = keyword.split(" ")
        self.composedOf_oneGrams = []
        for onGram in oneGrams:
            self.composedOf_oneGrams.append(TagOneGram(keyword=onGram, databaseInfo=databaseInfo))


    def __str__(self):
        return f"OBJECT: {type(self)}\n\t" \
               f"Keyword: {self.keyword}\n\t" \
               f"Synonyms: {self.synonyms}\n\t" \
               f"similarTo: {self.similarTo}\n\t" \

    def cypher_nGramTag_keyword(self, variable="ngram_tag"):
        if self.keyword is None:
            return ""
        return f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["ngram"]}' + \
               "{" + f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}"' + "})"

    def cypher_nGramTag_all(self, variable="ngram_tag"):
        query = f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["ngram"]}'
        if self.keyword or self.synonyms is not None:
            query += "{"
            if self.keyword is not None:
                query += f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}",'
            if self.synonyms is not None:
                query += f'{self.databaseInfoTag["properties"]["synonyms"]}:' + '["' + '","'.join(self.synonyms) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_nGramTag_createNode(self, variable="ngram_tag"):
        if self.cypher_tag_createNode(variable) == "":
            return ""
        query = self.cypher_tag_createNode(variable)
        query += f'\nSET {variable} {self.databaseInfoTag["label"]["ngram"]}'
        return query

    # def cypher_nGram_linkPartOf(self, variable="ngram_tag"):
    #     if not self.composedOf_oneGrams or self.cypher_nGramTag_keyword(variable) == "":
    #         return ""
    #
    #     query = f'MATCH {self.cypher_nGramTag_keyword(variable)}'
    #     for index, oneGram in enumerate(self.composedOf_oneGrams):
    #         var = variable + str(index)
    #         query += f'MATCH {oneGram.cypher_onGramTag_keyword(var)}'
    #         query += f'MERGE ({variable})-[{self.databaseInfoEdges["ngram-onegram"]}]->({var})'


class TagProblemItem(TagNGram):
    def __init__(self, keyword=None, synonyms=None, similarTo=None, databaseInfo=None):
        super().__init__(keyword, synonyms, similarTo, databaseInfo)

    def __str__(self):
        return f"OBJECT: {type(self)}\n\t" \
               f"Keyword: {self.keyword}\n\t" \
               f"Synonyms: {self.synonyms}\n\t" \
               f"similarTo: {self.similarTo}\n\t" \

    def cypher_problemItemTag_keyword(self, variable="problemitem_tag"):
        if self.keyword is None:
            return ""
        return f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["ngram"]}{self.databaseInfoTag["label"]["problem_item"]}' + \
               "{" + f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}"' + "})"

    def cypher_problemItemTag_all(self, variable="problemitem_tag"):
        query = f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["ngram"]}{self.databaseInfoTag["label"]["problem_item"]}'
        if self.keyword or self.synonyms is not None:
            query += "{"
            if self.keyword is not None:
                query += f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}",'
            if self.synonyms is not None:
                query += f'{self.databaseInfoTag["properties"]["synonyms"]}:' + '["' + '","'.join(self.synonyms) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_problemItemTag_createNode(self, variable="problemitem_tag"):
        if self.cypher_tag_createNode(variable) == "":
            return ""
        query = self.cypher_nGramTag_createNode(variable)
        query += f'\nSET {variable} {self.databaseInfoTag["label"]["problem_item"]}'
        return query


class TagSolutionItem(TagNGram):
    def __init__(self, keyword=None, synonyms=None, similarTo=None, databaseInfo=None):
        super().__init__(keyword, synonyms, similarTo, databaseInfo)

    def __str__(self):
        return f"OBJECT: {type(self)}\n\t" \
               f"Keyword: {self.keyword}\n\t" \
               f"Synonyms: {self.synonyms}\n\t" \
               f"similarTo: {self.similarTo}\n\t" \

    def cypher_solutionItemTag_keyword(self, variable="solutionitem_tag"):
        if self.keyword is None:
            return ""
        return f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["ngram"]}{self.databaseInfoTag["label"]["solution_item"]}' + \
               "{" + f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}"' + "})"

    def cypher_solutionItemTag_all(self, variable="solutionitem_tag"):
        query = f'({variable} {self.databaseInfoTag["label"]["tag"]}{self.databaseInfoTag["label"]["ngram"]}{self.databaseInfoTag["label"]["solution_item"]}'
        if self.keyword or self.synonyms is not None:
            query += "{"
            if self.keyword is not None:
                query += f'{self.databaseInfoTag["properties"]["keyword"]}:"{self.keyword}",'
            if self.synonyms is not None:
                query += f'{self.databaseInfoTag["properties"]["synonyms"]}:' + '["' + '","'.join(self.synonyms) + '"],'
            query = query[:-1] + "}"
        return query + ")"

    def cypher_solutionItemTag_createNode(self, variable="solutionitem_tag"):
        if self.cypher_tag_createNode(variable) == "":
            return ""
        query = self.cypher_nGramTag_createNode(variable)
        query += f'\nSET {variable} {self.databaseInfoTag["label"]["solution_item"]}'
        return query




    # def cypher_kpi(self, variable="tag_action_item"):
    #
    #     if self.it_is is "problem":
    #         variable += "_problem"
    #     elif self.it_is is "solution":
    #         variable += "_solution"
    #
    #     match = f'MATCH (issue {NodeIssue.LABEL_ISSUE.value})-[{self.label_link}]->({variable} {self.label_tag} {self.label_action_item})'
    #     where, res = self.cypher_where_properties(variable=variable)
    #
    #     return match, " OR ".join(where), res
    #
    # def cypher_where_properties(self, variable="tag_action_item"):
    #     return super().cypher_where_properties(variable)
