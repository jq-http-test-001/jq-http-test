
import requests,json
import sys
import datetime
import pandas as pd
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO
print('请登陆')
global token
token = None
url="https://dataapi.joinquant.com/apis"
def auth(mob,pwd):
    global token
    body={  
        "method": "get_token",
        "mob": mob,  #mob是申请JQData时所填写的手机号
        "pwd": pwd,  #Password为聚宽官网登录密码，新申请用户默认为手机号后6位
    }
    response = requests.post(url, data = json.dumps(body))
    token=response.text
    if token =='error:auth failed':
        print('登陆失败,请检查账号')
    else:
        print('登陆成功')
    # print('token:   %s'%token)
def get_data(response):
    '''格式化数据为DataFrame'''
    return pd.read_csv(StringIO(response.text))




def http_get_all_securities(code='stock',date=None):
    body = {
    "method": "get_all_securities",
    "token": token,
    "code": code,
    "date": date
    }
    return  get_data(requests.post(url, data = json.dumps(body))).set_index('code')

# In[5]:



# In[13]:


def http_get_security_info(code):
    body ={
    "method": "get_security_info",
    "token": token,
    "code": code
    }
    return get_data(requests.post(url, data = json.dumps(body)))
# http_get_security_info('600741.XSHG')


# In[15]:


def http_get_index_stocks(code,date=None):
    body ={
    "method": "get_index_stocks",
    "token": token,
    "code": code,
    "date":date
    }
    return requests.post(url, data = json.dumps(body)).text.split('\n')
# http_get_index_stocks('000300.XSHG','2018-10-01')


# In[121]:


def http_get_margincash_stocks(date=None):
    '''date为非交易日或者不指定date,返回为空'''
    body ={
    "method": "get_margincash_stocks",
    "token": token,
    "date":date
    }
    return requests.post(url, data = json.dumps(body)).text.split('\n')
# print http_get_margincash_stocks('2018-10-01')
# print http_get_margincash_stocks()


# In[125]:


def http_get_marginsec_stocks(date=None):
    '''date为非交易日或者不指定date,返回为空'''
    body ={
    "method": "get_marginsec_stocks",
    "token": token,
    "date":date
    }
    return requests.post(url, data = json.dumps(body)).text.split('\n')
# print http_get_marginsec_stocks('2018-10-01')
# print http_get_marginsec_stocks()


# In[180]:


def http_get_locked_shares(code,date=None,end_date=None):
    body ={
    "method": "get_locked_shares",
    "token": token,
    'code':code,
    "date":date,
    "end_date":end_date
    }
    
    return get_data(requests.post(url, data = json.dumps(body)))
# http_get_locked_shares('600507.XSHG','2005-09-09','2018-09-29')


# In[182]:


def http_get_index_weights(code,date=None):
    body ={
    "method": "get_index_weights",
    "token": token,
    'code':code,
    "date":date,
    }
    
    return get_data(requests.post(url, data = json.dumps(body)))
# http_get_index_weights("000300.XSHG",'2018-01-02')


# In[194]:


def http_get_industries(code):
    body ={
    "method": "get_industries",
    "token": token,
    'code':code,
    }
    
    return get_data(requests.post(url, data = json.dumps(body)))
# http_get_industries("sw_l1")


# In[191]:


def http_get_industry(code,date):
    body ={
    "method": "get_industry",
    "token": token,
    'code':code,
    "date":date
    }
    
    return get_data(requests.post(url, data = json.dumps(body)))
# http_get_industry("000011.XSHE",'2018-01-01')
# 

# In[202]:


def http_get_industry_stocks(code,date):
    body ={
    "method": "get_industry_stocks",
    "token": token,
    'code':code,
    "date":date
    }
    
    return requests.post(url, data = json.dumps(body)).text.split('\n')
# http_get_industry_stocks("801760",'2018-01-01')


# In[200]:


def http_get_concepts():
    body ={
    "method": "get_concepts",
    "token": token,
    }
    
    return get_data(requests.post(url, data = json.dumps(body)))
# http_get_concepts()


# In[203]:


def http_get_concept_stocks(code,date):
    body ={
    "method": "get_concept_stocks",
    "token": token,
    "code":code,
    "date":date
    }
    
    return requests.post(url, data = json.dumps(body)).text.split('\n')
# http_get_concept_stocks('GN076','2018-01-01')


# In[51]:


def http_get_trade_days(date,end_date):
    body ={
    "method": "get_trade_days",
    "token": token,
    "date":date,
    "end_date":end_date,
    }
    
    return requests.post(url, data = json.dumps(body)).text.split('\n')
