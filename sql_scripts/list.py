# -*- coding:utf-8 -*-

'''企业背景'''

#基本信息

jbxx={
	'sql':'jbxx',
	'legal_representative':u'法人代表',
	'registered_capital':u'注册资本',
	'registered_time':u'注册时间',
	'management_status':u'经营状况',
	'business_registration_number':u'工商注册号',
	'organization_code':u'组织机构代码',
	'uniform_credit_code':u'统一信用代码',
	'enterprise_type':u'企业类型',
	'industry':u'行业',
	'business_term':u'营业期限',
	'approval_date':u'核准日期',
	'registration_authority':u'登记机关',
	'registered_address':u'注册地址',
	'scope_of_business':u'经营范围',
	}

#主要人员
zyry={
	'sql':'qybj',
	'field':u'主要人员',
	'list':'result',
	'post':'typeJoin',
	'name':'name',
	}
	
#股东信息？？？
gdxx={
	'sql':'qybj',
	'field':u'股东信息',
	'list':'result',
	'shareholder':'name',
	'list1':'capital',
	'contributive_proportion':'percent',
	'subscribed_capital_contribution':'amomon',	
	}

#变更记录
bgjl={
	'sql':'qybj',
	'field':u'变更记录',
	'list':'result',
	'change_time':'changeTime',
	'change_project':'changeItem',
	'change_before':'contentAfter',
	}

#分支机构
fzjg={
	'sql':'qybj',
	'field':u'分支机构',
	'list':'result',
	'enterprise_name':'name',
	'legal_representative':'legalPersonName',
	'status':'regStatus',
	'register_time':'estiblishTime',
	}


'''企业发展'''
#融资历史
rzls={
	'sql':'qyfz',
	'field':u'融资历史',
	'list':'row',
	'time':'date',
	'round':'round',
	'valuation':'value',
	'money':'money',
	'proportion':'share',
	'investors':'Map',
	'news_source':'newsTitle',
	}

#核心团队
hxtd={
	'sql':'qyfz',
	'field':u'核心团队',
	'list':'rows',
	'name':'name',
	'logo_url':'icon',
	'post':'title',
	'content':'desc',
	}

#企业业务
qyyw={
	'sql':'qyfz',
	'field':u'企业业务',
	'list':'rows',
	'img_url':'logo',
	'business_name':'product',
	'business_introduce':'hangye',
	'content':'yewu',
	}

'''司法风险'''
#法律诉讼
flss={
	'sql':'sffx',
	'field':u'法律诉讼',
	'list':'items',
	'time':'submittime',
	'referee_documen':'title',
	'documen_type':'casetype',
	'document_number':'casetype',
	}

#法院公告
fygg={
	'sql':'sffx',
	'list':u'法院公告',
	'time':'publishdate',
	'appellant':'party1',
	'defendant':'party2',
	'announcement_type':'bltntypename',
	'court':'courtcode',	
	}

#失信人
sxr={
	'sql':'sffx',
	'field':u'失信人',
	'list':'items',
	'time':'publishdate',
	'case_no':'gistid',
	'court_execution':'courtname',
	'performance_status':'performance',
	'execution_reference_number':'casecode',
	}

#被执行人
bzxr={
	'sql':'sffx',
	'field':u'被执行人',
	'list':'items',
	'time':'caseCreateTime',
	'object_execution':'execMoney',
	'case_no':'caseCode',
	'court_justice':'execCourtName',
	}

'''经营风险'''
#经营异常
jyyc={
	'sql':'jyfx',
	'field':u'经营异常',
	'list':'result',
	'time':'putDate',
	'case':'putReason',
	'decision_organ':'putDepartment',
	}


#行政处罚
xzcf={
	'sql':'jyfx',
	'field':u'行政处罚',
	'list':'items',
	'time':'decisionDate',
	'letter_decision':'punishNumber',
	'type':'type',
	'decision_organ':'departmentName',
	}
#严重违法
yzwf={
	'sql':'jyfx',
	'field':u'严重违法',
	'list':'items',
	'time':'putDate',
	'executive_council':'putReason',
	'decision_organ':'putDepartment',
	}
#股权出质
gqcz={
	'sql':'jyfx',
	'field':u'股权出质',
	'list':'items',
	'time':'regDate',
	'registration_number':'regNumber',
	'pledgor':'pledgor',
	'apledgee':'pledgee',
	'status':'state',
	}
#动产抵押
dcdy={
	'sql':'jyfx',
	'field':u'动产抵押',
	'list':'items',
	'time':'regDate',
	'registration_number':'regNum',
	'types_secured_bonds':'type',
	'registration_authority':'regDepartment',
	'status':'status',
	}
	
#欠税公告!!!
qsgg={
	'sql':'jyfx',
	'field':u'欠税公告',
	'list':'items',
	'taxes_taxes':'taxCategory',
	'balance_tax_arrears':'ownTaxAmount',
	}

'''经营状况'''
#招投标
ztb={
	'sql':'jyzk',
	'field':u'招投标',
	'list':'items',
	'time':'publishTime',
	'title':'title',
	'purchaser':'purchaser',
	}
	
#购地信息
gdxx={
	'sql':'jyzk',
	'field':u'购地信息',
	'list':'companyPurchaseLandList',
	'time':'signedDate',
	'electronic_regulatory_number':'elecSupervisorNo',
	'agreed_commencement_date':'createTime',
	'gross_floor_area':'totalArea',
	'administrative_region':'location',
	}
	
#税务评级
swpj={
	'sql':'jyzk',
	'field':u'税务评级',
	'list':'items',
	'particular_year':'year',
	'tax_rating':'grade',
	'type':'type',
	'taxpayer_identification_number':'idNumber',
	'evaluation_unit':'evalDepartment',
	}
	
#资质证书???
zzzs={
	'sql':'jyzk',
	'field':u'资质证书',
	'list':'items',
	'device_name':'deviceName',
	'certificate_type':'licenceType',
	'date_issue':'issueDate',
	'closing_date':'toDate',
	'device_number':'deviceType',
	'license_number':'licenceNum',
	}

'''知识产权'''
#商标信息
sbxx={
	'sql':'zscq',
	'field':u'商标信息',
	'list':'items',
	'date_application':'appDate',
	'trademark':'tmPic',
	'trademark_name':'tmName',
	'register_number':'regNo',
	'type':'intCls',
	'status':'category',	
	}
	
#专利
zl={
	'sql':'zscq',
	'field':u'专利',
	'list':'items',
	'application_date':'applicationPublishTime',
	'patent_name':'patentName',
	'application_number':'patentNum',
	'application_publication_number':'applicationPublishNum',
	}





