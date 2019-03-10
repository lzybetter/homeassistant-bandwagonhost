# homeassistant-bandwagonhost
用于home assistant平台的搬瓦工状态监视器,可以监视搬瓦工VPS的状态、流量、内存、硬盘和SWAP的使用情况。  
请将py文件复制到sensor文件夹下  

配置信息(必须)： 
  sensor:  
     - platform: bandwagonhost_sensor  
       veid: 搬瓦工VPS的veid  
       api_key: 搬瓦工VPS的API_KEY  

​       monitored_conditions:

   - VPS_STATE
   - CURRENT_BANDWIDTH_USED

- RAM_USED
- DISK_USED
- SWAP_USED


VPS的veid和API_KEY可以从搬瓦工的控制页面获取。