# d = http_get_trade_days('2005-01-01','2019-02-01')


# In[210]:


def http_get_all_trade_days():
    body ={
    "method": "get_all_trade_days",
    "token": token,
    }
    
    return requests.post(url, data = json.dumps(body)).text.split('\n')
# http_get_all_trade_days()


# In[55]:


def http_get_mtss(code,date,end_date):
    body ={
    "method": "get_mtss",
    "token": token,
    "code":code,
    "date":date,
    "end_date":end_date
    }
    
    return get_data(requests.post(url, data = json.dumps(body)))
# http_get_mtss('000001.XSHG','2018-01-01','2019-01-01')


# In[58]:


def http_get_money_flow(code,date,end_date):
    body ={
    "method": "get_money_flow",
    "token": token,
    "code":code,
    "date":date,
    "end_date":end_date
    }
    
    return get_data(requests.post(url, data = json.dumps(body)))
# http_get_money_flow('000001.XSHG','2018-01-01','2019-01-01')


# In[59]:


def http_get_billboard_list(code=None,date=None,end_date=None):
    body ={
    "method": "get_billboard_list",
    "token": token,
    "code":code,
    "date":date,
    "end_date":end_date,
    }
    
    return get_data(requests.post(url, data = json.dumps(body)))
# http_get_billboard_list(code = '000001.XSHE',date='2017-01-01',end_date='2019-01-01')


# In[61]:


def http_get_future_contracts(code=None,date=None):
    body ={
    "method": "get_future_contracts",
    "token": token,
    "code":code,
    "date":date,
    }
    
    return requests.post(url, data = json.dumps(body)).text.split('\n')
# http_get_future_contracts('FU',date='2019-02-02')


# In[71]:


def http_get_dominant_future(code=None,date=None):
    body ={
    "method": "get_dominant_future",
    "token": token,
    "code":code,
    "date":date,
    }
    return requests.post(url, data = json.dumps(body)).text
# http_get_dominant_future('AG',date='2019-01-09')


# In[78]:


def http_get_fund_info(code=None,date=None):
    body ={
    "method": "get_fund_info",
    "token": token,
    "code":code,
    "date":date,
    }
    return eval(requests.post(url, data = json.dumps(body)).text)
# http_get_fund_info("510050.XSHG",date='2019-02-02')
# 

# In[81]:


def http_get_current_tick(code=None):
    '''获取的数据没对齐'''
    body ={
    "method": "get_current_tick",
    "token": token,
    "code":code,
    }
    # print (requests.post(url, data = json.dumps(body)).text)
    return get_data((requests.post(url, data = json.dumps(body))))#.iloc[0]
# http_get_current_tick("IF1902.CCFX").T
# import jq
# jq.get_current_tick('600741.XSHG').T


# In[82]:


# import jq
# jq.get_current_tick("IF1902.CCFX")


# In[130]:


def http_get_extras(code,date,end_date):
    body ={
    "method": "get_extras",
#     "token": token,
    "code":code,
    "date":date,
    "info":'futures_positions',
    "end_date":end_date
    }
    return get_data((requests.post(url, data = json.dumps(body))))#.iloc[0]
# http_get_extras("510050.XSHG",'2018-05-29','2018-10-01')
# http_get_extras("510050.XSHG",'2015-04-24','2018-10-01')


# In[120]:


def http_get_price(code,count,unit,end_date,fq_ref_date=None):
    '''分钟数据出现多余的夜盘'''
    body ={
    "method": "get_bars",
    "token": token,
    "code": code,
    "count": count,
    "unit": unit,
    "end_date": end_date,
    "fq_ref_date": fq_ref_date,
    }
    print(requests.post(url, data = json.dumps(body)).text)
    return  get_data(requests.post(url, data = json.dumps(body))).set_index('date')
# http_get_price("XXX.X SGE",30,'15m','2018-10-01')


# In[113]:


# http_get_price("TF1903.CCFX",280,'1m','2019-02-02')


# In[118]:


# http_get_price("XXXXX.CCFX",280,'1m','2019-02-02')


# In[96]:


def http_get_ticks(code,count,end_date):
    body ={
    "method": "get_ticks",
    "token": token,
    "code": code,
    "count": count,
    "end_date": end_date,
    }
    data = get_data(requests.post(url, data = json.dumps(body))).set_index('time')
    data.index.astype(datetime.datetime)
    return  data
# df = http_get_ticks('IF1902.CCFX',end_date='2019-01-30',count=5)
# df

