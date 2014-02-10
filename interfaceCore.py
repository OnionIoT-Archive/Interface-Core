import amqp_rpc as rpc



@rpc.register
def IF_REG_FUNCTION(params):
    payload = {}
    payload['path'] = params['path']
    payload['verb'] = params['verb']
    payload['deviceId'] = params['deviceId']
    payload['functionId'] = params['functionId']
    if params['verb'].upper() == "POST":
        payload['postParams'] = params['postParams']
    else:
        payload['postParams'] = []
    rpc.call('DB_ADD_PROCEDURE', payload)
    

@rpc.register
def IF_UPDATE_STATE(params):
    print rpc.call('IF_CALL_FUNCTION',{})
    return 'OK'

@rpc.register
def IF_CALL_FUNCTION(params):
    payload = {}
    payload['path'] = params['path']
    payload['verb'] = params['verb']
    payload['deviceId'] = params['deviceId']
    path = params['path']
    verb = params['verb']
    deviceId = params['deviceId']

    result = rpc.call('DB_GET_PROCEDURE', payload)
    if result != None:
        fid = result["functionId"]
        if params['verb'].upper() == "POST":
            postParams = params['postParams'] 
            params = []
            for p in result['postParams']:
                temp = str(postParams[p])
                params.append(str(temp.replace(',','.').replace(';',':')))
            cmd = "%s;%s"%(fid,','.join(params))
        else:
            postParams = None
            cmd = fid

        print '%s < %s'%(deviceId, cmd)

        rpc.call('DB_ADD_HISTORY', {
            'deviceId': deviceId,
            'action': "%s: %s"%(verb, path),
            'payload': postParams
            })

    return None

print "Started ..."
rpc.start()
