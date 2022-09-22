import os
from environment import ORIGIN_DB
from connection import Connection

cursor = Connection(
    ORIGIN_DB['host'],
    ORIGIN_DB['port'],
    ORIGIN_DB['user'],
    ORIGIN_DB['password'],
    ORIGIN_DB['database']
)

def get_wp_user_insert(wp_user, get_cols = True, metadata = False):
    '''
    get_wp_user_insert
    
    Gets user insert cols or values
    '''
    data = "("
    count = 0
    insert_data = wp_user.keys() if bool(get_cols) else wp_user.values()
    primary_key = 'umeta_id' if bool(metadata) else 'ID'
    for col in insert_data:
        count += 1
        if bool(get_cols) and col == primary_key or not bool(get_cols) and list(wp_user.keys())[list(wp_user.values()).index(col)] == primary_key:
            continue
        data += col if bool(get_cols) else "'{}'".format(col)
        if count < len(insert_data):
            data += ', '
   
    return data + ')'


migration_queries = ''
wp_user = cursor.query_data('SELECT * FROM wp_users WHERE ID = %s', [ORIGIN_DB['user_id']])[0]
wp_usermeta = cursor.query_data('SELECT * FROM wp_usermeta WHERE user_id = %s', [ORIGIN_DB['user_id']])
migration_queries += "INSERT INTO `wp_users` {} values {};\n".format(get_wp_user_insert(wp_user), get_wp_user_insert(wp_user, False))
for meta in wp_usermeta:
    migration_queries += "INSERT INTO `wp_usermeta` {} VALUES {};\n".format(get_wp_user_insert(meta, True, True), get_wp_user_insert(meta, False, True))

if (not os.path.exists('users')):
    os.makedirs('users')

with open('users/{}_migration.sql'.format(wp_user['user_nicename']), 'w') as migration_file:
    migration_file.write('-- Executar a query "INSERT INTO wp_user..." primeiro, e substituir o ID {} das queries seguintes pelo ID do usuário local gerado pela primeira query\n'.format(wp_user['ID']))
    migration_file.write(migration_queries)

print('Queries geradas com sucesso.')