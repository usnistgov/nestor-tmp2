from DatabaseStorage.Program.Objects.Human import *
from DatabaseStorage.Program.Objects.Issue import *
from DatabaseStorage.Program.Objects.Machine import *
from DatabaseStorage.Program.Objects.MaintenanceWorkOrder import *
from DatabaseStorage.Program.Objects.Tag import *
from DatabaseStorage.Program.Others.MyDate import clean_GS_date
from tqdm import tqdm
import os
import pandas as pd



"""
This files contains all the function to extract the MWOs from a CSV format to store it in a Neo4J Database

The localisation is a dictionary which describe the CSV file (what column contains what information):
 localization = {NodeHuman.VALUE_TECHNICIAN.value: ,
                    NodeHuman.VALUE_OPERATOR.value: ,
                    NodeHuman.VALUE_CRAFTS.value:,
                    NodeHuman.VALUE_SKILLS.value:,

                    NodeTag.VALUE_ITEM.value: ,
                    NodeTag.VALUE_PROBLEM.value: ,
                    NodeTag.VALUE_SOLUTION.value: ,

                    NodeMachine.VALUE_MACHINE.value: ,
                    NodeMachine.VALUE_TYPE.value:,
                    NodeMachine.VALUE_MANUFACTURER.value:,
                    NodeMachine.VALUE_LOCASION.value:,

                    NodeIssue.VALUE_DESCRIPTION_PROBLEM.value: ,
                    NodeIssue.VALUE_DESCRIPTION_SOLUTION.value: ,
                    NodeIssue.VALUE_DESCRIPTION_CAUSE.value:,
                    NodeIssue.VALUE_DESCRIPTION_EFFECT.value:,
                    NodeIssue.VALUE_PART_PROCESS.value: ,
                    NodeIssue.PROPERTY_NECESSARY_PART.value: ,
                    NodeIssue.VALUE_DATE_MACHINE_DOWN.value:,
                    NodeIssue.VALUE_DATE_MACHINE_UP.value:,
                    NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_ISSUE.value:,
                    NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_CLOSE.value:,
                    NodeIssue.VALUE_DATE_TECHNICIAN_ARRIVE.value:,
                    NodeIssue.VALUE_DATE_PROBLEM_FOUND.value:,
                    NodeIssue.VALUE_DATE_PROBLEM_SOLVE.value:,
                    NodeIssue.VALUE_DATE_PART_ORDER.value:,
                    NodeIssue.VALUE_DATE_MAINTENANCE_TECHNICIAN_REPAIR_PROBLEM.value:,

                    }
"""

