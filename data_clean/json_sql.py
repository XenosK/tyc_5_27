# -*- coding:utf-8 -*-
import json
import pymysql
from tyc_json_list import zyry,bgjl,fzjg,rzls,hxtd,qyyw,flss,sxr,bzxr,\
	jyyc,xzcf,yzwf,gqcz,dcdy,qsgg,ztb,xxgd,swpj,zzzs,sbxx,zl
import chardet
import sys
reload(sys)
sys.setdefaultencoding('utf-8')




def get_all_json():

    global warn ,error,null
    warn= 'warn'
    error = 'error'
    null ='null'
    wu = '[]'
    kon = '{}'

    #基本信息数据
    def get_jbxx(jbxxss):
        jbxxs = json.loads(jbxxss)
        base_info1 = {}
        try:
            base_info1['legal_representative'] = jbxxs[u'法人代表']
        except:
            base_info1['legal_representative'] = []
        try:
            base_info1['registered_capital'] = jbxxs[u'注册资本']
        except:
            base_info1['registered_capital'] = []
        try:
           base_info1['registered_time'] = jbxxs[u'注册时间']
        except:
            base_info1['registered_time'] = []
        try:
            base_info1['management_status'] = jbxxs[u'经营状态']
        except:
            base_info1['management_status'] = []
        try:
            base_info1['business_registration_number'] = jbxxs[u'工商注册号']
        except:
            base_info1['business_registration_number'] = []
        try:
            base_info1['organization_code'] = jbxxs[u'组织机构代码']
        except:
            base_info1['organization_code'] = []
        try:
            base_info1['uniform_credit_code'] = jbxxs[u'统一信用代码']
        except:
            base_info1['uniform_credit_code'] = []
        try:
            base_info1['industry'] = jbxxs[u'企业类型']
        except:
            base_info1['industry'] = []
        try:
            base_info1['enterprise_type'] = jbxxs[u'行业']
        except:
            base_info1['enterprise_type'] = []
        try:
            base_info1['business_term'] = jbxxs[u'营业期限']
        except:
            base_info1['business_term'] = []
        try:
            base_info1['approval_date'] = jbxxs[u'核准日期']
        except:
            base_info1['approval_date'] = []
        try:
            base_info1['registration_authority'] = jbxxs[u'登记机关']
        except:
            base_info1['registration_authority'] = []
        try:
            base_info1['registered_address'] = jbxxs[u'注册地址']
        except:
            base_info1['registered_address'] = []
        try:
            base_info1['scope_of_business'] = jbxxs[u'经营范围']
            #.replace(u'收起','').replace(u'详细','').replace('^；','')
        except:
            base_info1['scope_of_business'] = []
        base_info1 = clean(**base_info1)
        # 转换成数据库存储需要的格式
        base_info2 = json.dumps(base_info1,ensure_ascii=False)
        return  base_info2

    #股东信息数据
    def get_gdxx(qybjs):
        gdxxs = clean_dict(qybjs, u'股东信息')
        #shareholder_info2 = {}
        if gdxxs == {}:
            shareholder_info2 = []
        else:
            fields = gdxxs['result']
            shareholder_info_list = []
            for field in fields:
                shareholder_info1 = {}
                #field = clean(**field)
                try:
                    shareholder_info1['shareholder'] = field['name']
                except:
                    shareholder_info1['shareholder'] = []
                try:
                    list = field['capital']
                except:
                    list = []
                try:
                    shareholder_info1['contributive_proportion'] = list[0]['percent']
                except:
                    shareholder_info1['contributive_proportion'] = []
                try:
                    shareholder_info1['subscribed_capital_contribution'] = list[0]['amomon']
                except:
                    shareholder_info1['subscribed_capital_contribution'] = []
                shareholder_info1 = clean(**shareholder_info1)
                shareholder_info_list.append(shareholder_info1)
            #print list(shareholder_info_list)
            #shareholder_info2 = {'shareholder_info':shareholder_info_list}
            #shareholder_info2['shareholder_info'] = shareholder_info_list
            #转换成数据库存储需要的格式
            shareholder_info2 = shareholder_info_list
        shareholder_info2 = json.dumps(shareholder_info2,ensure_ascii=False)
        return shareholder_info2

    #法院公告数据
    def get_fygg(sffxs):
        fygg = clean_dict(sffxs, u'法院公告')
        if fygg == {}:
            court_notice2 = []
        else:
            fields = fygg
            court_notice_list = []
            for field in fields:
                court_notice1 = {}
                #field = clean(**field)
                try:
                    court_notice1['time'] = field['publishdate']
                except:
                    court_notice1['time'] = []
                try:
                    court_notice1['appellant'] = field['party1']
                except:
                    court_notice1['appellant'] = []
                try:
                    court_notice1['defendant'] = field['party2']
                except:
                    court_notice1['defendant'] = []
                try:
                    court_notice1['announcement_type'] = field['bltntypename']
                except:
                    court_notice1['announcement_type'] = []
                try:
                    court_notice1['court'] = field['courtcode']
                except:
                    court_notice1['court'] = []
                court_notice1 = clean(**court_notice1)
                court_notice_list.append(court_notice1)
            # 转换成数据库存储需要的格式
            court_notice2 = court_notice_list
        court_notice2 = json.dumps(court_notice2,ensure_ascii=False)
        return  court_notice2
    def get_fygg(sffxs):
        fygg = clean_dict(sffxs, u'法院公告')
        if fygg == {}:
            court_notice2 = []
        else:
            fields = fygg
            court_notice_list = []
            for field in fields:
                court_notice1 = {}
                #field = clean(**field)
                try:
                    court_notice1['time'] = field['publishdate']
                except:
                    court_notice1['time'] = []
                try:
                    court_notice1['appellant'] = field['party1']
                except:
                    court_notice1['appellant'] = []
                try:
                    court_notice1['defendant'] = field['party2']
                except:
                    court_notice1['defendant'] = []
                try:
                    court_notice1['announcement_type'] = field['bltntypename']
                except:
                    court_notice1['announcement_type'] = []
                try:
                    court_notice1['court'] = field['courtcode']
                except:
                    court_notice1['court'] = []
                court_notice1 = clean(**court_notice1)
                court_notice_list.append(court_notice1)
            # 转换成数据库存储需要的格式
            court_notice2 = court_notice_list
        court_notice2 = json.dumps(court_notice2,ensure_ascii=False)
        return  court_notice2

    #企业发展模块数据
    def get_data_qyfz(sql_dict,**args):
        #sql_dict = sql_dict
        dict1 = clean_dict(sql_dict, args['field'])
        #h2 = {}
        if type(dict1) != dict:
            dict1 = json.loads(dict1)
        else:pass
        if dict1 == {}:
            h2  = []
        else:
            fields1 = dict1['page']
            fields = fields1[args['list']]
            h2_list = []
            for field in fields:
                h1 = {}
                nokeys = ['ks','sql','field','list']
                for key in args:
                    if key not in nokeys:
                        try:
                            h1[key] = field[args[key]]
                        except:
                            h1[key] = []
                        #else:
                        #    try:
                        #        h1[key] = h1[key]#.replace('\n', '').replace('\r', '').replace('\r\n', '') .replace('</em>','').replace('<em>','').replace('<br>','')
                        #    except:
                        #        pass
                        '''
                        try:
                            if h1[key] == str:
                                h1[key] = field[args[key]].replace('\n','').replace('\r','').replace('\r\n','')
                            else:
                                h1[key] = fields[args[key]]
                        except Exception as e:
                            h1[key] = []
                        '''
                h1 = clean(**h1)
                h2_list.append(h1)
            #h2[args['ks']] = h2_list
            h2 = h2_list
        h2 = json.dumps(h2,ensure_ascii=False)
        return  h2

    def get_data_dcdy(sql_dict, **args):
        # sql_dict = sql_dict
        dict1 = clean_dict(sql_dict, args['field'])
        print dict1
        # h2 = {}
        if type(dict1) != dict:
            dict1 = json.loads(dict1)
        else:pass
        if dict1 == {}:
            h2 = []
        else:
            #fields1 = dict1['page']
            fields = dict1[args['list']]
            h2_list = []
            for field in fields:
                field = field['baseInfo']
                h1 = {}
                nokeys = ['ks', 'sql', 'field', 'list']
                for key in args:
                    if key not in nokeys:
                        try:
                            h1[key] = field[args[key]]
                        except:
                            h1[key] = []
                h1 = clean(**h1)
                h2_list.append(h1)
            # h2[args['ks']] = h2_list
            h2 = h2_list
        h2 = json.dumps(h2, ensure_ascii=False)
        return h2

    #一般性json数据（进行换行符清洗）
    def get_data_json(sql_dict,**args):
        #提取数据时候，先清洗成字典(sql_dict为数据库提取的值，args为预先定义好的字典数据)
        dict1 = clean_dict(sql_dict, args['field'])
        #假如清洗后的数据不是字典，则转换一下
        if type(dict1) != dict:
            dict1 = json.loads(dict1)
        else:pass
        #清洗后的数据为{}
        if dict1 == {}:
            h2 = []
        #清洗后的数据不为空
        else:
            #这边调用事先存储在字典里的key-value对应关系
            fields = dict1[args['list']]
            h2_list = []
            #print fields
            for field in fields:
                h1 = {}
                nokeys = ['ks','sql','field','list']
                for key in args:
                    if key not in nokeys:
                        try:
                            h1[key] = field[args[key]]
                        except:
                            h1[key] = []
                        #else:
                        #    try:
                        #        h1[key] = h1[key]#.replace('\n', '').replace('\r', '').replace('\r\n', '').replace('</em>','').replace('<em>','').replace('<br>','')
                        #    except:
                        #        pass
                        '''
                        try:
                            #判断value是否为str类型，是的话则清西掉回车等字符（换一种写法就是，判断哪些key需要转换）
                            if type(field[args[key]]) == str:
                                h1[key] = field[args[key]].replace('\n','').replace('\r','').replace('\r\n','')
                                #.replace('</em>','').replace('<em>','').replace('<br>','')
                            else:
                                h1[key] = field[args[key]]
                        #如果取不到对应key，则返回空值
                        except Exception as e:
                            h1[key] = []
                        '''
                #存储到数据库前调用一下入库的清晰方法
                h1 = clean(**h1)
                h2_list.append(h1)
                #h2[args['ks']] = h2_list
            #抓换成指定的数据类型格式
            h2 = h2_list
        h2 = json.dumps(h2,ensure_ascii=False)
        return  h2
    '''
    #不进行换行符清洗
    def get_data_json1(sql_dict,**args):
        dict1 = clean_dict(sql_dict, args['field'])
        if type(dict1) != dict:
            dict1 = json.loads(dict1)
        #h2 = {}
        if dict1 == {}:
            h2 = []
        else:
            fields = dict1[args['list']]
            h2_list = []
            #print fields
            for field in fields:
                h1 = {}
                nokeys = ['ks','sql','field','list']
                for key in args:
                    if key not in nokeys:
                        try:
                            h1[key] = field[args[key]]
                        except Exception as e:
                            h1[key] = []
                h1 = clean(**h1)
                h2_list.append(h1)
                #h2[args['ks']] = h2_list
            h2 = h2_list
        h2 = json.dumps(h2,ensure_ascii=False)
        return  h2
    '''
    '''
    #判断值是否为空
    def pdnos(**kw):
        for key in kw:
            if kw[key] == warn:
                kw[key] = []
            elif kw[key] == null:
                kw[key] = []
            elif kw[key] == error:
                kw[key] = []
            elif kw[key] == wu:
                kw[key] = []
            elif kw[key] == kon:
                kw[key] = []
            else:
                pass
        return kw
    '''
    #提取数据和入库前清洗数据
    def clean(**args):
        for key in args:
            if args[key] == warn:
                args[key] = ''
            elif args[key] == null:
                args[key] = ''
            elif args[key] == error:
                args[key] = ''
            elif args[key] == wu:
                args[key] = ''
            elif args[key] == kon:
                args[key] = ''
            elif args[key] == []:
                args[key] = ''
            elif args[key] == {}:
                args[key] = ''
            elif args[key] == None:
                args[key] = ''
            else:
                try:
                    args[key] = args[key].replace('\n', '').replace('\r', '').replace('\r\n', '').replace('</em>','').replace('<em>','').replace('<br>','')
                except:
                    pass
        return args

    #提取数据时候清洗数据
    def clean_dict(tcy_d,keys):
        #print keys
        #将对应的数据库中的字符串转化为字典
        #tyc_d = tcy_d.replace('null','').replace('</em>','').replace('<em>','').replace('<br>','')
        tyc_d = json.loads(tcy_d)
        try:
            tyc_info = tyc_d[keys]
        except:
            print(u'%s数据不存在'%keys)
            info = {}
        else:
            if tyc_info == error:
                info = {}
            elif tyc_info == warn:
                info = {}
            elif tyc_info == null:
                info ={}
            elif tyc_info == wu:
                info ={}
            elif tyc_info == kon:
                info = {}
            elif tyc_info == {}:
                info = {}
            elif tyc_info == []:
                info = {}
            elif tyc_info == None:
                info = {}
            else:
                info = json.loads(tyc_info)
                #print 'ok'
        #finally:
        return info


    #实例化数据并且入库
    db = pymysql.connect(host = "127.0.0.1", user = "root", password = "123", db = "test15", port=3306, charset='utf8')
    cursor = db.cursor()
    select_sql = "SELECT * FROM tyc_all_info_1 WHERE name = '南通明德塑胶有限公司'"
    #WHERE name='欧普照明股份有限公司
    cursor.execute(select_sql)
    db.commit()
    cursor.close()
    db.close()
    for i in cursor.fetchall():
        id,company_name, ssxx,qybj, qyfz, sffx, jyfx, jyzk, zscq, jbxx = i
        print company_name
        try:
            provider_id = 0
            # qybj - ['基本信息','主要人员', '股东信息','变更记录','分支机构']
            #base_info = get_jbxx(jbxx)
            base_info = get_jbxx(jbxx)
            print base_info
            main_person = get_data_json(qybj,**zyry)
            print main_person
            shareholder_info = get_gdxx(qybj)
            print shareholder_info
            #print shareholder_info
            change_record = get_data_json(qybj,**bgjl)
            print change_record
            #change_record = []
            branch=get_data_json(qybj,**fzjg)
            print branch
            # qyfz - ['融资历史', '核心团队','企业业务']
            financing_history = get_data_qyfz(qyfz,**rzls)
            print financing_history
            core_team = get_data_qyfz(qyfz,**hxtd)
            print core_team
            enterprise_business = get_data_qyfz(qyfz,**qyyw)
            print enterprise_business
            # sffx - ['法律诉讼',  '法院公告', '失信人', '被执行人']
            legal_proceedings = get_data_json(sffx,**flss)
            print legal_proceedings
            court_notice = get_fygg(sffx)
            print court_notice
            dishonest_person = get_data_json(sffx,**sxr)
            print dishonest_person
            person_subjected_execution = get_data_json(sffx,**bzxr)
            print person_subjected_execution
            # jyfx - ['经营异常',  '行政处罚', '严重违法',  '股权出资, '动产抵押', '欠税公告',  ']
            abnormal_operation = get_data_json(jyfx, **jyyc)
            print abnormal_operation
            administrative_sanction = get_data_json(jyfx,**xzcf)
            print administrative_sanction
            serious_violation = get_data_json(jyfx, **yzwf)
            print serious_violation
            stock_ownership = get_data_json(jyfx, **gqcz)
            print stock_ownership
            chattel_mortgage = get_data_dcdy(jyfx, **dcdy)
            print chattel_mortgage
            tax_notice = get_data_json(jyfx,**qsgg)
            print tax_notice
            # jyzk - [ '招投标', '购地信息', '税务评级', '资质证书', ]
            bidding = get_data_json(jyzk, **ztb)
            print bidding
            purchase_information = get_data_json(jyzk, **xxgd)
            print purchase_information
            tax_rating = get_data_json(jyzk, **swpj)
            print tax_rating
            qualification_certificate = get_data_json(jyzk, **zzzs)
            print qualification_certificate
            # zscq - ['商标信息', '专利']
            trademark_information = get_data_json(zscq, **sbxx)
            print trademark_information
            patent = get_data_json(zscq, **zl)
            print patent
            print(u'数据准备好')

            try:
                db1 = pymysql.connect(host="127.0.0.1", user="root", password="123", db="tyc", port=3306, charset='utf8')
                cursor1 = db1.cursor()
                insert_sql = "INSERT INTO fq_provider_business_1 (`provider_id`,`base_info`,`main_person`,`shareholder_info`,`change_record`,`branchs`,`financing_history`,`core_team`,`enterprise_business`,`legal_proceedings`,`court_notice`,`dishonest_person`,`person_subjected_execution`,`abnormal_operation`,`administrative_sanction`,`serious_violation`,`stock_ownership`,`chattel_mortgage`,`tax_notice`,`bidding`,`purchase_information`,`tax_rating`,`qualification_certificate`,`trademark_information`,`patent`,company) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    provider_id, base_info, main_person, shareholder_info, change_record, branch, financing_history,
                    core_team, enterprise_business, legal_proceedings, court_notice, dishonest_person,
                    person_subjected_execution, abnormal_operation, administrative_sanction, serious_violation,
                    stock_ownership, chattel_mortgage, tax_notice, bidding, purchase_information, tax_rating,
                    qualification_certificate, trademark_information, patent, company_name)
                # print(insert_sql)
                # print('\n')
                cursor1.execute(insert_sql)
                db1.commit()
            except Exception as e:
                print e
                with open('error_company.text', 'a') as f:
                    f.write(company_name + '\n')
                db1.rollback()
        except Exception as e:
            with open('error_company.text','a') as f:
                f.write(company_name+"%sjson\n"%e)
            print(e)
if __name__ == '__main__':
    get_all_json()













