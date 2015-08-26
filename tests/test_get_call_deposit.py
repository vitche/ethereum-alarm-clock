from ethereum import utils as ethereum_utils


def test_get_call_value(deployed_contracts, eth_coinbase):
    alarm = deployed_contracts.Alarm
    alarm.client.defaults['from'] = eth_coinbase

    alarm.scheduleCall.sendTransaction(
        eth_coinbase,
        'arst',
        ethereum_utils.decode_hex('c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'),
        1000,
        value=12345,
    )
    call_key = alarm.getLastCallKey.call()
    assert call_key

    value = alarm.getCallDeposit.call(call_key)
    assert value == 12345