#
# def graph_database_from_csv(database, file_path, localization, date_cleanizer=None):
#     """
#
#     :param database: the Neo4j database in which you want to store the data
#     :param file_path: the path of your CSV file
#     :param localization: a dictionary with the description of your csv file (where is which record) :
#             localization = {NodeHuman.VALUE_TECHNICIAN.value: ,
#                     NodeHuman.VALUE_OPERATOR.value: ,
#                     NodeHuman.VALUE_CRAFTS.value:,
#                     NodeHuman.VALUE_SKILLS.value:,
#
#                     NodeTag.VALUE_ITEM.value: ,
#                     NodeTag.VALUE_PROBLEM.value: ,
#                     NodeTag.VALUE_SOLUTION.value: ,
#
#                     NodeMachine.VALUE_MACHINE.value: ,
#                     NodeMachine.VALUE_TYPE.value:,
#                     NodeMachine.VALUE_MANUFACTURER.value:,
#                     NodeMachine.VALUE_LOCASION.value:,
#
#                     NodeIssue.VALUE_DESCRIPTION_PROBLEM.value: ,
#                     NodeIssue.VALUE_DESCRIPTION_SOLUTION.value: ,
#                     NodeIssue.VALUE_DESCRIPTION_CAUSE.value:,
#                     NodeIssue.VALUE_DESCRIPTION_EFFECT.value:,
#                     NodeIssue.VALUE_PART_PROCESS.value: ,
#                     NodeIssue.PROPERTY_NECESSARY_PART.value: ,
#                     NodeIssue.VALUE_DATE_MACHINE_DOWN.value:,
#                     NodeIssue.VALUE_DATE_MACHINE_UP.value:,
#                     NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_ISSUE.value:,
#                     NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_CLOSE.value:,
#                     NodeIssue.VALUE_DATE_TECHNICIAN_ARRIVE.value:,
#                     NodeIssue.VALUE_DATE_PROBLEM_FOUND.value:,
#                     NodeIssue.VALUE_DATE_PROBLEM_SOLVE.value:,
#                     NodeIssue.VALUE_DATE_PART_ORDER.value:,
#                     NodeIssue.VALUE_DATE_MAINTENANCE_TECHNICIAN_REPAIR_PROBLEM.value:,
#
#                     }
#     :return:
#     """
#
#     def create_MWO(row, localization, date_cleanizer=None):
#
#         #####   TECHNICIAN #####
#         def create_technicians(row, localization):
#             skills = []
#             try:
#                 for skill in row[localization[NodeHuman.VALUE_SKILLS.value]].split('/'):
#                     skills.append(skill)
#             except KeyError:
#                 pass
#
#             crafts = []
#             try:
#                 for craft in row[localization[NodeHuman.VALUE_CRAFTS.value]].split('/'):
#                     crafts.append(craft)
#             except KeyError:
#                 pass
#
#             technicians = []
#             try:
#                 for technician in row[localization[NodeHuman.VALUE_TECHNICIAN.value]].split('/'):
#                     technicians.append(Technician(name=technician, skills=skills, crafts=crafts))
#             except KeyError:
#                 pass
#
#             return technicians
#
#         #####   OPERATOR #####
#         def create_operators(row, localization):
#             operators = []
#             try:
#                 for operator in row[localization[NodeHuman.VALUE_OPERATOR.value]].split('/'):
#                     operators.append(Operator(name=operator))
#             except KeyError:
#                 pass
#
#             return operators
#
#         #####   MACHINE #####
#         def create_machine(row, localization):
#             machine = None
#
#             try:
#                 machine = Machine(name=row[localization[NodeMachine.VALUE_MACHINE.value]])
#
#                 try:
#                     machine._set_manufacturer(row[localization[NodeMachine.VALUE_MANUFACTURER.value]])
#                 except KeyError:
#                     pass
#
#                 try:
#                     machine._set_machine_type(row[localization[NodeMachine.VALUE_TYPE.value]])
#                 except KeyError:
#                     pass
#
#                 try:
#                     machine._set_locasion(row[localization[NodeMachine.VALUE_LOCASION.value]])
#                 except KeyError:
#                     pass
#
#             except KeyError:
#                 pass
#
#             return machine
#
#         #####   TAG #####
#         def create_items(row, localization):
#             items = []
#
#             try:
#                 for item in row[localization[NodeTag.VALUE_ITEM.value]].split('/ '):
#                     items.append(TagItem(keyword=item))
#             except KeyError:
#                 pass
#
#             return items
#
#         def create_problems(row, localization):
#             problems = []
#
#             try:
#                 for problem in row[localization[NodeTag.VALUE_PROBLEM.value]].split('/ '):
#                     problems.append(TagAction(keyword=problem, it_is="p"))
#             except KeyError:
#                 pass
#
#             return problems
#
#         def create_solutions(row, localization):
#             solutions = []
#
#             try:
#                 for solution in row[localization[NodeTag.VALUE_SOLUTION.value]].split('/ '):
#                     solutions.append(TagAction(keyword=solution, it_is="s"))
#             except KeyError:
#                 pass
#
#             return solutions
#
#         def create_unknown(row, localization):
#             unknowns = []
#
#             try:
#                 for unknown in row[localization[NodeTag.VALUE_UNKNOWN.value]].split('/ '):
#                     unknowns.append(TagUnknown(keyword=unknown))
#             except KeyError:
#                 pass
#             return unknowns
#
#         def create_other(row, localization):
#             others = []
#
#             try:
#                 for other in row[localization[NodeTag.VALUE_NA.value]].split('/ '):
#                     others.append(Tag(keyword=other))
#             except KeyError:
#                 pass
#
#             try:
#                 for other in row[localization[NodeTag.VALUE_STOP_WORDS.value]].split('/ '):
#                     others.append(Tag(keyword=other))
#             except KeyError:
#                 pass
#
#             return others
#
#         #####   ISSUE #####
#         def create_issue(row, localization, date_cleanizer=None):
#             issue = None
#
#             try:
#                 issue = Issue(problem=row[localization[NodeIssue.VALUE_DESCRIPTION_PROBLEM.value]],
#                               solution=row[localization[NodeIssue.VALUE_DESCRIPTION_SOLUTION.value]])
#                 try:
#                     issue._set_cause(row[localization[NodeIssue.VALUE_DESCRIPTION_CAUSE.value]])
#                 except KeyError:
#                     pass
#                 try:
#                     issue._set_effects(row[localization[NodeIssue.VALUE_DESCRIPTION_EFFECT.value]])
#                 except KeyError:
#                     pass
#                 try:
#                     issue._set_part_in_process(row[localization[NodeIssue.VALUE_PART_PROCESS.value]])
#                 except KeyError:
#                     pass
#                 try:
#                     issue._set_necessary_part(row[localization[NodeIssue.VALUE_NECESSARY_PART.value]])
#                 except KeyError:
#                     pass
#                 try:
#                     issue._set_machine_down(row[localization[NodeIssue.VALUE_MACHINE_DOWN.value]])
#                 except KeyError:
#                     pass
#                 try:
#                     if NodeIssue.VALUE_DATE_MACHINE_DOWN.value + "2" in localization \
#                             and row[localization[NodeIssue.VALUE_DATE_MACHINE_DOWN.value + "2"]] is not "":
#                         issue._set_date_machine_down(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MACHINE_DOWN.value]],
#                                 row[localization[NodeIssue.VALUE_DATE_MACHINE_DOWN.value + "2"]]
#                             )
#                         )
#                     elif NodeIssue.VALUE_DATE_MACHINE_DOWN.value in localization.keys():
#                         issue._set_date_machine_down(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MACHINE_DOWN.value]]
#                             )
#                         )
#                 except (KeyError, AttributeError):
#                     pass
#                 try:
#                     if NodeIssue.VALUE_DATE_MACHINE_UP.value + "2" in localization \
#                             and row[localization[NodeIssue.VALUE_DATE_MACHINE_UP.value + "2"]] is not "":
#                         issue._set_date_machine_up(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MACHINE_UP.value]],
#                                 row[localization[NodeIssue.VALUE_DATE_MACHINE_UP.value + "2"]]
#                             )
#                         )
#                     elif NodeIssue.VALUE_DATE_MACHINE_UP.value in localization.keys():
#                         issue._set_date_machine_up(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MACHINE_UP.value]]
#                             )
#                         )
#                 except (KeyError, AttributeError):
#                     pass
#                 try:
#                     if NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_ISSUE.value + "2" in localization \
#                             and row[
#                                 localization[NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_ISSUE.value + "2"]] is not "":
#                         issue._set_date_maintenance_work_order_issue(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_ISSUE.value]],
#                                 row[localization[NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_ISSUE.value + "2"]])
#                         )
#                     elif NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_ISSUE.value in localization.keys():
#                         issue._set_date_maintenance_work_order_issue(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_ISSUE.value]])
#                         )
#                 except (KeyError, AttributeError):
#                     pass
#                 try:
#                     if NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_CLOSE.value + "2" in localization \
#                             and row[
#                                 localization[NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_CLOSE.value + "2"]] is not "":
#                         issue._set_date_maintenance_work_order_close(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_CLOSE.value]],
#                                 row[localization[NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_CLOSE.value + "2"]])
#                         )
#                     elif NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_CLOSE.value in localization.keys():
#                         issue._set_date_maintenance_work_order_close(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MAINTENANCE_WORK_ORDER_CLOSE.value]])
#                         )
#                 except (KeyError, AttributeError):
#                     pass
#                 try:
#                     if NodeIssue.VALUE_DATE_TECHNICIAN_ARRIVE.value + "2" in localization \
#                             and row[localization[NodeIssue.VALUE_DATE_TECHNICIAN_ARRIVE.value + "2"]] is not "":
#                         issue._set_date_maintenance_technician_arrives(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_TECHNICIAN_ARRIVE.value]],
#                                 row[localization[NodeIssue.VALUE_DATE_TECHNICIAN_ARRIVE.value + "2"]])
#                         )
#                     elif NodeIssue.VALUE_DATE_TECHNICIAN_ARRIVE.value in localization.keys():
#                         issue._set_date_maintenance_technician_arrives(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_TECHNICIAN_ARRIVE.value]])
#                         )
#                 except (KeyError, AttributeError):
#                     pass
#                 try:
#                     if NodeIssue.VALUE_DATE_PROBLEM_FOUND.value + "2" in localization \
#                             and row[localization[NodeIssue.VALUE_DATE_PROBLEM_FOUND.value + "2"]] is not "":
#                         issue._set_date_problem_found(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_PROBLEM_FOUND.value]],
#                                 row[localization[NodeIssue.VALUE_DATE_PROBLEM_FOUND.value + "2"]])
#                         )
#                     elif NodeIssue.VALUE_DATE_PROBLEM_FOUND.value in localization.keys():
#                         issue._set_date_problem_found(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_PROBLEM_FOUND.value]])
#                         )
#                 except (KeyError, AttributeError):
#                     pass
#                 try:
#                     if NodeIssue.VALUE_DATE_PROBLEM_SOLVE.value + "2" in localization \
#                             and row[localization[NodeIssue.VALUE_DATE_PROBLEM_SOLVE.value + "2"]] is not "":
#                         issue._set_date_problem_solved(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_PROBLEM_SOLVE.value]],
#                                 row[localization[NodeIssue.VALUE_DATE_PROBLEM_SOLVE.value + "2"]])
#                         )
#                     elif NodeIssue.VALUE_DATE_PROBLEM_SOLVE.value in localization.keys():
#                         issue._set_date_problem_solved(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_PROBLEM_SOLVE.value]])
#                         )
#                 except (KeyError, AttributeError):
#                     pass
#                 try:
#                     if NodeIssue.VALUE_DATE_PART_ORDER.value + "2" in localization \
#                             and row[localization[NodeIssue.VALUE_DATE_PART_ORDER.value + "2"]] is not "":
#                         issue._set_date_part_ordered(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_PART_ORDER.value]],
#                                 row[localization[NodeIssue.VALUE_DATE_PART_ORDER.value + "2"]])
#                         )
#                     elif NodeIssue.VALUE_DATE_PART_ORDER.value in localization.keys():
#                         issue._set_date_part_ordered(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_PART_ORDER.value]])
#                         )
#                 except (KeyError, AttributeError):
#                     pass
#                 try:
#                     if NodeIssue.VALUE_DATE_MAINTENANCE_TECHNICIAN_REPAIR_PROBLEM.value + "2" in localization \
#                             and row[localization[
#                                         NodeIssue.VALUE_DATE_MAINTENANCE_TECHNICIAN_REPAIR_PROBLEM.value + "2"]] is not "":
#                         issue._set_date_maintenance_technician_begin_repair_problem(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MAINTENANCE_TECHNICIAN_REPAIR_PROBLEM.value]],
#                                 row[localization[
#                                     NodeIssue.VALUE_DATE_MAINTENANCE_TECHNICIAN_REPAIR_PROBLEM.value + "2"]])
#                         )
#                     elif NodeIssue.VALUE_DATE_MAINTENANCE_TECHNICIAN_REPAIR_PROBLEM.value in localization.keys():
#                         issue._set_date_maintenance_technician_begin_repair_problem(
#                             date_cleanizer(
#                                 row[localization[NodeIssue.VALUE_DATE_MAINTENANCE_TECHNICIAN_REPAIR_PROBLEM.value]])
#                         )
#                 except (KeyError, AttributeError):
#                     pass
#             except KeyError:
#                 pass
#             return issue
#
#         #####   CORE  #####
#         issue = create_issue(row, localization, date_cleanizer)
#         technicians = create_technicians(row, localization)
#         operators = create_operators(row, localization)
#         machine = create_machine(row, localization)
#         items = create_items(row, localization)
#         problems = create_problems(row, localization)
#         solutions = create_solutions(row, localization)
#         unknowns = create_unknown(row, localization)
#         others = create_other(row, localization)
#
#         return MaintenanceWorkOrder(issue=issue,
#                                     machine=machine,
#                                     operators=operators,
#                                     technicians=technicians,
#                                     tag_items=items,
#                                     tag_problems=problems,
#                                     tag_solutions=solutions,
#                                     tag_unknowns=unknowns,
#                                     tag_others=others
#                                     )
#
#     with open(file_path, encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         csvfile.seek(0)
#         # Only used for the tqdm
#         num_lines = 0
#         for line in csvfile:  # get the number total of row in the csv
#             num_lines += 1
#         csvfile.seek(0)  # reset the reader at the first line
#
#         count = 0
#         for row in tqdm(reader, total=num_lines):
#             # for row in reader:
#             mwo = create_MWO(row, localization, date_cleanizer)
#             query = mwo.cypher_mwo_graphdata()
#             query += "RETURN 1"
#             result, c = database.runQuery(query=query)
#             count += c
#         print(count, "Maintenance Word Order Created")


