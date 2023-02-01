IPy - class and tools for handling of IPv4 and IPv6 addresses and networks.

Website: https://github.com/autocracy/python-ipy/

Presentation of the API
=======================

The IP class allows a comfortable parsing and handling for most
notations in use for IPv4 and IPv6 addresses and networks. It was
greatly inspired by RIPE's Perl module NET::IP's interface but
doesn't share the implementation. It doesn't share non-CIDR netmasks,
so funky stuff like a netmask of 0xffffff0f can't be done here. ::

    >>> from IPy import IP
    >>> ip = IP('127.0.0.0/30')
    >>> for x in ip:
    ...  print(x)
    ...
    127.0.0.0
    127.0.0.1
    127.0.0.2
    127.0.0.3
    >>> ip2 = IP('0x7f000000/30')
    >>> ip == ip2
    1
    >>> ip.reverseNames()
    ['0.0.0.127.in-addr.arpa.', '1.0.0.127.in-addr.arpa.', '2.0.0.127.in-addr.arpa.', '3.0.0.127.in-addr.arpa.']
    >>> ip.reverseName()
    '0-3.0.0.127.in-addr.arpa.'
    >>> ip.iptype()
    'LOOPBACK'


Supports most IP address formats
================================

It can detect about a dozen different ways of expressing IP addresses
and networks, parse them and distinguish between IPv4 and IPv6 addresses: ::

    >>> IP('10.0.0.0/8').version()
    4
    >>> IP('::1').version()
    6

IPv4 addresses
--------------

::

    >>> print(IP(0x7f000001))
    127.0.0.1
    >>> print(IP('0x7f000001'))
    127.0.0.1
    >>> print(IP('127.0.0.1'))
    127.0.0.1
    >>> print(IP('10'))
    10.0.0.0

IPv6 addresses
--------------

::

    >>> print(IP('1080:0:0:0:8:800:200C:417A'))
    1080::8:800:200c:417a
    >>> print(IP('1080::8:800:200C:417A'))
    1080::8:800:200c:417a
    >>> print(IP('::1'))
    ::1
    >>> print(IP('::13.1.68.3'))
    ::d01:4403

Network mask and prefixes
-------------------------

::

    >>> print(IP('127.0.0.0/8'))
    127.0.0.0/8
    >>> print(IP('127.0.0.0/255.0.0.0'))
    127.0.0.0/8
    >>> print(IP('127.0.0.0-127.255.255.255'))
    127.0.0.0/8


Derive network address
===========================

IPy can transform an IP address into a network address by applying the given
netmask: ::

    >>> print(IP('127.0.0.1/255.0.0.0', make_net=True))
    127.0.0.0/8

This can also be done for existing IP instances: ::

    >>> print(IP('127.0.0.1').make_net('255.0.0.0'))
    127.0.0.0/8


Convert address to string
=========================

Nearly all class methods which return a string have an optional
parameter 'wantprefixlen' which controls if the prefixlen or netmask
is printed. Per default the prefilen is always shown if the network
contains more than one address: ::

    wantprefixlen == 0 / None     don't return anything   1.2.3.0
    wantprefixlen == 1            /prefix                 1.2.3.0/24
    wantprefixlen == 2            /netmask                1.2.3.0/255.255.255.0
    wantprefixlen == 3            -lastip                 1.2.3.0-1.2.3.255

You can also change the defaults on an per-object basis by fiddling with
the class members:

- NoPrefixForSingleIp
- WantPrefixLen

Examples of string conversions: ::

    >>> IP('10.0.0.0/32').strNormal()
    '10.0.0.0'
    >>> IP('10.0.0.0/24').strNormal()
    '10.0.0.0/24'
    >>> IP('10.0.0.0/24').strNormal(0)
    '10.0.0.0'
    >>> IP('10.0.0.0/24').strNormal(1)
    '10.0.0.0/24'
    >>> IP('10.0.0.0/24').strNormal(2)
    '10.0.0.0/255.255.255.0'
    >>> IP('10.0.0.0/24').strNormal(3)
    '10.0.0.0-10.0.0.255'
    >>> ip = IP('10.0.0.0')
    >>> print(ip)
    10.0.0.0
    >>> ip.NoPrefixForSingleIp = None
    >>> print(ip)
    10.0.0.0/32
    >>> ip.WantPrefixLen = 3
    >>> print(ip)
    10.0.0.0-10.0.0.0

Work with multiple networks
===========================

Simple addition of neighboring netblocks that can be aggregated will yield
a parent network of both, but more complex range mapping and aggregation
requires is available with the ``IPSet`` class which will hold any number of
unique address ranges and will aggregate overlapping ranges. ::

    >>> from IPy import IP, IPSet
    >>> IP('10.0.0.0/22') - IP('10.0.2.0/24')
    IPSet([IP('10.0.0.0/23'), IP('10.0.3.0/24')])
    >>> IPSet([IP('10.0.0.0/23'), IP('10.0.3.0/24'), IP('10.0.2.0/24')])
    IPSet([IP('10.0.0.0/22')])
    >>> s = IPSet([IP('10.0.0.0/22')])
    >>> s.add(IP('192.168.1.0/29'))
    >>> s
    IPSet([IP('10.0.0.0/22'), IP('192.168.1.0/29')])
    >>> s.discard(IP('192.168.1.2'))
    >>> s
    IPSet([IP('10.0.0.0/22'), IP('192.168.1.0/31'), IP('192.168.1.3'), IP('192.168.1.4/30')])

``IPSet`` supports the ``set`` method ``isdisjoint``: ::

    >>> s.isdisjoint(IPSet([IP('192.168.0.0/16')]))
    False
    >>> s.isdisjoint(IPSet([IP('172.16.0.0/12')]))
    True

``IPSet`` supports intersection: ::

    >>> s & IPSet([IP('10.0.0.0/8')])
    IPSet([IP('10.0.0.0/22')])

Compatibility and links
=======================

IPy 1.01 works on Python version 2.6 - 3.7.

The IP module should work in Python 2.5 as long as the subtraction operation
is not used. IPSet requires features of the collections class which appear
in Python 2.6, though they can be backported.

Eratta
======

When using IPv6 addresses, it is best to compare using  ``IP().len()``
instead of ``len(IP)``. Addresses with an integer value > 64 bits can break
the 2nd method.  See http://stackoverflow.com/questions/15650878 for more
info.

Fuzz testing for ``IPSet`` will throw spurious errors when the ``IPSet`` module
combines two smaller prefixes into a larger prefix that matches the random
prefix tested against.

This Python module is under BSD license: see COPYING file.

Further Information might be available at:
https://github.com/autocracy/python-ipy
