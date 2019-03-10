# homeassistant-bandwagonhost
用于home assistant平台的搬瓦工状态监视器,可以监视搬瓦工VPS的流量、内存和硬盘使用情况。  
请将py文件复制到sensor文件夹下  

配置信息： 
  sensor:  

   - platform: bandwagonhost_sensor  
       veid: 搬瓦工VPS的veid(必须)  
       api_key: 搬瓦工VPS的API_KEY(必须)    

  以上信息请从搬瓦工的控制页面获取。