charsplit = ','
def graphDatabase_from_TaggedCSV(database, dataframe, propertyToHeader_dict, databaseSchema_dict):

    def create_issue(row,propertyToHeader_issue):

        issue = None

        try:
            issue = Issue(problem=row[propertyToHeader_issue['description_problem']],
                          solution=row[propertyToHeader_issue['description_solution']],
                          databaseInfo=databaseSchema_dict)
            try:
                issue._set_cause(row[propertyToHeader_issue['description_cause']])
            except KeyError:
                pass
            try:
                issue._set_effects(row[propertyToHeader_issue['description_effect']])
            except KeyError:
                pass
            try:
                issue._set_part_in_process(row[propertyToHeader_issue['part_in_process']])
            except KeyError:
                pass
            try:
                issue._set_necessary_part(row[propertyToHeader_issue['necessary_part']])
            except KeyError:
                pass
            try:
                issue._set_machine_down(row[propertyToHeader_issue['machine_down']])
            except KeyError:
                pass
            #TODO add a date clenizer for only 1 value
            try:
                issue._set_date_machine_down(row[propertyToHeader_issue['date_machine_down']])
            except KeyError:
                pass
            try:
                issue._set_date_machine_up(row[propertyToHeader_issue['date_machine_up']])
            except KeyError:
                pass
            try:
                issue._set_date_workorder_completion(row[propertyToHeader_issue['date_workorder_completion']])
            except KeyError:
                pass
            try:
                issue._set_date_workorder_start(row[propertyToHeader_issue['date_workorder_start']])
            except KeyError:
                pass
            try:
                issue._set_date_maintenance_technician_arrives(row[propertyToHeader_issue['date_maintenance_technician_arrive']])
            except KeyError:
                pass
            try:
                issue._set_date_problem_solved(row[propertyToHeader_issue['date_problem_solve']])
            except KeyError:
                pass
            try:
                issue._set_date_problem_found(row[propertyToHeader_issue['date_problem_found']])
            except KeyError:
                pass
            try:
                issue._set_date_part_ordered(row[propertyToHeader_issue['date_part_ordered']])
            except KeyError:
                pass
            try:
                issue._set_date_part_received(row[propertyToHeader_issue['date_part_received']])
            except KeyError:
                pass

        except KeyError:
            pass
        return issue

    def create_technicians(row, propertyToHeader_technician):
        skills = []
        try:
            for skill in row[propertyToHeader_technician['skills']].split(charsplit):
                skills.append(skill)
        except KeyError:
            pass

        crafts = []
        try:
            for craft in row[propertyToHeader_technician['crafts']].split(charsplit):
                crafts.append(craft)
        except KeyError:
            pass

        technicians = []
        try:
            for name in row[propertyToHeader_technician['name']].split(charsplit):
                technicians.append(Technician(name=name, skills=skills, crafts=crafts, databaseInfo=databaseSchema_dict))
        except KeyError:
            pass

        return technicians

    def create_operators(row,propertyToHeader_operator):
        operators = []
        try:
            for name in row[propertyToHeader_operator['name']].split(charsplit):
                operators.append(Operator(name=name, databaseInfo=databaseSchema_dict))
        except KeyError:
            pass

        return operators

    def create_machine(row, propertyToHeader_machine):
        machine = None

        try:
            machine = Machine(name=row[propertyToHeader_machine['name']], databaseInfo=databaseSchema_dict)
            #print(row[propertyToHeader_machine['name']])

            try:
                machine._set_manufacturer(row[propertyToHeader_machine['manufacturer']])
                #print(row[propertyToHeader_machine['manufacturer']])
            except KeyError:
                pass

            try:
                machine._set_machine_type(row[propertyToHeader_machine['type']])
                #print(row[propertyToHeader_machine['type']])
            except KeyError:
                pass

            try:
                machine._set_locasion(row[propertyToHeader_machine['locasion']])
                #print(row[propertyToHeader_machine['locasion']])
            except KeyError:
                pass

        except KeyError:
            pass

        return machine

    def create_items(row, propertyToHeader_item):
        items = []

        try:
            for item in row[propertyToHeader_item["keyword"]].split(charsplit):
                items.append(TagItem(keyword=item, databaseInfo=databaseSchema_dict))
        except KeyError:
            pass

        return items

    def create_problems(row, propertyToHeader_problem):
        problems = []

        try:
            for problem in row[propertyToHeader_problem["keyword"]].split(charsplit):
                problems.append(TagProblem(keyword=problem, databaseInfo=databaseSchema_dict))
        except KeyError:
            pass

        return problems

    def create_solutions(row, propertyToHeader_solution):
        solutions = []

        try:
            for solution in row[propertyToHeader_solution["keyword"]].split(charsplit):
                solutions.append(TagSolution(keyword=solution, databaseInfo=databaseSchema_dict))
        except KeyError:
            pass

        return solutions

    def create_unknowns(row, propertyToHeader_unknown):
        unknowns = []

        try:
            for unknown in row[propertyToHeader_unknown["keyword"]].split(charsplit):
                unknowns.append(TagUnknown(keyword=unknown, databaseInfo=databaseSchema_dict))
        except KeyError:
            pass

        return unknowns

    def create_problemItems(row, propertyToHeader_problemItem):
        problemItems = []

        try:
            for problemItem in row[propertyToHeader_problemItem["keyword"]].split(charsplit):
                problemItems.append(TagProblemItem(keyword=problemItem, databaseInfo=databaseSchema_dict))
        except KeyError:
            pass

        return problemItems

    def create_solutionItems(row, propertyToHeader_solutionItem):
        solutionItems = []

        try:
            for solutionItem in row[propertyToHeader_solutionItem["keyword"]].split(charsplit):
                solutionItems.append(TagSolutionItem(keyword=solutionItem, databaseInfo=databaseSchema_dict))
        except KeyError:
            pass

        return solutionItems


    #for each row in the dataframe
    for index, row in dataframe.iterrows():

        # creat the objects
        machine = create_machine(row, propertyToHeader_dict['machine'])
        operators = create_operators(row, propertyToHeader_dict['operator'])
        technicians = create_technicians(row, propertyToHeader_dict['technician'])
        issue = create_issue(row, propertyToHeader_dict['issue'])
        items = create_items(row, propertyToHeader_dict['item'])
        problems = create_problems(row, propertyToHeader_dict['problem'])
        solutions = create_solutions(row, propertyToHeader_dict['solution'])
        unknowns = create_unknowns(row, propertyToHeader_dict['unknown'])
        problemItems = create_problemItems(row, propertyToHeader_dict['problemitem'])
        solutionItems = create_solutionItems(row, propertyToHeader_dict['solutionitem'])

    return dataframe
