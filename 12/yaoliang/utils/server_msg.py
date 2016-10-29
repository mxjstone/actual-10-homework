# coding: utf-8

import salt.client

client = salt.client.LocalClient()

# name是salt-minion的名称

# 查看磁盘信息（名称，挂载点，总量，未使用量，使用百分百）
def disk_msg(name):
    f = client.cmd(name,'disk.usage')
    data = f[name]

    d = {}
    for i in data.keys():
	if i == '/':
	    d['mount'] = i
	    d['filesystem'] = data[i]['filesystem']
	    if int(data[i]['1K-blocks'])/1024 > 1024:
		d['all'] = str(round(int(data[i]['1K-blocks'])/1024/1024))+'G'
		d['available'] = str(round(int(data[i]['available'])/1024/1024))+'G'
	    else:
		d['all'] = str(round(int(data[i]['1K-blocks'])/1024))+'M'
		d['available'] = str(round(int(data[i]['available'])/1024))+'M'
	    d['percent'] = data[i]['capacity']
#    return '{},{},{},{},{}\n'.format(filesystem,mount,all,available,percent)
    return d

# 主机名
def host_msg(name):
    f = client.cmd(name,'grains.item',['host']) 
    host = f[name]['host']

    return host

# Linux发行版和版本号
def os_msg(name):
    f = client.cmd(name,'grains.item',['osfullname','osrelease'])
    osfullname = f[name]['osfullname']
    osrelease = f[name]['osrelease']
    os_msg = osfullname + osrelease

    return os_msg

# cpu的型号
def cpu_model(name):
    f = client.cmd(name,'grains.item',['cpu_model'])
    cpu_model = f[name]['cpu_model']

    return cpu_model

# cpu的线程数（一些服务器没有此项）
#def cpu_thread(name):
#    f = client.cmd(name,'grains.item',['deployment'])
#    deployment = f[name]['deployment']
#
#    cpu_thread = int(deployment[-1])
#    return cpu_thread

# 磁盘总量
def mem_total(name):
    f = client.cmd(name,'grains.item',['mem_total'])
    mem_total = str(f[name]['mem_total']) + 'M'

    return mem_total


if __name__=='__main__':
    name = 'minion-192-168-3-251'
    print disk_msg(name)
    print host_msg(name)
    print os_msg(name)
    print cpu_model(name)
    print mem_total(name)
