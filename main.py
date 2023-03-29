# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []

    contacts = {}
    for cur_query in queries:
        if cur_query.number > 1 and cur_query.number < 10**7:
            if cur_query.type == 'add':
                if cur_query.name != 'not found' and len(cur_query.name) <= 15:
                    contacts[cur_query.number] = cur_query.name
            elif cur_query.type == 'del':
                if cur_query.number in contacts:
                    del contacts[cur_query.number]
            else:
                response = 'not found'
                if cur_query.number in contacts:
                    response = contacts[cur_query.number]
                result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))