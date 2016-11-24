# coding:utf-8

class MysqlConfig():
    SQL_HOST='localhost'
    SQL_USER='root'
    SQL_PASSWD='123456'
    SQL_DB='reboot10'

class Table():
    FIELDS_USER=['id','name','name_cn','password','email','email_password','mobile','role','status']
    FIELDS_IDC=['id','name','name_cn','address','adminer','phone','num']
    FIELDS_CABINET=['id','name','idc_id','u_num','power']
    FIELDS_SERVER=['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']
    FIELDS_CODE=['id','update_date','package','update_persion','project','message']
    FIELDS_OPS_JOBS=['id','apply_date','apply_type','apply_desc','deal_persion','status','deal_desc','deal_time','apply_persion']

class RemoteHost():
    HOST1=['192.168.1.100',22,'root','123456']
    HOST2=['192.168.1.101',22,'root','123456']
    HOST3=['192.168.1.102',22,'root','123456']
#    HOST1=['192.168.38.250',22,'root','890iop']
