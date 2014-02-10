import amqp_rpc as rpc

print "#### TEST ####"
deviceId = 'rIJQNvNk'
print rpc.call('IF_REG_FUNCTION', {
    'path': '/hello',
    'verb': 'GET',
    'deviceId': deviceId,
    'functionId': 2
    }, True)

print rpc.call('IF_REG_FUNCTION', {
    'path': '/hello2',
    'verb': 'POST',
    'deviceId': deviceId,
    'functionId': 2,
    'postParams': ['a','b']
    })

print rpc.call('IF_CALL_FUNCTION', {
    'deviceId': deviceId,
    'path': '/hello',
    'verb': 'GET'
    })

print rpc.call('IF_CALL_FUNCTION', {
    'deviceId': deviceId,
    'path': '/hello2',
    'verb': 'POST',
    'postParams': {'a': '1', 'b': '2'}
    })
#print rpc.call('IF_UPDATE_STATE', {})
