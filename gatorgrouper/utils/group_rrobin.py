""" group using round robin approach"""

import logging
import random
import itertools
import group_scoring


def group_rrobin_group_size(responses, grpsize):
    """ group responses using round robin approach """

    # setup target groups
    groups = list()  # // integer div
    responsesToRemove = list()
    numgrps = len(responses) // grpsize
    logging.info("target groups: %d", numgrps)

    for _ in range(numgrps):
        groups.append(list())

    logging.info("Groups looks like: " + str(groups))
    # setup cyclical group target
    indices = list(range(0, numgrps))
    target_group = itertools.cycle(indices)

    logging.info(responses)
    # randomize the order in which the columns will be drained
    columns = list()
    for col in range(1, len(responses[0])):
        columns.append(col)
    logging.info("Columns looks like:" + str(columns))
    random.shuffle(columns)
    logging.info("Columns post shuffle looks like:" + str(columns))

    # iterate through the response columns
    for col in columns:
        logging.info("Col looks like:" + str(col))
        responses = [x for x in responses if x not in responsesToRemove]
        for response in responses:
            logging.info("responses looks like:" + str(responses))
            logging.info("response looks like:" + str(response))
            logging.info("responses to remove looks like:" +str(responsesToRemove))
            if response[col] is True:
                logging.info("response is true, groups looks like:" + str(groups))
                groups[target_group.__next__()].append(response)
                responsesToRemove.append(response)
                logging.info("changed groups, now looks like:" + str(groups))

    # disperse anyone not already grouped
    while responses:
        groups[target_group.__next__()].append(responses[0])
        responses.remove(responses[0])

    # scoring and return
    scores, ave = [], 0
    scores, ave = group_scoring.score_groups(groups)
    return groups


def group_rrobin_num_group(responses, numgrps):
    """ group responses using round robin approach """

    # setup target groups
    groups = list()  # // integer div
    logging.info("target groups: %d", numgrps)
    for _ in range(numgrps):
        groups.append(list())

    # setup cyclical group target
    indices = list(range(0, numgrps))
    target_group = itertools.cycle(indices)

    # randomize the order in which the columns will be drained
    columns = list()
    for col in range(1, len(responses[0])):
        columns.append(col)
    random.shuffle(columns)
    logging.info("column priority: %d", columns)

    # iterate through the response columns
    for col in columns:
        for response in responses:
            if response[col] is True:
                groups[target_group.__next__()].append(response)
                responses.remove(response)

    # disperse anyone not already grouped
    while responses:
        groups[target_group.__next__()].append(responses[0])
        responses.remove(responses[0])

    # scoring and return
    scores, ave = [], 0
    scores, ave = group_scoring.score_groups(groups)
    logging.info("scores: %d", scores)
    logging.info("average: %d", ave)
    return groups
