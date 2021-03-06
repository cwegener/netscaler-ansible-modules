#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2017 Citrix Systems
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#


ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.0'}


DOCUMENTATION = '''
---
module: _
short_description: _
description:
    - _

version_added: 2.3.1

options:

    name:
        description:
            - >-
                Name for the service. Must begin with an ASCII alphabetic or underscore (_) character, and must
                contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals
                (=), and hyphen (-) characters. Cannot be changed after the service has been created.
            - "Minimum length = 1"

    ip:
        description:
            - "IP to assign to the service."
            - "Minimum length = 1"

    servername:
        description:
            - "Name of the server that hosts the service."
            - "Minimum length = 1"

    servicetype:
        choices:
            - 'HTTP'
            - 'FTP'
            - 'TCP'
            - 'UDP'
            - 'SSL'
            - 'SSL_BRIDGE'
            - 'SSL_TCP'
            - 'DTLS'
            - 'NNTP'
            - 'RPCSVR'
            - 'DNS'
            - 'ADNS'
            - 'SNMP'
            - 'RTSP'
            - 'DHCPRA'
            - 'ANY'
            - 'SIP_UDP'
            - 'SIP_TCP'
            - 'SIP_SSL'
            - 'DNS_TCP'
            - 'ADNS_TCP'
            - 'MYSQL'
            - 'MSSQL'
            - 'ORACLE'
            - 'RADIUS'
            - 'RADIUSListener'
            - 'RDP'
            - 'DIAMETER'
            - 'SSL_DIAMETER'
            - 'TFTP'
            - 'SMPP'
            - 'PPTP'
            - 'GRE'
            - 'SYSLOGTCP'
            - 'SYSLOGUDP'
            - 'FIX'
            - 'SSL_FIX'
        description:
            - "Protocol in which data is exchanged with the service."

    port:
        description:
            - "Port number of the service."
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"

    cleartextport:
        description:
            - >-
                Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic.
                Applicable to transparent SSL services.
            - "Minimum value = 1"

    cachetype:
        choices:
            - 'TRANSPARENT'
            - 'REVERSE'
            - 'FORWARD'
        description:
            - "Cache type supported by the cache server."

    maxclient:
        description:
            - "Maximum number of simultaneous open connections to the service."
            - "Minimum value = 0"
            - "Maximum value = 4294967294"

    healthmonitor:
        description:
            - "Monitor the health of this service. Available settings function as follows:"
            - "YES - Send probes to check the health of the service."
            - >-
                NO - Do not send probes to check the health of the service. With the NO option, the appliance shows
                the service as UP at all times.
            - "Default value: YES"

    maxreq:
        description:
            - "Maximum number of requests that can be sent on a persistent connection to the service."
            - "Note: Connection requests beyond this value are rejected."
            - "Minimum value = 0"
            - "Maximum value = 65535"

    cacheable:
        description:
            - "Use the transparent cache redirection virtual server to forward requests to the cache server."
            - "Note: Do not specify this parameter if you set the Cache Type parameter."
            - "Default value: NO"

    cip:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6
                address as its value. Used if the server needs the client's IP address for security, accounting, or
                other purposes, and setting the Use Source IP parameter is not a viable option.

    cipheader:
        description:
            - >-
                Name for the HTTP header whose value must be set to the IP address of the client. Used with the
                Client IP parameter. If you set the Client IP parameter, and you do not specify a name for the
                header, the appliance uses the header name specified for the global Client IP Header parameter (the
                cipHeader parameter in the set ns param CLI command or the Client IP Header parameter in the
                Configure HTTP Parameters dialog box at System > Settings > Change HTTP parameters). If the global
                Client IP Header parameter is not specified, the appliance inserts a header with the name
                "client-ip.".
            - "Minimum length = 1"

    usip:
        description:
            - >-
                Use the client's IP address as the source IP address when initiating a connection to the server. When
                creating a service, if you do not set this parameter, the service inherits the global Use Source IP
                setting (available in the enable ns mode and disable ns mode CLI commands, or in the System >
                Settings > Configure modes > Configure Modes dialog box). However, you can override this setting
                after you create the service.

    pathmonitor:
        description:
            - "Path monitoring for clustering."

    pathmonitorindv:
        description:
            - "Individual Path monitoring decisions."

    useproxyport:
        description:
            - >-
                Use the proxy port as the source port when initiating connections with the server. With the NO
                setting, the client-side connection port is used as the source port for the server-side connection.
            - "Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES."

    sc:
        description:
            - "State of SureConnect for the service."
            - "Default value: OFF"

    sp:
        description:
            - "Enable surge protection for the service."

    rtspsessionidremap:
        description:
            - "Enable RTSP session ID mapping for the service."
            - "Default value: OFF"

    clttimeout:
        description:
            - "Time, in seconds, after which to terminate an idle client connection."
            - "Minimum value = 0"
            - "Maximum value = 31536000"

    svrtimeout:
        description:
            - "Time, in seconds, after which to terminate an idle server connection."
            - "Minimum value = 0"
            - "Maximum value = 31536000"

    customserverid:
        description:
            - >-
                Unique identifier for the service. Used when the persistency type for the virtual server is set to
                Custom Server ID.
            - "Default value: \\"None\\""

    serverid:
        description:
            - "The identifier for the service. This is used when the persistency type is set to Custom Server ID."

    cka:
        description:
            - "Enable client keep-alive for the service."

    tcpb:
        description:
            - "Enable TCP buffering for the service."

    cmp:
        description:
            - "Enable compression for the service."

    maxbandwidth:
        description:
            - "Maximum bandwidth, in Kbps, allocated to the service."
            - "Minimum value = 0"
            - "Maximum value = 4294967287"

    accessdown:
        description:
            - >-
                Use Layer 2 mode to bridge the packets sent to this service if it is marked as DOWN. If the service
                is DOWN, and this parameter is disabled, the packets are dropped.
            - "Default value: NO"

    monthreshold:
        description:
            - >-
                Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to
                mark a service as UP or DOWN.
            - "Minimum value = 0"
            - "Maximum value = 65535"

    state:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Initial state of the service."
            - "Default value: ENABLED"

    downstateflush:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do
                not enable this option for applications that must complete their transactions.
            - "Default value: ENABLED"

    tcpprofilename:
        description:
            - "Name of the TCP profile that contains TCP configuration settings for the service."
            - "Minimum length = 1"
            - "Maximum length = 127"

    httpprofilename:
        description:
            - "Name of the HTTP profile that contains HTTP configuration settings for the service."
            - "Minimum length = 1"
            - "Maximum length = 127"

    hashid:
        description:
            - >-
                A numerical identifier that can be used by hash based load balancing methods. Must be unique for each
                service.
            - "Minimum value = 1"

    comment:
        description:
            - "Any information about the service."

    appflowlog:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Enable logging of AppFlow information."
            - "Default value: ENABLED"

    netprofile:
        description:
            - "Network profile to use for the service."
            - "Minimum length = 1"
            - "Maximum length = 127"

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID
                of 0.
            - "Minimum value = 0"
            - "Maximum value = 4094"

    processlocal:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                By turning on this option packets destined to a service in a cluster will not under go any steering.
                Turn this option for single packet request response mode or when the upstream device is performing a
                proper RSS for connection based distribution.
            - "Default value: DISABLED"

    dnsprofilename:
        description:
            - >-
                Name of the DNS profile to be associated with the service. DNS profile properties will applied to the
                transactions processed by a service. This parameter is valid only for ADNS and ADNS-TCP services.
            - "Minimum length = 1"
            - "Maximum length = 127"

    ipaddress:
        description:
            - "The new IP address of the service."

    weight:
        description:
            - >-
                Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its
                binding with the service determines how much the monitor contributes toward keeping the health of the
                service above the value configured for the Monitor Threshold parameter.
            - "Minimum value = 1"
            - "Maximum value = 100"

    monitor_name_svc:
        description:
            - "Name of the monitor bound to the specified service."
            - "Minimum length = 1"

    riseapbrstatsmsgcode:
        description:
            - "The code indicating the rise apbr status."

    delay:
        description:
            - >-
                Time, in seconds, allocated to the NetScaler appliance for a graceful shutdown of the service. During
                this period, new requests are sent to the service only for clients who already have persistent
                sessions on the appliance. Requests from new clients are load balanced among other available
                services. After the delay time expires, no requests are sent to the service, and the service is
                marked as unavailable (OUT OF SERVICE).

    graceful:
        description:
            - >-
                Shut down gracefully, not accepting any new connections, and disabling the service when all of its
                connections are closed.
            - "Default value: NO"

    all:
        description:
            - "Display both user-configured and dynamically learned services."

    Internal:
        description:
            - "Display only dynamically learned services."

    newname:
        description:
            - >-
                New name for the service. Must begin with an ASCII alphabetic or underscore (_) character, and must
                contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals
                (=), and hyphen (-) characters.
            - "Minimum length = 1"


extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled, get_immutables_intersection
try:
    from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
    PYTHON_SDK_IMPORTED = True
except ImportError as e:
    PYTHON_SDK_IMPORTED = False


def _exists(client, module):
    if _.count_filtered(client, 'name:%s' % module.params['name']) > 0:
        return True
    else:
        return False


def _identical(client, module, _proxy):
    _list = _.get_filtered(client, 'name:%s' % module.params['name'])
    diff_dict = _proxy.diff_object(_list[0])
    if len(diff_dict) == 0:
        return True
    else:
        return False


def diff_list(client, module, _proxy):
    _list = _.get_filtered(client, 'name:%s' % module.params['name'])
    return _proxy.diff_object(_list[0])


def main():

    module_specific_arguments = dict(
        name=dict(type='str'),
        ip=dict(type='str'),
        servername=dict(type='str'),
        servicetype=dict(
            type='str',
            choices=[
                'HTTP',
                'FTP',
                'TCP',
                'UDP',
                'SSL',
                'SSL_BRIDGE',
                'SSL_TCP',
                'DTLS',
                'NNTP',
                'RPCSVR',
                'DNS',
                'ADNS',
                'SNMP',
                'RTSP',
                'DHCPRA',
                'ANY',
                'SIP_UDP',
                'SIP_TCP',
                'SIP_SSL',
                'DNS_TCP',
                'ADNS_TCP',
                'MYSQL',
                'MSSQL',
                'ORACLE',
                'RADIUS',
                'RADIUSListener',
                'RDP',
                'DIAMETER',
                'SSL_DIAMETER',
                'TFTP',
                'SMPP',
                'PPTP',
                'GRE',
                'SYSLOGTCP',
                'SYSLOGUDP',
                'FIX',
                'SSL_FIX',
            ]
        ),
        port=dict(type='int'),
        cleartextport=dict(type='int'),
        cachetype=dict(
            type='str',
            choices=[
                'TRANSPARENT',
                'REVERSE',
                'FORWARD',
            ]
        ),
        maxclient=dict(type='float'),
        healthmonitor=dict(type='bool'),
        maxreq=dict(type='float'),
        cacheable=dict(type='bool'),
        cip=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        cipheader=dict(type='str'),
        usip=dict(type='bool'),
        pathmonitor=dict(type='bool'),
        pathmonitorindv=dict(type='bool'),
        useproxyport=dict(type='bool'),
        sc=dict(type='bool'),
        sp=dict(type='bool'),
        rtspsessionidremap=dict(type='bool'),
        clttimeout=dict(type='float'),
        svrtimeout=dict(type='float'),
        customserverid=dict(type='str'),
        serverid=dict(type='float'),
        cka=dict(type='bool'),
        tcpb=dict(type='bool'),
        cmp=dict(type='bool'),
        maxbandwidth=dict(type='float'),
        accessdown=dict(type='bool'),
        monthreshold=dict(type='float'),
        state=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        downstateflush=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        tcpprofilename=dict(type='str'),
        httpprofilename=dict(type='str'),
        hashid=dict(type='float'),
        comment=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        netprofile=dict(type='str'),
        td=dict(type='float'),
        processlocal=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        dnsprofilename=dict(type='str'),
        ipaddress=dict(type='str'),
        weight=dict(type='float'),
        monitor_name_svc=dict(type='str'),
        riseapbrstatsmsgcode=dict(type='int'),
        delay=dict(type='float'),
        graceful=dict(type='bool'),
        all=dict(type='bool'),
        Internal=dict(type='bool'),
        newname=dict(type='str'),
    )

    hand_inserted_arguments = dict(
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)
    argument_spec.update(hand_inserted_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines,
    )

    # Fail the module if imports failed
    if not PYTHON_SDK_IMPORTED:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)

    try:
        client.login()
    except nitro_exception as e:
        msg = "nitro exception during login. errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg)
    except Exception as e:
        if str(type(e)) == "<class 'requests.exceptions.ConnectionError'>":
            module.fail_json(msg='Connection error %s' % str(e))
        elif str(type(e)) == "<class 'requests.exceptions.SSLError'>":
            module.fail_json(msg='SSL Error %s' % str(e))
        else:
            module.fail_json(msg='Unexpected error during login %s' % str(e))

    readwrite_attrs = [
        'name',
        'ip',
        'servername',
        'servicetype',
        'port',
        'cleartextport',
        'cachetype',
        'maxclient',
        'healthmonitor',
        'maxreq',
        'cacheable',
        'cip',
        'cipheader',
        'usip',
        'pathmonitor',
        'pathmonitorindv',
        'useproxyport',
        'sc',
        'sp',
        'rtspsessionidremap',
        'clttimeout',
        'svrtimeout',
        'customserverid',
        'serverid',
        'cka',
        'tcpb',
        'cmp',
        'maxbandwidth',
        'accessdown',
        'monthreshold',
        'state',
        'downstateflush',
        'tcpprofilename',
        'httpprofilename',
        'hashid',
        'comment',
        'appflowlog',
        'netprofile',
        'td',
        'processlocal',
        'dnsprofilename',
        'monconnectionclose',
        'ipaddress',
        'weight',
        'monitor_name_svc',
        'riseapbrstatsmsgcode',
        'delay',
        'graceful',
        'all',
        'Internal',
        'newname',
    ]

    readonly_attrs = [
        'numofconnections',
        'policyname',
        'serviceconftype',
        'serviceconftype2',
        'value',
        'gslb',
        'dup_state',
        'publicip',
        'publicport',
        'svrstate',
        'monitor_state',
        'monstatcode',
        'lastresponse',
        'responsetime',
        'riseapbrstatsmsgcode2',
        'monstatparam1',
        'monstatparam2',
        'monstatparam3',
        'statechangetimesec',
        'statechangetimemsec',
        'tickssincelaststatechange',
        'stateupdatereason',
        'clmonowner',
        'clmonview',
        'serviceipstr',
        'oracleserverversion',
        '__count',
    ]

    immutable_attrs = [
        'name',
        'ip',
        'servername',
        'servicetype',
        'port',
        'cleartextport',
        'cachetype',
        'cipheader',
        'serverid',
        'state',
        'td',
        'monitor_name_svc',
        'riseapbrstatsmsgcode',
        'delay',
        'graceful',
        'all',
        'Internal',
        'newname',
    ]

    transforms = {
        'pathmonitorindv': ['bool_yes_no'],
        'cacheable': ['bool_yes_no'],
        'cka': ['bool_yes_no'],
        'pathmonitor': ['bool_yes_no'],
        'tcpb': ['bool_yes_no'],
        'sp': ['bool_on_off'],
        'graceful': ['bool_yes_no'],
        'usip': ['bool_yes_no'],
        'healthmonitor': ['bool_yes_no'],
        'useproxyport': ['bool_yes_no'],
        'rtspsessionidremap': ['bool_on_off'],
        'sc': ['bool_on_off'],
        'accessdown': ['bool_yes_no'],
        'cmp': ['bool_yes_no'],
    }

    # Instantiate config proxy
    _proxy = ConfigProxy(
        actual=_(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        immutable_attrs=immutable_attrs,
        transforms=transforms,
    )

    try:
        ensure_feature_is_enabled(client, ' _')
        # Apply appropriate state
        if module.params['state'] == 'present':
            if not _exists(client, module):
                if not module.check_mode:
                    _proxy.add()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            elif not _identical(client, module, _proxy):

                # Check if we try to change value of immutable attributes
                immutables_changed = get_immutables_intersection(_proxy, diff_list(client, module, _proxy).keys())
                if immutables_changed != []:
                    module.fail_json(msg='Cannot update immutable attributes %s' % (immutables_changed,), diff=diff(client, module, _proxy), **module_result)

                if not module.check_mode:
                    _proxy.update()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for state
            if not module.check_mode:
                if not _exists(client, module):
                    module.fail_json(msg='_ does not exist', **module_result)
                if not _identical(client, module, _proxy):
                    module.fail_json(msg='_ differs from configured', diff=diff(client, module, _proxy), **module_result)

        elif module.params['state'] == 'absent':
            if _exists(client, module):
                if not module.check_mode:
                    _proxy.delete()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for state
            if not module.check_mode:
                if _exists(client, module):
                    module.fail_json(msg='_ still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
