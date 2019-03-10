# homeassistant-bandwagonhost
用于home assistant平台的搬瓦工状态监视器,可以监视搬瓦工VPS的流量、内存和硬盘使用情况。  
请将py文件复制到sensor文件夹下  

配置信息：  
  sensor:  

   - platform: bandwagonhost_sensor  
       veid: 搬瓦工VPS的veid(必须)  
       api_key: 搬瓦工VPS的API_KEY(必须)  
       monitored_conditions:(可选)  
           - VPS_STAT(可选，VPS运行状态)  
           - CURRENT_BANDWIDTH_USED(可选，流量情况)  
           - RAM_USED(可选，已用内存)  
           - DISK_USED(可选，已用硬盘)  
           - SWAP_USED(可选，已用SWAP)  
  以上信息请从搬瓦工的控制页面获取。

效果如下：  
![image](https://github.com/lzybetter/homeassistant-bandwagonhost/raw/master/bandwagonhost.png)
