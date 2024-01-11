import pandas as pd
import time
import argparse

nested_set = pd.DataFrame(columns=['id', 'name', 'left_value', 'right_value'])

INITIAL_LEFT_VALUE = 1
INITIAL_RIGHT_VALUE = 2


def add_node_to_nested_set(node: dict, parent_id=None):
    if parent_id is None:
        if not nested_set.empty:
            nested_set['left_value'] += 2
            nested_set['right_value'] += 2
        nested_set.loc[len(nested_set)] = [node['id'], node['name'], INITIAL_LEFT_VALUE, INITIAL_RIGHT_VALUE]
    else:
        parent_row = nested_set[nested_set['id'] == parent_id]
        p_left_value = parent_row.iloc[0]['left_value']

        nested_set.loc[(nested_set['left_value'] >= p_left_value) & (nested_set['id'] != parent_id), 'left_value'] +=2
        nested_set.loc[nested_set['right_value'] >= p_left_value, 'right_value'] += 2
        nested_set.loc[len(nested_set)] = [node['id'], node['name'], p_left_value+1, p_left_value+2]


def create_nested_set(tree: list, parent_id = None):
    for node in tree:
        add_node_to_nested_set(node, parent_id)
        if 'children' in node and node['children']:
            create_nested_set(node['children'], node['id'])



def query_parent_child_relationship(parent_name):
    parent_row = nested_set[nested_set['name'] == parent_name]
    if parent_row.empty:
        print(f'There is no parent having name {parent_name} in the nested set')
        return

    p_left_value, p_right_value = parent_row.iloc[0]['left_value'], parent_row.iloc[0]['right_value']
    
    children_row = nested_set[(nested_set['left_value'] > p_left_value) & (nested_set['right_value'] < p_right_value)]

    if children_row.empty:
        print(f"There is no children of the parent having name {parent_name}")
    else:
        print(f"The children of the parent having name {parent_name} are {', '.join(children_row['name'])}")

def evaluate_creating_nested_set(data):
    start_time = time.perf_counter()
    create_nested_set(hierarchical_data)
    end_time = time.perf_counter()
    print(f"Time to create nested_set is {end_time - start_time} secs")    


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--get_nested_set',help='create a nested set based on the given hierarchical_data', action='store_true')
    parser.add_argument('--get_parent_name', type=str, help='retrieve the children of a parent given its name')
    parser.add_argument('--get_time_performance', help='retrieve the time to create the nested set given the data', action='store_true')

    args = parser.parse_args()
    
    hierarchical_data = [
        {'id': 1, 'name': 'Node 1', 'children': [
            {'id': 2, 'name': 'Node 1.1'},
            {'id': 3, 'name': 'Node 1.2', 'children': [
                {'id': 4, 'name': 'Node 1.2.1'},
                {'id': 5, 'name': 'Node 1.2.2'},
            ]}
        ]},
        {'id': 6, 'name': 'Node 2'},
    ]

    create_nested_set(hierarchical_data)
    if args.get_nested_set:
        print(nested_set)
    if args.get_parent_child_relationship:
        query_parent_child_relationship(args.get_parent_child_relationship)
    if args.get_time_performance:
        evaluate_creating_nested_set(hierarchical_data)

