import logging

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_MONITORED_CONDITIONS, CONF_NAME
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
import requests
import json

_Log=logging.getLogger(__name__)

DEFAULT_NAME = '搬瓦工状态'
CONF_VEID = 'veid'
CONF_API_KEY = 'api_key'
MONITORED_CONDITIONS = {
    'ATTR_CURRENT_BANDWIDTH_USED': ['Current Bandwidth Used', '',
                                  'mdi:cloud-tags'],
    'ATTR_DISK_USED': ['DISK USED', '', 'mdi:disc'],
    'ATTR_RAM_USDE':['RAM USED', '', 'mdi:responsive'],
}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_VEID): cv.string,
    vol.Required(CONF_API_KEY): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})


API_URL = "https://api.64clouds.com/v1/getLiveServiceInfo?"

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the sensor platform."""
    veid = config.get(CONF_VEID)
    api_key = config.get(CONF_API_KEY)
    sensor_name = config.get(CONF_NAME)
    monitored_conditions = list(MONITORED_CONDITIONS)

    sensors = []

    for condition in monitored_conditions:

        sensors.append(BandwagonHostSensor(sensor_name, veid, api_key, condition))

    add_entities(sensors, True)


class BandwagonHostSensor(Entity):

    def __init__(self,sensor_name,veid, api_key, condition):
        
        if(sensor_name == '搬瓦工状态'):
            sensor_name = condition.replace('ATTR_','').replace('_', ' ')
        else:
            sensor_name = sensor_name
        self.attributes = {}
        self._state = None
        self._name = sensor_name
        self._condition = condition
        self._veid = veid
        self._api_key = api_key

        condition_info = MONITORED_CONDITIONS[condition]

        self._condition_name = condition_info[0]
        self._units = condition_info[1]
        self._icon = condition_info[2]

    @property
    def name(self):
        """Return the name of the sensor."""
        try:
            return self._name.format(self._condition_name)
        except IndexError:
            try:
                return self._name.format(
                    self.data['label'], self._condition_name)
            except (KeyError, TypeError):
                return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """返回图标."""
        return self._icon

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.attributes

    @property
    def unit_of_measurement(self):
        self._units




    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        try:
            response = requests.get(API_URL + 'veid=' + self._veid + '&api_key=' + self._api_key)
            json_obj = json.loads(response.text)

            if self._condition == 'ATTR_CURRENT_BANDWIDTH_USED':
                self._state = str(round(json_obj['data_counter']/1024/1024/1024,2)) + 'GB/1000GB'
            elif self._condition == 'ATTR_DISK_USED':
                self._state = str(round(json_obj['ve_used_disk_space_b']/1024/1024/1024,2)) + 'GB/20GB'
            elif self._condition == 'ATTR_RAM_USDE':
                self._state = str(round((json_obj['plan_ram'] - json_obj['mem_available_kb']*1024)/1024/1024/1024,2)) + 'GB/1GB'
            else:
                self._state = "something wrong"
        except ConnectionError:
                _Log.error("搬瓦工：连接错误，请检查网络")